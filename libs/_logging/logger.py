import logging


class Logger:
    logger = logging.getLogger(__name__)

    def __init__(self, level=logging.INFO, log_file=None):
        self.logger.setLevel(level)

        if log_file is not None:
            file_handler = logging.FileHandler(log_file)
            fh_formatter = logging.Formatter(
                "%(asctime)s %(name)s[%(process)s] %(levelname)s: %(message)s"
            )
            file_handler.setFormatter(fh_formatter)
            self.logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        sh_formatter = logging.Formatter("%(levelname)s: %(message)s")
        stream_handler.setFormatter(sh_formatter)
        self.logger.addHandler(stream_handler)

    def info(self, msg):
        return self.logger.info(msg)

    def debug(self, msg):
        return self.logger.debug(msg)

    def warning(self, msg):
        return self.logger.warning(msg)

    def error(self, msg):
        return self.logger.error(msg)

    def critical(self, msg):
        return self.logger.critical(msg)
