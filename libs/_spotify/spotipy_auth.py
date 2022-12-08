import os
from configparser import ConfigParser

def spotipy_auth():
    config = ConfigParser()
    config.read('/opt/spotify.ini')
    os.environ['SPOTIPY_CLIENT_ID'] = config['spotify']['SpotifyClientId']
    os.environ['SPOTIPY_CLIENT_SECRET'] = config['spotify']['SpotifyClientSecret']

if __name__ == "__main__":
    spotipy_auth()
    print(f"Environment variable for spotipy is all set.\n"
          f"SPOTIPY_CLIENT_ID: {os.environ['SPOTIPY_CLIENT_ID']}")