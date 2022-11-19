from datetime import datetime
import pandas as pd
from spotipy import Spotify, SpotifyClientCredentials
from _spotify.spotipy_auth import spotipy_auth
from _auth.google_auth import google_auth
from _auth.get_project_id import get_project_id
from _logging.logger import Logger

logger = Logger()


spotipy_auth()
sp = Spotify(auth_manager=SpotifyClientCredentials())


def retrieve_audio_features_global():
    google_auth()
    spotipy_auth()

    sp = Spotify(
        auth_manager = SpotifyClientCredentials()
    )

    res = sp.playlist_items('37i9dQZEVXbMDoHDwVN2tF', limit = 50)

    tracks = [{
        'id' : i['track']['id'], 
        'name': i['track']['name'], 
        'artist': i['track']['artists'][0]['name']
    } for i in res['items']]

    audio_features = [{
        'name': i['name'], 
        'artist': i['artist'], 
        'features': sp.audio_features(i['id'])
    } for i in tracks]

    dfs = []
    for i in audio_features:
        df = pd.DataFrame(i['features'])
        df['name'] = i['name']
        df['artist'] = i['artist']
        dfs.append(df)

    df = pd.concat(dfs)


    df = df[[
        'id',
        'name',
        'artist',
        'key',
        'mode',
        'tempo',
        'danceability',
        'energy',
        'loudness',
        'speechiness',
        'acousticness',
        'instrumentalness',
        'liveness',
        'valence',
        'duration_ms',
        'time_signature',
    ]]

    (
        df.describe()
        .to_csv(
            f'gs://{get_project_id()}/spotify/global_audio_features/'
            f'{datetime.today().strftime("%Y-%m-%d")}.csv', 
            index = True, 
            encoding = 'utf-8'
        )
    )