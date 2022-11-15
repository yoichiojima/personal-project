from _logging.logger import Logger

logger = Logger(log_file="./test.log")

logger.info("info")
logger.debug("debug")
logger.warning("warning")
logger.error("error")
