from functools import lru_cache
from datetime import datetime

from fastapi import Depends
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError


from core.config import get_settings
from db.db_factory import get_session
from models.db_models import BaseDiscount, DiscountType, PersonalDiscount, DiscountStatus

conf = get_settings()


class DiscountService:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_discounts(self, user_id):
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
            .filter(BaseDiscount.expired_at > datetime.now())
        )
        return discounts.scalars()

    async def change_personal_discount_status(self, user_id, discount_id, current_status, required_status):
        discount = await self.get_personal_discount(user_id, discount_id, current_status)
        if discount:
            discount.discount_status = required_status
            await self.session.commit()
            return True
        return False

    async def get_personal_discount(self, user_id, discount_id, status: DiscountStatus):
        discount = await self.session.execute(
            select(PersonalDiscount)
            .where(
                (PersonalDiscount.discount == discount_id) &
                (PersonalDiscount.user_id == user_id) &
                (PersonalDiscount.discount_status == status)
            )
        )
        return discount.scalars().first()


@lru_cache()
def get_discount_service(
        session: AsyncSession = Depends(get_session)
) -> DiscountService:
    return DiscountService(session)
