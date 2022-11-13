from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from libs.get_global_top_50 import get_global_top_50

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


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/global_top_50")
async def global_top_50(date: str):
    return get_global_top_50(date)
