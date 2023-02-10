from models.db_models import DiscountStatus


discount_mapping = {
    'apply': {
        'current_status': DiscountStatus.not_processed,
        'required_status': DiscountStatus.in_process,
        'successful_message': 'Discount applied'
    },
    'confirm': {
        'current_status': DiscountStatus.in_process,
        'required_status': DiscountStatus.finished,
        'successful_message': 'Discount confirmed'
    },
    'revoke': {
        'current_status': DiscountStatus.in_process,
        'required_status': DiscountStatus.not_processed,
        'successful_message': 'Discount revoked'
    },
}
