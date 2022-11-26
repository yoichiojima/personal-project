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
    apx.set_data([100, 200, 350, 330, 400])
    return apx.data
