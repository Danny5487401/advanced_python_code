import logging

logging.basicConfig(
    # 运行时间、模块名称、日志级别、日志内容
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

logger.info("This is a log info")
logger.debug("Debugging")
logger.warning("Warning exists")
logger.info("Finish")
