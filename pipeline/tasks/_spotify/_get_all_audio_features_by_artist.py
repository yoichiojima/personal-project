from tqdm import tqdm
import json
import sys

import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from _spotify.spotipy_auth import spotipy_auth
from _auth.get_project_id import get_project_id
from _auth.google_auth import google_auth
from _storage.upload_blob_from_memory import upload_blob_from_memory
from _logging.logger import Logger

logger = Logger()

spotipy_auth()
google_auth()

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
artist_id = "3WrFJ7ztbogyGnTHbHJFl2"


def _get_albums(artist_id: str) -> list:
    """
    Returns a list of albums for a given artist_id
        Parameters:
            artist_id (str): Spotify artist id
        Returns:
            list: list of albums
    """
    albums = []

    result = sp.artist_albums(artist_id)

    for i in result["items"]:
        d = {}
        d["id"] = i["id"]
        d["name"] = i["name"]
        albums.append(d)

    while result["next"]:
        result = sp.next(result)

        for i in result["items"]:
            d = {}
            d["id"] = i["id"]
            d["name"] = i["name"]
            albums.append(d)

    return albums


def _get_tracks(album_id: str) -> list:
    """
    Returns a list of tracks for a given album_id
        Parameters:
            album_id (str): Spotify album id
        Returns:
            list: list of tracks
    """
    tracks = []

    result = sp.album_tracks(album_id)
    for i in result["items"]:
        d = {}
        d["id"] = i["id"]
        d["name"] = i["name"]
        d["album_id"] = album_id
        tracks.append(d)

    while result["next"]:
        result = sp.next(result)
        for i in result["items"]:
            d = {}
            d["id"] = i["id"]
            d["name"] = i["name"]
            d["album_id"] = album_id
            tracks.append(d)

    return tracks


def store_albums(albums, artist_id):
    pd.DataFrame(albums).to_csv(
        f"gs://{get_project_id()}/spotify/albums/{artist_id}.csv",
        index=False,
        encoding="utf-8",
    )
    logger.info(f"gs://spotify/albums/{artist_id}.csv uploaded.")


def get_albums_tracks(album_ids):
    tracks = []

    for i in tqdm(album_ids, desc="downloading tracks data"):
        result = _get_tracks(i)
        for j in result:
            tracks.append(j)

    return tracks


def store_tracks(tracks, artist_id):
    pd.DataFrame(tracks).to_csv(
        f"gs://{get_project_id()}/spotify/tracks/{artist_id}.csv",
        index=False,
        encoding="utf-8",
    )
    logger.info(f"gs://{get_project_id()}/spotify/tracks/{artist_id}.csv uploaded.")


def get_audio_features(track_ids: list) -> pd.DataFrame:
    audio_features = []
    for i in tqdm(track_ids, desc="downloading audio features"):
        for i in sp.audio_features(i):
            audio_features.append(i)

    return pd.DataFrame(audio_features)


def store_audio_features(audio_features: pd.DataFrame, artist_id: int):
    audio_features.to_csv(
        f"gs://{get_project_id()}/spotify/audio_features/{artist_id}.csv",
        index=False,
        encoding="utf-8",
    )
    logger.info(f"audio_features/{artist_id}.csv uploaded.")


def get_all_audio_features_by_artist(artist_id: str):
    albums = _get_albums(artist_id)
    store_albums(albums, artist_id)

    album_ids = [i["id"] for i in albums]
    tracks = get_albums_tracks(album_ids)
    store_tracks(tracks, artist_id)

    track_ids = [i["id"] for i in tracks]
    audio_features = get_audio_features(track_ids)
    store_audio_features(audio_features, artist_id)


if __name__ == "__main__":
    get_all_audio_features_by_artist(sys.argv[1])
