import sys
from datetime import datetime
import pandas as pd
from _auth.get_authenticated import get_authenticated
from _auth.get_project_id import get_project_id
from _storage.list_blobs import list_blobs

def get_global_top_50(_date: datetime) -> dict:

    get_authenticated()

    project_id = get_project_id()

    df = pd.concat([pd.read_csv(f"gs://{project_id}/{i}") for i in list_blobs(project_id)])
    df['added_at'] = pd.to_datetime(pd.to_datetime(df['added_at']).dt.tz_localize(None))
    df['added_at_date'] = pd.to_datetime(df['added_at'].dt.date)
    df = df[df['added_at_date'] == _date]

    df['added_at'] = df['added_at'].apply(lambda dt: dt.strftime('%Y-%m-%d %H:%M:%S'))
    df['added_at_date'] = df['added_at_date'].apply(lambda dt: dt.strftime('%Y-%m-%d'))
    
    return df.to_dict() 

if __name__ == "__main__":
    print(get_global_top_50(datetime.strptime(sys.argv[1], "%Y-%m-%d")))