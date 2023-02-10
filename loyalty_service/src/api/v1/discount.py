import logging
import uuid

from fastapi import APIRouter, Depends

from api.v1.schemas.general import Discount, BaseAction
from api.v1.utils import discount_mapping
from core.config import get_settings
from core.middleware import AuthRequired
from models.responses import StandardResponse
from services.discount import get_discount_service, DiscountService
from services.json import JsonService

router = APIRouter()
conf = get_settings()
logger = logging.getLogger('')


@router.get('/', summary='Список доступных скидок', response_model=list[Discount])
async def discounts_scope(
        discount_service: DiscountService = Depends(get_discount_service),
        user_id: uuid.UUID = Depends(AuthRequired(conf.AUTH_LOGIN_REQUIRED))
):
    """
    Возвращает список доступных пользователю скидок со следующим содержимым:
    - **id**: идентификатор
    - **created_at**: дата создания скидки
    - **expired_at**: дата окончания скидки
    - **percent**: процент скидки
    - **group_product_id**: группа товаров, на которые действует скидка
    - **discount_type**: тип скидки
    """
    logger.info('User-"%(user_id)s" try to get all discounts.', {'user_id': user_id})
    discounts = await discount_service.get_discounts(user_id)
    if not discounts:
        logger.info('No discounts found for user-"%(user_id)s".', {'user_id': user_id})
        return JsonService.return_not_found('Discounts not found')
    logger.info('Successfully found discounts for the user-"%(user_id)s".', {'user_id': user_id})
    return prepare_output(Discount, discounts)


@router.post('/{action}/{discount_id}', summary='Изменить статус персональной скидки', response_model=StandardResponse)
async def change_discount_status(
        action: BaseAction,
        discount_id: uuid.UUID,
        discount_service: DiscountService = Depends(get_discount_service),
        user_id: uuid.UUID = Depends(AuthRequired(conf.AUTH_LOGIN_REQUIRED))
):
    """
    Изменяет статус персональной скидки в зависимости от переданного действия
    Доступные действия:
    - **apply**: применить скидку
    - **confirm**: подтвердить применение скидки
    - **revoke**: отменить применение скидки
    """
    logger.info(
        'User-"%(user_id)s" try to "%(action)s" personal discount-"%(discount_id)s".',
        {'user_id': user_id, 'action': action.value, 'discount_id': discount_id}
    )
    discount = await discount_service.get_personal_discount(user_id, discount_id)
    if not discount:
        logger.info(
            'Failed to "%(action)s" discount-"%(discount_id)s" by user-"%(user_id)s" (Discount not found).',
            {'user_id': user_id, 'action': action.value, 'discount_id': discount_id}
        )
        return JsonService.return_not_found('Discount not found')
    if discount.discount_status != discount_mapping[action.value]['current_status']:
        logger.info(
            'Failed to "%(action)s" discount-"%(discount_id)s" by user-"%(user_id)s" (Wrong type of discount).',
            {'user_id': user_id, 'action': action.value, 'discount_id': discount_id}
        )
        return JsonService.return_bad_request('Wrong type of discount')
    await discount_service.change_personal_discount_status(
        discount, discount_mapping[action.value]['required_status']
    )
    logger.info(
        'Successfully "%(action)s" discount-"%(discount_id)s" by user-"%(user_id)s".',
        {'user_id': user_id, 'action': action.value, 'discount_id': discount_id}
    )
    return JsonService.return_success_response(discount_mapping[action.value]['successful_message'])
