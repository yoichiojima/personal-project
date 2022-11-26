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
    apx.set_chart_id("chart_id")
    apx.set_xaxis_categories(["a", "b", "c"])
    apx.set_series_name("series_name")
    apx.set_series_data([1, 2, 3])
    return apx.res
