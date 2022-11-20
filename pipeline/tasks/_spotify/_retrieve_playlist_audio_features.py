import sys
from datetime import datetime
import pandas as pd
from spotipy import Spotify, SpotifyClientCredentials
from _spotify.spotipy_auth import spotipy_auth
from _auth.google_auth import google_auth
from _auth.get_project_id import get_project_id
from _logging.logger import Logger


def retrieve_playlist_audio_features(playlist_id: str) -> dict:    
    google_auth()
    spotipy_auth()

    sp = Spotify(auth_manager=SpotifyClientCredentials())

    sp = Spotify(
        auth_manager = SpotifyClientCredentials()
    )

    res = sp.playlist_items(playlist_id, limit = 50)

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

    df = df.describe()
    df = pd.concat([df.mean(), df.std()], axis = 1)

    df.columns = ['mean', 'std']
    
    df.to_csv(f'gs://{get_project_id()}/spotify/audio_features/{playlist_id}/{datetime.today().strftime("%Y-%m-%d")}.csv', index = True, encoding = 'utf-8')

    logger = Logger()
    logger.info('audio features global uploaded.')


if __name__ == '__main__':
    retrieve_playlist_audio_features(sys.argv[1])