import boto3
from botocore.exceptions import ClientError

from unit23_aws_s3.configs.logging_setup import logger_e
from unit23_aws_s3.configs.settings import (BUCKET_REGION,
                                            KEY_ID,
                                            ACCESS_KEY,
                                            bucket_name)


def download_file(file_path: str) -> bool:
    """Downloads the .xlsx file from s3 bucket.

    :param file_path: Path to save the .xlsx file from bucket
    :type file_path: str
    :return: Returns True if file was downloaded, else False
    :rtype: bool
    """

    # Defines credentials
    s3_client = boto3.client(service_name='s3',
                             region_name=BUCKET_REGION,
                             aws_access_key_id=KEY_ID,
                             aws_secret_access_key=ACCESS_KEY
                             )

    try:
        # Downloads file from bucket
        s3_client.download_file(bucket_name, 'medals.xlsx', file_path)
        logger_e.info('File downloaded successfully')
    except ClientError:
        logger_e.error('Error when trying to download file')
        return False

    return True
