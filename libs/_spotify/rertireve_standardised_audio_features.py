import sys
import pandas as pd
from spotipy import Spotify, SpotifyClientCredentials
from _auth.google_auth import google_auth
from _spotify.spotipy_auth import spotipy_auth


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


if __name__ == "__main__":
    print(retirieve_standardised_audio_features(sys.argv[1]))
