import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from datetime import datetime

from spotipy_auth import spotipy_auth
spotipy_auth()
from google_auth import google_auth
google_auth()

def download_top_50_global():
    spotify = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials())

    result = spotify.playlist_tracks(playlist_id = '37i9dQZEVXbMDoHDwVN2tF', 
                                     limit = 50)
    
    df = pd.DataFrame(result['items'])
    df = df[['added_at',
             'track']]

    df = df.copy()
    df['track_id'] = df['track'].apply(lambda row: row['id'])

    df['track_name'] = df['track'].apply(lambda row: row['name'])
    df['artists_id'] = df['track'].apply(lambda row: [artist['id'] for artist in row['artists']])
    df['artists_name'] = df['track'].apply(lambda row: [artist['name'] for artist in row['artists']])

    df = df[['track_name', 
               'artists_name', 
               'added_at',
               'track_id', 
               'artists_id']]

    timestamp = datetime.now().strftime('%Y-%m-%d')

    df.to_csv(f'/app/bucket/spotify/global_top_50/{timestamp}.csv', 
               index = False, 
               encoding = 'utf_8_sig')

if __name__ == '__main__':
    download_top_50_global()