import uuid
import enum

import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class BaseStatus(enum.Enum):
    in_process = "in_process"
    finished = "finished"


class PromocodeStatus(BaseStatus):
    pass


class DiscountStatus(BaseStatus):
    not_processed = "not_processed"


class PromocodeType(enum.Enum):
    all_users = "all_users"
    personal = "personal"


class DiscountType(enum.Enum):
    all_users = "all_users"
    registration = "registration"
    birthday = "birthday"


class UUIDMixin:
    id = sqlalchemy.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class TimeStampedMixin:
    created_at = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())
    expired_at = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True))


class BasePromocode(Base, UUIDMixin, TimeStampedMixin):
    __tablename__ = "BasePromocode"
    label = sqlalchemy.Column(sqlalchemy.String(100), unique=True)
    is_disposable = sqlalchemy.Column(sqlalchemy.Boolean())
    percent = sqlalchemy.Column(sqlalchemy.Float())
    promocode_type = sqlalchemy.Column(sqlalchemy.Enum(PromocodeType))


class PersonalPromocode(Base, UUIDMixin):
    __tablename__ = "PersonalPromocode"
    promocode = sqlalchemy.Column(sqlalchemy.ForeignKey("BasePromocode.id"))
    user_id = sqlalchemy.Column(UUID(as_uuid=True))


class PromocodeHistory(Base, UUIDMixin):
    __tablename__ = "PromocodeHistory"
    promocode = sqlalchemy.Column(sqlalchemy.ForeignKey("BasePromocode.id"))
    created_at = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())
    user_id = sqlalchemy.Column(UUID(as_uuid=True))
    promocode_status = sqlalchemy.Column(sqlalchemy.Enum(PromocodeStatus))


class BaseDiscount(Base, UUIDMixin, TimeStampedMixin):
    __tablename__ = "BaseDiscount"
    percent = sqlalchemy.Column(sqlalchemy.Float())
    group_product_id = sqlalchemy.Column(UUID(as_uuid=True))
    discount_type = sqlalchemy.Column(sqlalchemy.Enum(DiscountType))


class PersonalDiscount(Base, UUIDMixin):
    __tablename__ = "PersonalDiscount"
    discount = sqlalchemy.Column(sqlalchemy.ForeignKey("BaseDiscount.id"))
    user_id = sqlalchemy.Column(UUID(as_uuid=True))
    discount_status = sqlalchemy.Column(sqlalchemy.Enum(DiscountStatus))
