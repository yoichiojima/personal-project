import pandas as pd
from spotipy import Spotify, SpotifyClientCredentials
from _spotify.spotipy_auth import spotipy_auth
from _auth.google_auth import google_auth


def retrieve_playlist_audio_features(playlist_id: str) -> dict:
    google_auth()
    spotipy_auth()

    sp = Spotify(auth_manager=SpotifyClientCredentials())

    res = sp.playlist_items(playlist_id, limit=50)

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

    df = df.reset_index()
    df.columns = ["feature", "mean", "std"]

    return df.to_dict()
