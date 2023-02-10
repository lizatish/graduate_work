import enum
import uuid

from pydantic import BaseModel


class DiscountTypeBroker(enum.Enum):
    """Типы скидок, принимаемые брокером."""
    registration = 'registration'
    birthday = 'birthday'


class DiscountBroker(BaseModel):
    """Модель передачи данных на создание персональных скидок через брокер."""
    user_id: uuid.UUID
    discount_type: DiscountTypeBroker
