import logging
import uuid

from fastapi import APIRouter, Depends

from api.v1.schemas.general import ChangePromocodeStatusResponse
from core.config import get_settings
from core.middleware import AuthRequired
from models.db_models import PromocodeHistory
from models.responses import StandardResponse
from services.json import JsonService
from services.promocode import PromocodeService, get_promocode_service

router = APIRouter()
conf = get_settings()
logger = logging.getLogger(__name__)


@router.post('/status', summary='Изменить статус промокода', response_model=StandardResponse)
async def change_promocode_status(
        promocode_response: ChangePromocodeStatusResponse,
        promocode_service: PromocodeService = Depends(get_promocode_service),
        user_id: uuid.UUID = Depends(AuthRequired(conf.AUTH_LOGIN_REQUIRED))
):
    """
    Тут система после колбека биллинга либо отменяет промокод, либо полностью подтверждает

    Изменяет статус промокода в зависимости от переданного действия после его применения
    Доступные действия:
    - **confirm**: подтвердить применение промокода
    - **revoke**: отменить применение промокода
    """
    logger.info(
        'User-"%(user_id)s" try to "%(action)s" personal promocode-"%(label)s".',
        {'user_id': user_id, 'action': promocode_response.action.value, 'label': promocode_response.label}
    )

    promocode, is_personal = await promocode_service.get_promocode(user_id, promocode_response.label)
    if not promocode:
        JsonService.return_not_found("Promocode not found")

    is_expired = promocode_service.check_promocode_expired(promocode)
    if is_expired:
        return JsonService.promocode_expired()

    new_status = await promocode_service.check_status(user_id, promocode, promocode_response.action)
    if not new_status:
        return JsonService.promocode_in_invalid_status()

    await promocode_service.change_promocode_status(
        user_id,
        promocode,
        new_status,
        is_personal
    )
    return JsonService.return_success_response("Promocode status was changed")


@router.get(
    '/history',
    summary='Получить историю применения промокодов для пользователя',
    response_model=StandardResponse,
)
async def get_promocode_history(
        promocode_service: PromocodeService = Depends(get_promocode_service),
        user_id: uuid.UUID = Depends(AuthRequired(conf.AUTH_LOGIN_REQUIRED))
):
    """Возвращает историю применения промокодов для пользователя"""
    history = await promocode_service.get_promocodes_history(user_id)
    return JsonService.prepare_output(PromocodeHistory, history)

# todo добавить параметр цена - новая цена

# todo тестирование изменения цены после успешного и неуспешного применения промокода