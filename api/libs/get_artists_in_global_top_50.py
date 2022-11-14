import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from _spotify.spotipy_auth import spotipy_auth

from ._get_artists_in_global_top_50 import _get_artists_in_global_top_50


def get_artists_in_global_top_50() -> list:
    spotipy_auth()
    ids = [i["id"] for i in _get_artists_in_global_top_50()]
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    return [sp.artist(_id) for _id in ids]


if __name__ == "__main__":
    print(get_artists_in_global_top_50())
