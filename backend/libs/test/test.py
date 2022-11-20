import sys

sys.path.append("..")
from spotify.client import Client as SpotifyClient


def test_retrieve_album_tracks():
    res = SpotifyClient.retrieve_audio_features_global()
    print(res)


test_retrieve_album_tracks()
