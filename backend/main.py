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


@app.get("/search/")
def search(query: str) -> dict:
    return SpotifyClient.search(query)


@app.get("/artist/")
def artist(artist_id: str) -> dict:
    return SpotifyClient.artist(artist_id)


@app.get("/artist_albums/")
def artist_albums(artist_id: str) -> dict:
    return SpotifyClient.artist_albums(artist_id)


@app.get("/album/")
def album(album_id: str) -> dict:
    return SpotifyClient.album(album_id)


@app.get("/album_tracks/")
def album_tracks(album_id: str) -> dict:
    return SpotifyClient.album_tracks(album_id)


@app.get("/track/")
def track(track_id: str) -> dict:
    return SpotifyClient.track(track_id)


@app.get("/audio_features/")
def audio_features(track_id: str) -> dict:
    return SpotifyClient.audio_features(track_id)


@app.get("/audio_analysis/")
def audio_analysis(track_id: str) -> dict:
    return SpotifyClient.audio_analysis(track_id)


@app.get("/artist_related_artists/")
def artist_related_artists(artist_id: str) -> dict:
    return SpotifyClient.artist_related_artists(artist_id)


@app.get("/artist_top_tracks/")
def artist_top_tracks(artist_id: str) -> dict:
    return SpotifyClient.artist_top_tracks(artist_id)


@app.get("/new_releases/")
def new_releases() -> dict:
    return SpotifyClient.new_releases()


@app.get("/audio-features-from-album-id/")
def audio_features_from_album_id(album_id: str) -> list:
    return SpotifyClient.audio_features_from_album_id(album_id)


@app.get("/audio_features_global/")
def åaudio_features_global():
    return SpotifyClient.retrieve_audio_features_global()


@app.get("/standardised_audio_features/")
def standardised_audio_features(track_id: str):
    return SpotifyClient.standardised_audio_features(track_id)


@app.get("/standardised_audio_features_radar/")
def standardised_audio_features_radar(track_id: str):
    return SpotifyClient.standardised_audio_features_radar(track_id)
