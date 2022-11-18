from datetime import datetime
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