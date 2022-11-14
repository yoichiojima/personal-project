import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from _spotify.spotipy_auth import spotipy_auth


def _get_artists_in_global_top_50() -> list:
    spotipy_auth()
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    playlist_tracks = sp.playlist_tracks(playlist_id="37i9dQZEVXbMDoHDwVN2tF", limit=50)

    track_artists = [
        item["track"]["album"]["artists"] for item in playlist_tracks["items"]
    ]
    artists_appeared = []
    for artists in track_artists:
        for artist in artists:
            artists_appeared.append(artist)

    return artists_appeared


if __name__ == "__main__":
    print(_get_artists_in_global_top_50())
