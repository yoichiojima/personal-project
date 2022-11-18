import sys
import pandas as pd
from _auth.get_project_id import get_project_id
from _auth.google_auth import google_auth
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from _spotify import spotipy_auth


google_auth()


def download_audio_features(artist_id: list) -> pd.DataFrame:
    return pd.read_csv(
        f"gs://{get_project_id()}/spotify/audio_features/{artist_id}.csv"
    )


def _track(track_id: str) -> dict:
    spotipy_auth()

    sp = Spotify(auth_manager=SpotifyClientCredentials())
    res_track = sp.track(track_id)
    res_album = res_track["album"]

    artist = [(i["id"], i["name"]) for i in res_album["artists"]][0]
    album = (res_album["id"], res_album["name"])
    popularity = res_track["popularity"]

    return {"artist": artist, "album": album, "popularity": popularity}


def deconstruct_track_dict(audio_features: pd.DataFrame) -> pd.DataFrame:
    audio_features["track_info"] = audio_features["id"].apply(_track)
    audio_features["artist_id"] = audio_features["track_info"].apply(
        lambda x: x["artist"][0]
    )
    audio_features["artist_name"] = audio_features["track_info"].apply(
        lambda x: x["artist"][1]
    )
    audio_features["album_id"] = audio_features["track_info"].apply(
        lambda x: x["album"][0]
    )
    audio_features["album_name"] = audio_features["track_info"].apply(
        lambda x: x["album"][1]
    )
    audio_features["popularity"] = audio_features["track_info"].apply(
        lambda x: x["popularity"]
    )
    audio_features = audio_features.drop(columns=["track_info"])
    return audio_features


def main(artist_id: str) -> pd.DataFrame:
    audio_features = download_audio_features(artist_id)
    audio_features = deconstruct_track_dict(audio_features)
    return audio_features


if __name__ == "__main__":
    main(sys.argv[1])
