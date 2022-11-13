import json


def get_project_id():
    with open("/opt/google_auth.json") as f:
        data = json.load(f)
        return data["project_id"]
