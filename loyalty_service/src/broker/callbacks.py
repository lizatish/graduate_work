import logging

from aio_pika.abc import AbstractIncomingMessage

from core.config import get_settings
from services.discount import DiscountService
from db.db_factory import get_session
from broker.validator import get_payload

conf = get_settings()

logger = logging.getLogger('')


async def callback_discounts(
        message: AbstractIncomingMessage
):
    logger.info('callback_discounts message:"%(message)s"', {'message': message.body})
    discount = get_payload(message)
    discount_service = DiscountService(await get_session())
    is_created = await discount_service.create_personal_discounts(discount.user_id, discount.discount_type)
    if is_created:
        logger.info(
            'Successfully created "%(type)s" discounts for user-"%(user_id)s".',
            {'user_id': discount.user_id, 'type': discount.discount_type.value}
        )
    else:
        logger.info(
            'Failed to create "%(type)s" discounts for user-"%(user_id)s" (already exists).',
            {'user_id': discount.user_id, 'type': discount.discount_type.value}
        )
