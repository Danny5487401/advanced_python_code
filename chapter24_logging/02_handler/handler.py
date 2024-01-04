import logging
from logging.handlers import HTTPHandler
import sys

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

# StreamHandler
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(level=logging.DEBUG)
logger.addHandler(stream_handler)

# FileHandler
file_handler = logging.FileHandler("output.log")
file_handler.setLevel(level=logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# HTTPHandler
# http_handler = HTTPHandler(host="localhost:8001", url="log", method="POST")
# logger.addHandler(http_handler)

# Log
logger.info("This is a log info")
logger.debug("Debugging")
logger.warning("Warning exists")
logger.info("Finish")
