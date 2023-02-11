import uuid

import sqlalchemy
from sqlalchemy import UUID
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import relationship
from sqlalchemy.orm.decl_api import DeclarativeMeta, declarative_base
from sqlalchemy.sql import expression
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

    personal_promocodes = relationship(
        "PersonalPromocode",
        back_populates="promocode",
        cascade="all, delete",
        passive_deletes=True,
    )
    promocode_history = relationship(
        "PromocodeHistory",
        back_populates="promocode",
        cascade="all, delete",
        passive_deletes=True,
    )


class PersonalPromocode(Base, UUIDMixin):
    """Модель персональных промокодов."""

    __tablename__ = "personal_promocode"
    __table_args__ = (sqlalchemy.UniqueConstraint('promocode_id', 'user_id', name='promocode_user'),)

    promocode_id = sqlalchemy.Column(sqlalchemy.ForeignKey("base_promocode.id", ondelete="CASCADE"), nullable=False)
    user_id = sqlalchemy.Column(UUID(as_uuid=True))

    promocode = relationship("BasePromocode", back_populates="personal_promocodes")


class PromocodeHistory(Base, UUIDMixin):
    """Модель истории промокодов."""

    __tablename__ = "promocode_history"
    promocode_id = sqlalchemy.Column(sqlalchemy.ForeignKey("base_promocode.id", ondelete="CASCADE"), nullable=False)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime(), server_default=utcnow())
    user_id = sqlalchemy.Column(UUID(as_uuid=True))
    promocode_status = sqlalchemy.Column(sqlalchemy.Enum(LoyaltyStatus))

    promocode = relationship("BasePromocode", back_populates="promocode_history")


class BaseDiscount(Base, UUIDMixin, TimeStampedMixin):
    """Модель всех скидок."""

    __tablename__ = "base_discount"
    percent = sqlalchemy.Column(sqlalchemy.Float())
    group_product_id = sqlalchemy.Column(UUID(as_uuid=True))
    discount_type = sqlalchemy.Column(sqlalchemy.Enum(DiscountType))

    personal_discounts = relationship(
        "PersonalDiscount",
        back_populates="discount",
        cascade="all, delete",
        passive_deletes=True,
    )


class PersonalDiscount(Base, UUIDMixin):
    """Модель персональных скидок."""

    __tablename__ = "personal_discount"
    __table_args__ = (sqlalchemy.UniqueConstraint('discount_id', 'user_id', name='discount_user'),)

    discount_id = sqlalchemy.Column(sqlalchemy.ForeignKey("base_discount.id", ondelete="CASCADE"), nullable=False)
    user_id = sqlalchemy.Column(UUID(as_uuid=True))
    discount_status = sqlalchemy.Column(sqlalchemy.Enum(LoyaltyStatus))

    discount = relationship("BaseDiscount", back_populates="personal_discounts")
