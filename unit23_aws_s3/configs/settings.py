from decouple import config

# Configuration to access S3 bucket on AWS
BUCKET_REGION = config('BUCKET_REGION')
KEY_ID = config('KEY_ID')
ACCESS_KEY = config('ACCESS_KEY')
bucket_name = config('bucket_name')
