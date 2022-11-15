import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from _spotify.spotipy_auth import spotipy_auth

def parse_album(album):
    response = {}
    keys_to_save = [key for key in album.keys() if key not in ['external_urls', 'available_markets', 'Images']]
    for i in keys_to_save:
        response[i] = album[i]
    response['external_urls'] = album['external_urls']['spotify']
    response['image_url'] = album['images'][0]['url']
    return response

def get_albums_by_artist(album_id):
    spotipy_auth()
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    albums = sp.artist_albums(album_id)['items']
    return [parse_album(album) for album in albums]