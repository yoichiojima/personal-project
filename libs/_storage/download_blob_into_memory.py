import sys
from google.cloud import storage


def download_blob_into_memory(bucket_name, blob_name):
    """Downloads a blob into memory."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(blob_name)
    contents = blob.download_as_string()

    return contents


if __name__ == "__main__":
    download_blob_into_memory(
        bucket_name=sys.argv[1],
        blob_name=sys.argv[2],
    )
