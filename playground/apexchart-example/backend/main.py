from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from libs.apex_chart import ApexChart


app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test")
def test():
    apx = ApexChart()
    apx.set_options(
        id="basic-bar",
        categories=[
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
        background="#f4f4f4",
        fore_color="#333",
    )
    apx.set_series_data([{"data": [44, 55, 41, 67, 22, 43, 21, 49, 44, 62, 21, 49]}])
    return apx.res
