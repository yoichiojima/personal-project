import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from _spotify.spotipy_auth import spotipy_auth

def artist(artist_id):
    spotipy_auth()
    return spotipy.Spotify(
        client_credentials_manager = SpotifyClientCredentials()
    ).artist(artist_id)