import enum
import uuid
from datetime import datetime

from pydantic import BaseModel

from models.common import LoyaltyStatus, DiscountType


class Discount(BaseModel):
    """Схема скидки."""

    id: uuid.UUID
    created_at: datetime
    expired_at: datetime
    percent: float
    group_product_id: uuid.UUID
    discount_type: DiscountType


class BaseAction(enum.Enum):
    """Lоступные действия над скидкой или промокодом."""
    confirm = 'confirm'
    revoke = 'revoke'
    apply = 'apply'


class ChangePromocodeStatusResponse(BaseModel):
    label: str
    action: BaseAction


class PromocodeSuccessResponse(BaseModel):
    """Ответ после удачного изменения статуса промокода."""
    discount_value: float
    new_status: LoyaltyStatus
    label: str


class PromocodeHistoryResponce(BaseModel):
    promocode: str
    created_at: str
    user_id: uuid.UUID
    promocode_status: LoyaltyStatus


discount_mapping = {
    'apply': {
        'current_status': LoyaltyStatus.not_processed,
        'required_status': LoyaltyStatus.in_process,
        'successful_message': 'Discount applied',
        'unsuccessful_message': 'The discount has already been used or is no longer available!'
    },
    'confirm': {
        'current_status': LoyaltyStatus.in_process,
        'required_status': LoyaltyStatus.finished,
        'successful_message': 'Discount confirmed',
        'unsuccessful_message': 'Discount not found'
    },
    'revoke': {
        'current_status': LoyaltyStatus.in_process,
        'required_status': LoyaltyStatus.not_processed,
        'successful_message': 'Discount revoked',
        'unsuccessful_message': 'Discount not found'
    },
}
