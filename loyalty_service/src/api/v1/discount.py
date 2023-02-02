import uuid
import logging

from fastapi import APIRouter, Depends
from services.discount import get_discount_service, DiscountService
from core.middleware import AuthRequired
from core.config import get_settings


router = APIRouter()
conf = get_settings()
logger = logging.getLogger('')


@router.get('/', summary='Список доступных скидок')
async def discounts_scope(
        discount_service: DiscountService = Depends(get_discount_service),
        user_id: uuid.UUID = Depends(AuthRequired(conf.AUTH_LOGIN_REQUIRED))
):
    pass


@router.post('/apply', summary='Применить скидку')
async def apply_discount(
        discount_service: DiscountService = Depends(get_discount_service),
        user_id: uuid.UUID = Depends(AuthRequired(conf.AUTH_LOGIN_REQUIRED))
):
    pass


@router.post('/confirm', summary='Подтвердить скидку')
async def confirm_discount(
        discount_service: DiscountService = Depends(get_discount_service),
        user_id: uuid.UUID = Depends(AuthRequired(conf.AUTH_LOGIN_REQUIRED))
):
    pass


@router.post('/revoke', summary='Отозвать скидку')
async def revoke_discount(
        discount_service: DiscountService = Depends(get_discount_service),
        user_id: uuid.UUID = Depends(AuthRequired(conf.AUTH_LOGIN_REQUIRED))
):
    pass


@router.post('/test', summary='test')
async def test(
        discount_service: DiscountService = Depends(get_discount_service),
        user_id: uuid.UUID = Depends(AuthRequired(conf.AUTH_LOGIN_REQUIRED))
):
    test = await discount_service.test()
    if test:
        logger.info(
            "test discount - %(discount_id)d was created by user %(user_id)d",
            {"discount_id": test.id, "user_id": user_id}
        )
        return f'success-{user_id}'
    logger.info(
        "test discount fail created by user %(user_id)d",
        {"user_id": user_id}
    )
    return f'fail-{user_id}'
