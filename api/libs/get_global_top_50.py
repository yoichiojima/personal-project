import sys
from datetime import datetime
import pandas as pd
from _auth.get_authenticated import get_authenticated
from _auth.get_project_id import get_project_id


def get_global_top_50(_date):
    get_authenticated()
    project_id = get_project_id()
    df = pd.read_csv(f"gs://{project_id}/spotify/global_top_50/{_date}.csv")
    return df.to_dict('tight')


if __name__ == "__main__":
    print(get_global_top_50(datetime.strptime(sys.argv[1], "%Y-%m-%d")))
