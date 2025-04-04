import logging
import uuid

from fastapi import APIRouter, Depends

from api.v1.schemas.general import ChangePromocodeStatusRequest, PromocodeSuccessResponse, PromocodeHistoryResponce
from core.config import get_settings
from core.middleware import AuthRequired
from services.json import JsonService
from services.promocode import PromocodeService, get_promocode_service

router = APIRouter()
conf = get_settings()
logger = logging.getLogger(__name__)


@router.post('/status', summary='Изменить статус промокода', response_model=PromocodeSuccessResponse)
async def change_promocode_status(
        promocode_response: ChangePromocodeStatusRequest,
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
    return PromocodeSuccessResponse(
        label=promocode.label,
        discount_value=promocode.percent,
        new_status=new_status,
    )


@router.get(
    '/history',
    summary='Получить историю применения промокодов для пользователя',
    response_model=list[PromocodeHistoryResponce],
)
async def get_promocode_history(
        promocode_service: PromocodeService = Depends(get_promocode_service),
        user_id: uuid.UUID = Depends(AuthRequired(conf.AUTH_LOGIN_REQUIRED))
):
    """Возвращает историю применения промокодов для пользователя"""
    history, promocodes = await promocode_service.get_promocodes_history(user_id)
    return JsonService.prepare_history_output(history, promocodes)
