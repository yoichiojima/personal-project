import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from _spotify.spotipy_auth import spotipy_auth


def get_artist(artist_id):
    spotipy_auth()
    return spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials()
    ).artist(artist_id)


if __name__ == "__main__":
    print(get_artist(sys.argv[1]))
