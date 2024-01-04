import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# FileHandler
file_handler = logging.FileHandler("result.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# StreamHandler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# Log
logger.info("Start")
logger.warning("Something maybe fail.")
try:
    result = 10 / 0
except Exception:
    logger.error("Faild to get result", exc_info=True)
logger.info("Finished")
