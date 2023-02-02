import enum
import uuid

from pydantic import BaseModel

from core.config import get_settings

conf = get_settings()


class RoleType(str, enum.Enum):
    """Тип роли пользователя."""

    STANDARD = 'STANDARD'
    PRIVILEGED = 'PRIVILEGED'
    ADMIN = 'ADMIN'
    ANONYMOUS = 'ANONYMOUS'


class AuthUserData(BaseModel):
    """Данные о пользователе, полученные из сервиса авторизации."""

    role: RoleType
    user_id: uuid.UUID | None

    class Config:
        """Дополнительные настройки"""
        use_enum_values = True  # использовать по умолчанию значение вложенного enum
