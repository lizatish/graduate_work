import os
from functools import lru_cache

from pydantic import BaseSettings


class TestSettings(BaseSettings):
    """Базовые тестовые настройки."""

    AUTH_SERVICE_HOST: str = '0.0.0.0'
    AUTH_SERVICE_PORT: int = 4555
    AUTH_LOGIN_REQUIRED: list[str] = ['STANDARD', 'ADMIN', 'PRIVILEGED']

    PROJECT_NAME: str = 'graduate_work'

    DATABASE_URL: str = 'postgresql+psycopg2://user:password@localhost:5434/loyalty_postgres'
    DATABASE_URL_ASYNC: str = 'postgresql+asyncpg://user:password@localhost:5434/loyalty_postgres'

    APP_HOST: str = '0.0.0.0'
    APP_PORT: int = 6666

    LOGGER_FILENAME: str = "fastapi-elk-stack-logs.json"
    LOGGER_MAXBYTES: int = 15000000
    LOGGER_MOD: str = 'a'
    LOGGER_BACKUP_COUNT: int = 5

    BROKER_URL: str = 'amqp://localhost:5673'

    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    BASE_URL: str = 'http://localhost/'

    TESTING: bool = True

    class Config:
        """Дополнительные базовые настройки."""

        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings() -> TestSettings:
    """Возвращает настройки тестов."""
    return TestSettings()
