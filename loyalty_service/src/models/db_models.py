import uuid
import enum

import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.sql import func

Base: DeclarativeMeta = declarative_base()


class PromocodeStatus(enum.Enum):
    in_process = "in_process"
    finished = "finished"


class DiscountStatus(enum.Enum):
    in_process = "in_process"
    finished = "finished"
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
    created_at = sqlalchemy.Column(sqlalchemy.DateTime(), server_default=func.now())
    expired_at = sqlalchemy.Column(sqlalchemy.DateTime())


class BasePromocode(Base, UUIDMixin, TimeStampedMixin):
    __tablename__ = "base_promocode"
    label = sqlalchemy.Column(sqlalchemy.String(100), unique=True)
    is_disposable = sqlalchemy.Column(sqlalchemy.Boolean())
    percent = sqlalchemy.Column(sqlalchemy.Float())
    promocode_type = sqlalchemy.Column(sqlalchemy.Enum(PromocodeType))


class PersonalPromocode(Base, UUIDMixin):
    __tablename__ = "personal_promocode"
    promocode_id = sqlalchemy.Column(sqlalchemy.ForeignKey("base_promocode.id"))
    user_id = sqlalchemy.Column(UUID(as_uuid=True))


class PromocodeHistory(Base, UUIDMixin):
    __tablename__ = "promocode_history"
    promocode_id = sqlalchemy.Column(sqlalchemy.ForeignKey("base_promocode.id"))
    created_at = sqlalchemy.Column(sqlalchemy.DateTime(), server_default=func.now())
    user_id = sqlalchemy.Column(UUID(as_uuid=True))
    promocode_status = sqlalchemy.Column(sqlalchemy.Enum(PromocodeStatus))


class BaseDiscount(Base, UUIDMixin, TimeStampedMixin):
    __tablename__ = "base_discount"
    percent = sqlalchemy.Column(sqlalchemy.Float())
    group_product_id = sqlalchemy.Column(UUID(as_uuid=True))
    discount_type = sqlalchemy.Column(sqlalchemy.Enum(DiscountType))


class PersonalDiscount(Base, UUIDMixin):
    __tablename__ = "personal_discount"
    discount_id = sqlalchemy.Column(sqlalchemy.ForeignKey("base_discount.id"))
    user_id = sqlalchemy.Column(UUID(as_uuid=True))
    discount_status = sqlalchemy.Column(sqlalchemy.Enum(DiscountStatus))

    __table_args__ = (sqlalchemy.UniqueConstraint('discount', 'user_id', name='discount_user'),)
