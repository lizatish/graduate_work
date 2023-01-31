from functools import lru_cache
from datetime import datetime

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError


from core.config import get_settings
from db.db_factory import get_session
from models.db_models import BaseDiscount

conf = get_settings()


class DiscountService:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def test(self):
        return await self.create(
            BaseDiscount,
            expired_at=datetime.now(),
            percent=30.5,
            group_product_id="e118b6a5-f42b-4c27-ac63-b703720ceeef",
            discount_type="all_users"
        )

    async def create(self, model, **kwargs):
        instance = model(**kwargs)
        self.session.add(instance)
        try:
            await self.session.commit()
            return instance
        except IntegrityError as _:
            await self.session.rollback()
            return None


@lru_cache()
def get_discount_service(
        session: AsyncSession = Depends(get_session)
) -> DiscountService:
    return DiscountService(session)
