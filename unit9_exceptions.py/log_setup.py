import logging

# Logging setup
logger = logging.getLogger('main')
level = logging.getLevelName('INFO')
logger.setLevel(level)

# Format
format = logging.Formatter('%(message)s')

# Handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(format)
logger.addHandler(stream_handler)