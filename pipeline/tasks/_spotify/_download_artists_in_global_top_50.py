import json
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from _storage.upload_blob_from_memory import upload_blob_from_memory
from _auth.get_project_id import get_project_id
from _auth.google_auth import google_auth
from _spotify.spotipy_auth import spotipy_auth
from _logging import Logger

logger = Logger()

spotipy_auth()


def _get_artists_in_global_top_50() -> list:
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


def get_artists_in_global_top_50() -> list:
    ids = [i["id"] for i in _get_artists_in_global_top_50()]
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    return [sp.artist(_id) for _id in ids]


def download_artists_in_global_top_50():
    artists_in_global_top_50 = get_artists_in_global_top_50()
    json_to_upload = json.dumps(artists_in_global_top_50)

    google_auth()
    project_id = get_project_id()
    timestamp = datetime.now().strftime("%Y-%m-%d")
    upload_blob_from_memory(
        bucket_name=project_id,
        contents=json_to_upload,
        destination_blob_name=f"spotify/artists_in_global_top_50/{timestamp}.json",
    )
    logger.info("artists_in_global_top_50.json uploaded to GCS")


if __name__ == "__main__":
    print(download_artists_in_global_top_50())
