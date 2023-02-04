import enum
import uuid

from pydantic import BaseModel


class DiscountTypeBroker(enum.Enum):
    """Типы скидок, принимаемые брокером."""
    registration = 'registration'
    birthday = 'birthday'


class DiscountBroker(BaseModel):
    """Модель передачи данных на email-рассылку."""
    user_id: uuid.UUID
    discount_type: DiscountTypeBroker
