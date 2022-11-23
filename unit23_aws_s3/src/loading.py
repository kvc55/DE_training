import os
from pathlib import Path

import boto3
from botocore.exceptions import ClientError, DataNotFoundError

from unit23_aws_s3.configs.logging_setup import logger_l
from unit23_aws_s3.configs.settings import (BUCKET_REGION,
                                            KEY_ID,
                                            ACCESS_KEY,
                                            bucket_name)

path = Path(__file__).resolve().parent.parent


def upload_file(file_name: str, object_name=None) -> bool:
    """Takes a .xlsx file and loads it to S3 bucket

    :param file_name: Path to .xlsx file
    :type file_name: str
    :param object_name: S3 object name, defaults to None
    :type object_name: str
    :return: Returns True if file was uploaded, else False
    :rtype: bool
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Defines credentials
    s3_client = boto3.client(service_name='s3',
                             region_name=BUCKET_REGION,
                             aws_access_key_id=KEY_ID,
                             aws_secret_access_key=ACCESS_KEY
                             )

    try:
        # Uploads file if it doesn't exist or replace the old one
        s3_client.upload_file(file_name, bucket_name, object_name)
        logger_l.info('File loaded successfully')
    except ClientError:
        logger_l.error('Error when trying to download file')
        return False
    except DataNotFoundError:
        logger_l.error('No data was found')
        return False

    return True
