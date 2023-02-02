import uuid
import logging

from fastapi import APIRouter, Depends
from services.discount import get_discount_service, DiscountService
from core.middleware import AuthRequired
from core.config import get_settings
from services.json import JsonService
from api.v1.schemas.general import Discount
from models.db_models import DiscountStatus


router = APIRouter()
conf = get_settings()
logger = logging.getLogger('')


@router.get('/', summary='Список доступных скидок')
async def discounts_scope(
        discount_service: DiscountService = Depends(get_discount_service),
        user_id: uuid.UUID = Depends(AuthRequired(conf.AUTH_LOGIN_REQUIRED))
):
    discounts = await discount_service.get_discounts(user_id)
    if not discounts:
        return JsonService.return_not_found('Discounts not found')
    return JsonService.prepare_output(Discount, discounts)


@router.post('/apply-personal-discount/{discount_id}', summary='Применить персональную скидку')
async def apply_personal_discount(
        discount_id: uuid.UUID,
        discount_service: DiscountService = Depends(get_discount_service),
        user_id: uuid.UUID = Depends(AuthRequired(conf.AUTH_LOGIN_REQUIRED))
):
    applied = await discount_service.change_personal_discount_status(
        user_id, discount_id, DiscountStatus.not_processed, DiscountStatus.in_process
    )
    if applied:
        return JsonService.return_success_response('Discount applied')
    return JsonService.return_not_found('The discount has already been used or is no longer available!')


@router.post('/confirm-personal-discount/{discount_id}', summary='Подтвердить персональную скидку')
async def confirm_discount(
        discount_id: uuid.UUID,
        discount_service: DiscountService = Depends(get_discount_service),
        user_id: uuid.UUID = Depends(AuthRequired(conf.AUTH_LOGIN_REQUIRED))
):
    confirmed = await discount_service.change_personal_discount_status(
        user_id, discount_id, DiscountStatus.in_process, DiscountStatus.finished
    )
    if confirmed:
        return JsonService.return_success_response('Discount confirmed')
    return JsonService.return_not_found('Discount not found')


@router.post('/revoke-personal-discount/{discount_id}', summary='Отозвать персональную скидку')
async def revoke_discount(
        discount_id: uuid.UUID,
        discount_service: DiscountService = Depends(get_discount_service),
        user_id: uuid.UUID = Depends(AuthRequired(conf.AUTH_LOGIN_REQUIRED))
):
    revoked = await discount_service.change_personal_discount_status(
        user_id, discount_id, DiscountStatus.in_process, DiscountStatus.not_processed
    )
    if revoked:
        return JsonService.return_success_response('Discount revoked')
    return JsonService.return_not_found('Discount not found')
