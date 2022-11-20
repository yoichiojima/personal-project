from datetime import datetime
import pandas as pd
from spotipy import Spotify, SpotifyClientCredentials
from _spotify.spotipy_auth import spotipy_auth
from _auth.google_auth import google_auth
from _logging.logger import Logger

logger = Logger()


spotipy_auth()
sp = Spotify(auth_manager=SpotifyClientCredentials())


def retrieve_artist_album(artist_id: str) -> list:
    """
    Returns a list of albums for an artist
        Parameters:
            artist_id (str): artist id
        Returns:
            list: list of albums
    """

    def _reduce_albums_to_id_and_name(item: dict) -> dict:
        return {"id": item["id"], "name": item["name"]}

    albums = []
    res = sp.artist_albums(artist_id=artist_id)
    for i in res["items"]:
        albums.append(_reduce_albums_to_id_and_name(i))

    while res["next"]:
        res = sp.next(res)
        for i in res["items"]:
            albums.append(_reduce_albums_to_id_and_name(i))

    return albums


def retrieve_album_tracks(album_id: str) -> list:
    """
    Returns a list of tracks for an album
        Parameters:
            album_id (str): album id
        Returns:
            list: list of tracks
    """
    tracks = []

    res = sp.album_tracks(album_id=album_id)
    for i in res["items"]:
        tracks.append(i)

    while res["next"]:
        res = sp.next(res)
        for i in res["items"]:
            tracks.append(i)

    response = []
    for tr in tracks:
        response.append(
            {
                "id": tr["id"],
                "name": tr["name"],
            }
        )

    return response


def retrieve_album_tracks_handler(artist_album: list) -> list:
    """
    Returns a list of tracks for each album
        Parameters:
            artist_album (list): list of albums
        Returns:
            list: list of tracks
    """
    tracks = []
    for i in artist_album:
        tracks = tracks + retrieve_album_tracks(i["id"])

    return tracks


def retrieve_audio_features(track_id: str) -> dict:
    return sp.audio_features(track_id)[0]


def retrieve_audio_features_handler(tracks: list) -> list:
    return [
        {"audio_features": retrieve_audio_features(i["id"]), "track": i} for i in tracks
    ]


# Standardise audio features
def _standardise(audio_features: pd.DataFrame, reference: pd.DataFrame) -> pd.DataFrame:
    metrics = [
        "danceability",
        "energy",
        "loudness",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
        "duration_ms",
    ]

    for m in metrics:
        audio_features[m] = (
            audio_features[m] - reference.loc[m, "mean"]
        ) / reference.loc[m, "std"]

    return audio_features[metrics].T.to_dict()[0]


class Client:
    @staticmethod
    def artist(artist_id: str) -> dict:
        return sp.artist(artist_id)

    @staticmethod
    def audio_features_from_artist_id(artist_id: str) -> list:
        artist = sp.artist(artist_id)
        artist_name = artist["name"]

        albums = retrieve_artist_album(artist_id)
        tracks = retrieve_album_tracks_handler(albums)
        print(
            f"{'=' * 50}\n"
            f"Retrieving audio features...\n"
            f"Numbers of albums: {len(albums)}\n"
            f"Numbers of tracks: {len(tracks)}\n"
            f"{'=' * 50}"
        )
        audio_features = retrieve_audio_features_handler(tracks)

        res = {}
        res["audio_features"] = audio_features
        res["artist_name"] = artist_name

        return res

    @staticmethod
    def audio_features_from_album_id(album_id: str) -> list:
        album = sp.album(album_id)
        tracks = retrieve_album_tracks(album_id)
        print(
            f"{'=' * 50}\n"
            f"Retrieving audio features...\n"
            f"Numbers of tracks: {len(tracks)}\n"
            f"{'=' * 50}"
        )
        audio_features = retrieve_audio_features_handler(tracks)

        res = {}
        res["album"] = album
        res["audio_features"] = audio_features

        return res

    @staticmethod
    def audio_features_from_track_id(track_id: str) -> list:
        track = sp.track(track_id)
        audio_features = retrieve_audio_features(track_id)

        res = {}
        res["track"] = track
        res["audio_features"] = audio_features

        features = [
            "danceability",
            "energy",
            "loudness",
            "speechiness",
            "acousticness",
            "instrumentalness",
            "liveness",
            "valence",
            "tempo",
        ]

        chart_values = []
        for i in audio_features:
            if i in features:
                chart_values.append(audio_features[i])

        data = {
            "options": {
                "chart": {
                    "id": "basic-bar",
                },
                "xaxis": {
                    "categories": features,
                },
            },
            "series": [
                {
                    "name": "series-1",
                    "data": chart_values,
                },
            ],
        }

        return data

    @staticmethod
    def retrieve_audio_features_global():
        google_auth()
        spotipy_auth()

        sp = Spotify(auth_manager=SpotifyClientCredentials())

        res = sp.playlist_items("37i9dQZEVXbMDoHDwVN2tF", limit=50)

        tracks = [
            {
                "id": i["track"]["id"],
                "name": i["track"]["name"],
                "artist": i["track"]["artists"][0]["name"],
            }
            for i in res["items"]
        ]

        audio_features = [
            {
                "name": i["name"],
                "artist": i["artist"],
                "features": sp.audio_features(i["id"]),
            }
            for i in tracks
        ]

        dfs = []
        for i in audio_features:
            df = pd.DataFrame(i["features"])
            df["name"] = i["name"]
            df["artist"] = i["artist"]
            dfs.append(df)

        df = pd.concat(dfs)

        df = df[
            [
                "id",
                "name",
                "artist",
                "key",
                "mode",
                "tempo",
                "danceability",
                "energy",
                "loudness",
                "speechiness",
                "acousticness",
                "instrumentalness",
                "liveness",
                "valence",
                "duration_ms",
                "time_signature",
            ]
        ]

        df = df.describe()
        df = pd.concat([df.mean(), df.std()], axis=1)

        df.columns = ["mean", "std"]

        return df.to_dict()

    @staticmethod
    def retirieve_standardised_audio_features(track_id: str) -> dict:
        google_auth()
        spotipy_auth()

        # Get Reference
        global_top = pd.read_csv(
            "gs://yo-personal-project/spotify/audio_features/37i9dQZEVXbMDoHDwVN2tF/2022-11-20.csv"
        ).set_index("feature")

        # Get audio features from track_id
        sp = Spotify(auth_manager=SpotifyClientCredentials())
        audio_features = pd.DataFrame(sp.audio_features(tracks=track_id))

        # Standardise audio features by global 50
        return _standardise(audio_features, global_top)
