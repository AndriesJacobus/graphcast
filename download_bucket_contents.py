import os

from google.cloud import storage


def download_bucket_contents(bucket_name, destination_directory):
    """Downloads all the files in the given bucket to the specified directory.

    If the files already exist in the destination directory, they will be
    skipped.

    Args:
        bucket_name: The name of the bucket to download from.
        destination_directory: The directory to download the files to.
    """

    gcs_client = storage.Client.create_anonymous_client()
    gcs_bucket = gcs_client.get_bucket(bucket_name)

    for blob in gcs_bucket.list_blobs():
        destination_file_name = os.path.join(destination_directory, blob.name)
        if not os.path.exists(destination_file_name):
            blob.download_to_filename(destination_file_name)

if __name__ == "__main__":
    # TODO(developer): Replace these variables before running the sample.
    bucket_name = "dm_graphcast"
    destination_directory = "dataset"

    download_bucket_contents(bucket_name, destination_directory)
