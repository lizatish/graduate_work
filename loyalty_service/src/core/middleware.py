from http import HTTPStatus

import requests
from fastapi import Request

from core.config import get_settings
from models.auth import AuthUserData, RoleType
from services.json import JsonService

conf = get_settings()


class AuthRequired:
    """Класс для проверки ролей и доступов."""

    def __init__(self, roles: list[str]):
        """Инициализация требования ролей."""
        self.roles = roles

    def __call__(self, request: Request):
        """Проверка токена доступа и роли пользователя"""
        try:
            token = request.headers['Authorization']
            response = requests.get(
                f'http://{conf.AUTH_SERVICE_HOST}:{conf.AUTH_SERVICE_PORT}/auth/v1/users/protected',
                headers={"Authorization": token}
            )
            response_body = response.json()
            if response.status_code == HTTPStatus.OK:
                auth_user_data = AuthUserData.parse_obj(response_body)
            else:
                raise Exception
        except Exception:
            auth_user_data = AuthUserData(user_id=None, role=RoleType.ANONYMOUS)

        if auth_user_data.role not in self.roles:
            return JsonService.return_authorization_failed()
        return auth_user_data.user_id
