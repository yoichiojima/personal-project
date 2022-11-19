from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from libs.spotify.client import Client as SpotifyClient

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/audio-features-from-album-id/")
def audio_features_from_album_id(album_id: str) -> list:
    return SpotifyClient.audio_features_from_album_id(album_id)


@app.get("/artist/")
def artist(artist_id: str) -> dict:
    return SpotifyClient.artist(artist_id)


@app.get("/rader-chart/")
def rader_chart(track_id: str) -> list:
    return SpotifyClient.audio_features_from_track_id(track_id)


@app.get('/retrieve_audio_features_global/')
def retrieve_audio_features_global():
    return SpotifyClient.retrieve_audio_features_global()