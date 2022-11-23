import logging

# Logging setup
logger_e = logging.getLogger('src.extraction')
logger_p = logging.getLogger('src.processing')
logger_l = logging.getLogger('src.loading')

level = logging.getLevelName('INFO')

logger_e.setLevel(level)
logger_p.setLevel(level)
logger_l.setLevel(level)

# Format
format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(levelno)s - %(message)s')

# Handler 1 - Stream Handler (INFO)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(format)

logger_e.addHandler(stream_handler)
logger_p.addHandler(stream_handler)
logger_l.addHandler(stream_handler)

# Handler 2 - File Handler (INFO)
file_handler = logging.FileHandler(
    'airflow/dags/unit23_aws_s3/logs/general.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(format)

logger_e.addHandler(file_handler)
logger_p.addHandler(file_handler)
logger_l.addHandler(file_handler)
