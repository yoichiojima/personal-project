from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from libs.apex_chart import ApexChart
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
    apx = ApexChart()
    apx.set_options({
        'chart': {
            'id': "basic-bar",
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
                "Dec"
            ], 
            'foreColor': 'black'
        }, 
        'theme': {
            'mode': 'dark', 
            'palette': 'palette2'
        }
    })
    apx.set_series_data([
        {"data": [randint(0, 100) for _ in range(12)]},
        {"data": [randint(0, 100) for _ in range(12)]}
    ])

    return apx.res

@app.get("/radar")
def radar():
    apx = ApexChart()

    apx.set_options({
        'labels': ['April', 'May', 'June', 'July', 'August', 'September'], 
        'theme': {
            'mode': 'light', 
            'palette': 'palette2'
        }
    })
    
    apx.set_series_data([
        {"data": [randint(0, 100) for _ in range(6)]},
        {"data": [randint(0, 100) for _ in range(6)]}
    ])
    
    return apx.res
