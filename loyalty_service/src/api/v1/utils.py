import enum

from models.db_models import DiscountStatus


class DiscountAction(enum.Enum):
    """Доступные действия над скидкой."""

    apply = 'apply'
    confirm = 'confirm'
    revoke = 'revoke'


discount_mapping = {
    'apply': {
        'current_status': DiscountStatus.not_processed,
        'required_status': DiscountStatus.in_process,
        'successful_message': 'Discount applied',
        'unsuccessful_message': 'The discount has already been used or is no longer available!'
    },
    'confirm': {
        'current_status': DiscountStatus.in_process,
        'required_status': DiscountStatus.finished,
        'successful_message': 'Discount confirmed',
        'unsuccessful_message': 'Discount not found'
    },
    'revoke': {
        'current_status': DiscountStatus.in_process,
        'required_status': DiscountStatus.not_processed,
        'successful_message': 'Discount revoked',
        'unsuccessful_message': 'Discount not found'
    },
}
