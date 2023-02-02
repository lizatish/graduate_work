from http import HTTPStatus
from fastapi import HTTPException
from models.responses import StandardResponse


class JsonService:
    @staticmethod
    def return_success_response(message: str) -> StandardResponse:
        """Возвращает ответ пользователю, сообщающий о выполнении успешной операции."""
        return StandardResponse(detail=message)

    @staticmethod
    def return_authorization_failed() -> dict:
        """Возвращает ответ пользователю, сообщающий об ошибке авторизации."""
        raise HTTPException(HTTPStatus.UNAUTHORIZED, detail='You don\'t have permissions for this action')
