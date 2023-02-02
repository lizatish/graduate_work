import uuid
from datetime import datetime

from pydantic import BaseModel
from models.db_models import DiscountType


class Discount(BaseModel):
    id: uuid.UUID
    created_at: datetime
    expired_at: datetime
    percent: float
    group_product_id: uuid.UUID
    discount_type: DiscountType
