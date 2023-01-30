import uuid

import sqlalchemy
from sqlalchemy import UUID
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import relationship
from sqlalchemy.orm.decl_api import DeclarativeMeta, declarative_base
from sqlalchemy.sql import expression
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime

from models.common import PromocodeType, DiscountType, LoyaltyStatus

Base: DeclarativeMeta = declarative_base()


class utcnow(expression.FunctionElement):
    type = DateTime()
    inherit_cache = True


@compiles(utcnow, 'postgresql')
def pg_utcnow(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


class UUIDMixin:
    """Миксин-класс для типа uuid идентификатора всех моделей."""

    id = sqlalchemy.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TimeStampedMixin:
    """Миксин-класс для добавления полей времени создания и протухания."""

    created_at = sqlalchemy.Column(sqlalchemy.DateTime(), server_default=utcnow())
    expired_at = sqlalchemy.Column(sqlalchemy.DateTime())


class BasePromocode(Base, UUIDMixin, TimeStampedMixin):
    """Модель описания всех промокодов."""

    __tablename__ = "base_promocode"
    label = sqlalchemy.Column(sqlalchemy.String(100), unique=True)
    is_disposable = sqlalchemy.Column(sqlalchemy.Boolean())
    percent = sqlalchemy.Column(sqlalchemy.Float())
    promocode_type = sqlalchemy.Column(sqlalchemy.Enum(PromocodeType))

    personal_promocodes = relationship("PersonalPromocode", lazy="joined")


class PersonalPromocode(Base, UUIDMixin):
    """Модель персональных промокодов."""

    __tablename__ = "personal_promocode"
    promocode_id = sqlalchemy.Column(sqlalchemy.ForeignKey("base_promocode.id"))
    user_id = sqlalchemy.Column(UUID(as_uuid=True))


class PromocodeHistory(Base, UUIDMixin):
    """Модель истории промокодов."""

    __tablename__ = "promocode_history"
    promocode_id = sqlalchemy.Column(sqlalchemy.ForeignKey("base_promocode.id"))
    created_at = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())
    user_id = sqlalchemy.Column(UUID(as_uuid=True))
    promocode_status = sqlalchemy.Column(sqlalchemy.Enum(LoyaltyStatus))


class BaseDiscount(Base, UUIDMixin, TimeStampedMixin):
    """Модель всех скидок."""

    __tablename__ = "base_discount"
    percent = sqlalchemy.Column(sqlalchemy.Float())
    group_product_id = sqlalchemy.Column(UUID(as_uuid=True))
    discount_type = sqlalchemy.Column(sqlalchemy.Enum(DiscountType))


class PersonalDiscount(Base, UUIDMixin):
    """Модель персональных скидок."""

    __tablename__ = "personal_discount"
    discount_id = sqlalchemy.Column(sqlalchemy.ForeignKey("base_discount.id"))
    user_id = sqlalchemy.Column(UUID(as_uuid=True))
    discount_status = sqlalchemy.Column(sqlalchemy.Enum(LoyaltyStatus))

    __table_args__ = (sqlalchemy.UniqueConstraint('discount_id', 'user_id', name='discount_user'),)
