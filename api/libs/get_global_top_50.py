import sys
from datetime import datetime
import pandas as pd
from _auth.google_auth import google_auth
from _auth.get_project_id import get_project_id


def get_global_top_50(_date: datetime)-> dict:
    google_auth()
    return pd.read_csv(
        f"gs://{get_project_id()}"
        f"/spotify/global_top_50/{_date}.csv"
    ).to_dict('tight')


if __name__ == "__main__":
    print(get_global_top_50(datetime.strptime(sys.argv[1], "%Y-%m-%d")))
