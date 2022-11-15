import logging
import google.cloud.logging
from _auth.google_auth import google_auth

google_auth()


class Logger:
    logger = logging.getLogger(__name__)
    gcloud_logging = google.cloud.logging.Client()

    def __init__(self, level=logging.INFO, log_file=None):
        self.logger.setLevel(level)
        self.gcloud_logging.setup_logging()

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
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
