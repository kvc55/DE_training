import logging

# Logging setup
logger = logging.getLogger('comentarios')
level = logging.getLevelName('INFO')
logger.setLevel(level)

# Format
format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(format)
logger.addHandler(stream_handler)
