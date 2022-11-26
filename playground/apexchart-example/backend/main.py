from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from random import randint


app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/monthly_multiple_series")
def monthly_multiple_series():
    res = {}
    res["options"] = {
        "chart": {
            "id": "basic-bar",
            "categories": [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
                "Nov",
                "Dec",
            ],
            "foreColor": "black",
        },
        "theme": {"mode": "dark", "palette": "palette2"},
    }
    res["series"] = [
        {"data": [randint(0, 100) for _ in range(12)]},
        {"data": [randint(0, 100) for _ in range(12)]},
    ]

    return res


@app.get("/radar")
def radar():
    res = {}
    res["options"] = {
        "labels": ["April", "May", "June", "July", "August", "September"],
        "theme": {"mode": "light", "palette": "palette2"},
    }

    res["series"] = [
        {"data": [randint(0, 100) for _ in range(6)]},
        {"data": [randint(0, 100) for _ in range(6)]},
    ]

    return res
