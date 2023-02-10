import enum


class LoyaltyStatus(enum.Enum):
    """Статусы скидок."""

    in_process = "in_process"
    finished = "finished"
    not_processed = "not_processed"


class PromocodeType(enum.Enum):
    """Типы применения промокодов."""

    all_users = "all_users"
    personal = "personal"


class DiscountType(enum.Enum):
    """Типы применения скидок."""

    all_users = "all_users"
    registration = "registration"
    birthday = "birthday"
