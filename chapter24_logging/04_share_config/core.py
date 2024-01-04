import logging

# 注意这里开头是 main，在 main.py 里面的 Logger 的名称，这样 core.py 里面的 Logger 就会复用 main.py 里面的 Logger 配置
logger = logging.getLogger("main.core")


def run():
    logger.info("Core Info")
    logger.debug("Core Debug")
    logger.error("Core Error")
