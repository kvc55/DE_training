from decouple import config

# Configuration to access database
DB_USERNAME = config('DB_USERNAME')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
DB_NAME = config('DB_NAME')

DB_URL = (f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}'
          f'@{DB_HOST}:{DB_PORT}/{DB_NAME}')
