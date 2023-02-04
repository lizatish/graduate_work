from functools import lru_cache
from datetime import datetime
import uuid
import logging
from typing import Optional

from fastapi import Depends
import sqlalchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import get_settings
from db.db_factory import get_session
from models.db_models import BaseDiscount, DiscountType, PersonalDiscount, DiscountStatus
from models.broker_models import DiscountTypeBroker

conf = get_settings()
logger = logging.getLogger()


class DiscountService:
    """Сервис для работы со скидками."""

    def __init__(self, session: AsyncSession):
        """Инициализация сервиса."""
        self.session = session

    async def get_discounts(self, user_id: uuid.UUID) -> sqlalchemy.engine.result.ScalarResult:
        """Функция для получения списка скидок."""
        discounts = await self.session.execute(
            select(BaseDiscount, PersonalDiscount.discount)
            .outerjoin(PersonalDiscount)
            .where(
                or_(
                    (BaseDiscount.discount_type == DiscountType.all_users),
                    (
                        (PersonalDiscount.user_id == user_id) &
                        (PersonalDiscount.discount_status == DiscountStatus.not_processed)
                    )
                )

            )
            .filter(BaseDiscount.expired_at > datetime.now())  # type: ignore
        )
        return discounts.scalars()

    async def change_personal_discount_status(
            self, user_id: uuid.UUID, discount_id: uuid.UUID,
            current_status: DiscountStatus, required_status: DiscountStatus
    ) -> bool:
        """Функция для изменения статуса скидки."""
        discount = await self.get_personal_discount(user_id, discount_id, current_status)
        if discount:
            discount.discount_status = required_status
            await self.session.commit()
            return True
        return False

    async def get_personal_discount(
            self, user_id: uuid.UUID, discount_id: uuid.UUID, status: DiscountStatus
    ) -> Optional[PersonalDiscount]:
        """Функция для получения персональной скидки."""
        discount = await self.session.execute(
            select(PersonalDiscount)
            .where(
                (PersonalDiscount.discount == discount_id) &
                (PersonalDiscount.user_id == user_id) &
                (PersonalDiscount.discount_status == status)
            )
        )
        return discount.scalars().first()

    async def create_personal_discounts(
            self, user_id: uuid.UUID, discount_type: DiscountTypeBroker
    ) -> bool:
        """Функция для создания персональных скидок пользователю."""
        discounts = await self.get_discounts_by_type(discount_type)
        personal_discounts = []
        for discount in discounts:
            personal_discounts.append(
                PersonalDiscount(
                    discount=discount.id, user_id=user_id, discount_status=DiscountStatus.not_processed  # type: ignore
                )
            )
        self.session.add_all(personal_discounts)
        try:
            await self.session.commit()
            return True
        except IntegrityError as _:
            await self.session.rollback()
            return False

    async def get_discounts_by_type(
            self, discount_type: DiscountTypeBroker
    ) -> sqlalchemy.engine.result.ScalarResult:
        """Функция для получения списка скидок с определенным типом."""
        discounts = await self.session.execute(
            select(BaseDiscount)
            .where(BaseDiscount.discount_type == discount_type.value)  # type: ignore
            .filter(BaseDiscount.expired_at > datetime.now())  # type: ignore
        )
        return discounts.scalars()


@lru_cache()
def get_discount_service(
        session: AsyncSession = Depends(get_session)
) -> DiscountService:
    return DiscountService(session)
