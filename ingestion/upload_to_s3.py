import boto3
from botocore.exceptions import ClientError
import sys

def upload(bucket_name, object_key, file_path, profile='default', overwrite=True):
    """
    Uploads a local file to an S3 bucket and returns the public file URL.

    Parameters:
    ----------
    bucket_name : str
        The name of the target S3 bucket.
    object_key : str
        The key (i.e., the path and filename) under which the file will be stored in the S3 bucket.
    file_path : str
        The full local file path to be uploaded.
    profile : str, optional
        The AWS CLI named profile to use for authentication. Defaults to 'default'.
    overwrite : bool, optional
        If False and the object_key already exists in the bucket, the upload will be aborted.
        If True (default), the existing object will be overwritten.
    Returns:
    -------
    str
        The public URL of the uploaded file in the S3 bucket.

    Notes:
    -----
    - The uploaded file is set to be publicly readable (ACL = 'public-read').
    - If the session region is not defined, it defaults to 'ap-southeast-1'.
    - AWS credentials (Access Key ID, Secret Access Key, and default region) are expected
      to be configured in the local machine under `~/.aws/credentials` and `~/.aws/config`
    """
    session = boto3.Session(profile_name=profile)
    s3 = session.client('s3')
    try:
        s3.head_object(Bucket=bucket_name, Key=object_key)
        if overwrite:
            print(f"File '{object_key}' already exists in '{bucket_name}'. It will be overwritten.")
        else:
            print(f"File '{object_key}' already exists in '{bucket_name}'. Exiting the script.")
            sys.exit()
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            print(f"✅ File '{object_key}' does not exist in '{bucket_name}'. Uploading now...")
        else:
            raise
    s3.upload_file(file_path, bucket_name, object_key, ExtraArgs={'ACL': 'public-read'})
    region = session.region_name or 'ap-southeast-1'
    file_url = f'https://{bucket_name}.s3.{region}.amazonaws.com/{object_key}'
    return file_url