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

    @staticmethod
    def return_not_found(message: str) -> dict:
        """Возвращает ответ пользователю, сообщающий об отсутствии элементов"""
        raise HTTPException(HTTPStatus.NOT_FOUND, detail=message)

    @staticmethod
    def prepare_output(model, items):
        """Возвращает данные в json формате приведенные к нужной модели."""
        return [model(**item.__dict__) for item in items]

    @staticmethod
    def return_bad_request(message: str) -> dict:
        """Возвращает ответ пользователю, сообщающий об отсутствии элементов"""
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail=message)
