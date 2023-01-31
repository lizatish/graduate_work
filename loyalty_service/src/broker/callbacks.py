import logging

from aio_pika.abc import AbstractIncomingMessage

from core.config import get_settings
from services.discount import DiscountService
from db.db_factory import get_session

conf = get_settings()

logger = logging.getLogger('')


async def callback_registration(
        message: AbstractIncomingMessage
):
    logger.info(f"callback_registration message:{message.body}")
    discount_service = DiscountService(await get_session())
    test = await discount_service.test()
    if test:
        logger.info("test discount success")
    else:
        logger.info("test discount fail")


async def callback_birthday(message: AbstractIncomingMessage):
    logger.info(f"callback_birthday message:{message.body}")
