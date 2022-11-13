import sys

from google.cloud import storage


def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)
    return [blob.name for blob in blobs]


if __name__ == "__main__":
    list_blobs(bucket_name=sys.argv[1])