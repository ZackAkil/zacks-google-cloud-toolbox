# pip install google-cloud-storage

import tempfile
from google.cloud import storage

def upload_to_gcs(local_filename:str, gs_location:str) -> None:
    """Uploads a file to a Google Storage bucket.
    """
    bucket_name, blob_name = gs_location.replace('gs://', '').split('/', 1)
    
    print(f'⬆️ Uploadting {local_filename} to bucket 🪣:{bucket_name}, blob {blob_name} ...')

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(local_filename)
    print(f'✅ Uploaded {local_filename} to bucket:{bucket_name}, blob {blob_name}')


def download_from_gcs(gs_location:str) -> str:
    """Loads a file from Google Storage.
    """
    print(f'⬇️ Downloading file :{gs_location}...')
    
    bucket_name, blob_name = gs_location.replace('gs://', '').split('/', 1)

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    with tempfile.NamedTemporaryFile(delete=False) as temp:
        blob.download_to_file(temp)
    print(f'✅ Downloaded file :{gs_location}')
    return temp.name
