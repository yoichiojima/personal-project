import sys
from google.cloud import storage


def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()

    print(f"Blob {blob_name} deleted.")


if __name__ == "__main__":
    delete_blob(bucket_name=sys.argv[1], blob_name=sys.argv[2])
