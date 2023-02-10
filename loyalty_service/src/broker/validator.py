import json
import logging

import pydantic
from aio_pika.abc import AbstractIncomingMessage

from models.broker_models import DiscountBroker

logger = logging.getLogger()


def get_payload(message: AbstractIncomingMessage) -> DiscountBroker | None:
    """Проверка сообщения на валидность."""
    try:
        message_json = json.loads(message.body)
        discount = DiscountBroker(**message_json)
    except json.JSONDecodeError as exc:
        logger.error(
            'ERROR: Invalid JSON: %(message)s, line %(line)s, column %(column)s',
            {'message': exc.msg, 'line': exc.lineno, 'column': exc.colno}
        )
        return None
    except pydantic.ValidationError as exc:
        logger.error(
            'ERROR: Invalid schema: %(message)s',
            {'message': exc}
        )
        return None
    return discount
