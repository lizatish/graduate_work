from functools import lru_cache

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from core.config import get_settings
from db.db_factory import get_session

conf = get_settings()


class PromocodeService:

    def __init__(self, session: AsyncSession):
        self.session = session

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
def get_promocode_service(
        session: AsyncSession = Depends(get_session)
) -> PromocodeService:
    return PromocodeService(session)
