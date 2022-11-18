import sys
import json
from datetime import datetime
from _storage.download_into_memory import download_blob_into_memory
from _auth.get_project_id import get_project_id
from _auth.google_auth import google_auth


def parse_respose(row):
    res = {}
    res["url"] = row["external_urls"]["spotify"]
    res["name"] = row["name"]
    res["popularity"] = row["popularity"]
    res["followers"] = row["followers"]["total"]
    res["genres"] = row["genres"]
    res["image_url"] = row["images"][0]["url"]
    return res


def get_artists_in_global_top_50(_date: datetime) -> list:
    google_auth()
    project_id = get_project_id()
    res_from_server = download_blob_into_memory(
        project_id,
        f"spotify/artists_in_global_top_50/{_date.strftime('%Y-%m-%d')}.json",
    )
    res_json = json.loads(res_from_server)
    return [parse_respose(row) for row in res_json]


if __name__ == "__main__":
    print(get_artists_in_global_top_50(datetime.strptime(sys.argv[1], "%Y-%m-%d")))
