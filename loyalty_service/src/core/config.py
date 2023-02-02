import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Настройки приложения."""

    AUTH_SERVICE_HOST: str = 'dockervm.promo-miner.art'
    AUTH_SERVICE_PORT = ''
    AUTH_LOGIN_REQUIRED: list[str] = ['STANDARD', 'ADMIN', 'PRIVILEGED']

    PROJECT_NAME: str = 'graduate_work'

    DATABASE_URL_ASYNC: str
    DATABASE_URL: str

    APP_HOST: str = '0.0.0.0'
    APP_PORT: int = 6666

    LOGGER_FILENAME: str = "./logs/fastapi-elk-stack.json"
    LOGGER_MAXBYTES: int = 15000000
    LOGGER_MOD: str = 'a'
    LOGGER_BACKUP_COUNT: int = 5

    BROKER_URL: str = 'amqp://127.0.0.1:5672'

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    class Config:
        """Дополнительные базовые настройки."""

        env_file = '../../.env'
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings():
    """Возвращает настройки тестов."""
    return Settings()
