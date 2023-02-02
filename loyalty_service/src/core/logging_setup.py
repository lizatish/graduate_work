import logging

from core.config import get_settings

conf = get_settings()

LOG_FORMAT = '{"request_id": "%(request_id)s", "asctime": \
             "%(asctime)s", "levelname": "%(levelname)s", \
             "name": "%(name)s", "message": "%(message)s"}'


def setup_root_logger():
    logger = logging.getLogger('')
    if (logger.hasHandlers()):
        logger.handlers.clear()
    formatter = logging.Formatter(LOG_FORMAT)
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    file = logging.handlers.RotatingFileHandler(
        filename=conf.LOGGER_FILENAME, mode=conf.LOGGER_MOD,
        maxBytes=conf.LOGGER_MAXBYTES, backupCount=conf.LOGGER_BACKUP_COUNT
    )
    file.setFormatter(formatter)
    logger.addHandler(console)
    logger.addHandler(file)
    logger.setLevel(logging.INFO)
