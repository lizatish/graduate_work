from http import HTTPStatus

from fastapi import HTTPException

from api.v1.schemas.general import PromocodeHistoryResponce
from models.db_models import PromocodeHistory, BasePromocode
from models.responses import StandardResponse


class JsonService:
    @staticmethod
    def prepare_history_output(history: list[PromocodeHistory], promocodes: list[BasePromocode]) -> list[
        PromocodeHistoryResponce]:
        """Возвращает данные в json формате приведенные к нужной модели."""
        return [PromocodeHistoryResponce(
            promocode=promocode_elem.label,
            created_at=history_elem.created_at.isoformat(),
            user_id=history_elem.user_id,
            promocode_status=history_elem.promocode_status.value) for promocode_elem, history_elem in
            zip(promocodes, history)]

    @staticmethod
    def prepare_output(model, items):
        """Возвращает данные в json формате приведенные к нужной модели."""
        return [model(**item.__dict__) for item in items]

    @staticmethod
    def promocode_expired():
        """Возвращает ответ пользователю, сообщающий о том, что время действия промокода истекло."""
        raise HTTPException(HTTPStatus.GONE, detail='This promo code has expired')

    @staticmethod
    def promocode_in_invalid_status():
        """Возвращает ответ пользователю, сообщающий об ошибке авторизации."""
        raise HTTPException(HTTPStatus.BAD_REQUEST,
                            detail='This promocode can\'t be used because has invalid status')

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
    def return_bad_request(message: str) -> dict:
        """Возвращает ответ пользователю, сообщающий об отсутствии элементов"""
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail=message)
