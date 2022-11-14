import logging

# Logging setup
logger = logging.getLogger('main')
level = logging.getLevelName('INFO')
logger.setLevel(level)

# Format
format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(levelno)s - %(message)s')

# Handler 1 - Stream Handler (INFO)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(format)
logger.addHandler(stream_handler)

# Handler 2 - File Handler (INFO)
file_handler = logging.FileHandler(
    '/home/karencaro/airflow/dags/unit5_logging_airflow/logs/custom_log.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(format)
logger.addHandler(file_handler)
