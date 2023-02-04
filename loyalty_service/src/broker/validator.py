import json
import logging
from typing import Optional

import pydantic
from aio_pika.abc import AbstractIncomingMessage

from models.broker_models import DiscountBroker

logger = logging.getLogger()


def get_payload(message: AbstractIncomingMessage) -> Optional[DiscountBroker]:
    """Проверка сообщения на валидность."""
    try:
        message_json = json.loads(message.body)
        discount = DiscountBroker(**message_json)
    except json.JSONDecodeError as exc:
        logger.error(
            'ERROR: Invalid JSON: %(message)s, line %(line)s, column %(column)s',
            {'message': exc.msg, 'line': exc.lineno, 'column': exc.colno}
        )
        return
    except pydantic.ValidationError as exc:
        logger.error(f"ERROR: Invalid schema: {exc}")
        logger.error(
            'ERROR: Invalid schema: %(message)s',
            {'message': exc}
        )
        return
    return discount
