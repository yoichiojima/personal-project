import os


def google_auth():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/opt/google_auth.json"


if __name__ == "__main__":
    google_auth()
