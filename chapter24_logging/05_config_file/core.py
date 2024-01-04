import logging

logger = logging.getLogger("main.core")


def run():
    logger.info("Core Info")
    logger.debug("Core Debug")
    logger.error("Core Error")
