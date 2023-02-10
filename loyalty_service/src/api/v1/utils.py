from models.db_models import LoyaltyStatus

discount_mapping = {
    'apply': {
        'current_status': LoyaltyStatus.not_processed,
        'required_status': LoyaltyStatus.in_process,
        'successful_message': 'Discount applied'
    },
    'confirm': {
        'current_status': LoyaltyStatus.in_process,
        'required_status': LoyaltyStatus.finished,
        'successful_message': 'Discount confirmed'
    },
    'revoke': {
        'current_status': LoyaltyStatus.in_process,
        'required_status': LoyaltyStatus.not_processed,
        'successful_message': 'Discount revoked'
    },
}
