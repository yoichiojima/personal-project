import os

def get_authenticated():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/opt/google_auth.json'