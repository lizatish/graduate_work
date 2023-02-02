import uuid

from fastapi import APIRouter, Depends
from services.promocode import get_promocode_service, PromocodeService
from core.middleware import AuthRequired
from core.config import get_settings

router = APIRouter()
conf = get_settings()


@router.post('/apply', summary='Применить промокод')
async def apply_promocode(
        promocode_service: PromocodeService = Depends(get_promocode_service),
        user_id: uuid.UUID = Depends(AuthRequired(conf.AUTH_LOGIN_REQUIRED))
):
    pass


@router.post('/confirm', summary='Подтвердить промокод')
async def confirm_promocode(
        promocode_service: PromocodeService = Depends(get_promocode_service),
        user_id: uuid.UUID = Depends(AuthRequired(conf.AUTH_LOGIN_REQUIRED))
):
    pass


@router.post('/revoke', summary='Отозвать промокод')
async def revoke_promocode(
        promocode_service: PromocodeService = Depends(get_promocode_service),
        user_id: uuid.UUID = Depends(AuthRequired(conf.AUTH_LOGIN_REQUIRED))
):
    pass
