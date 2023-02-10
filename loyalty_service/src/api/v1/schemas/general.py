import uuid
import enum
from datetime import datetime

from pydantic import BaseModel
from models.db_models import DiscountType


class Discount(BaseModel):
    """Схема скидки."""

    id: uuid.UUID
    created_at: datetime
    expired_at: datetime
    percent: float
    group_product_id: uuid.UUID
    discount_type: DiscountType


class DiscountAction(enum.Enum):
    """Доступные действия над скидкой."""

    apply = 'apply'
    confirm = 'confirm'
    revoke = 'revoke'
