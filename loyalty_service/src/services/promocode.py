import datetime
import uuid
from functools import lru_cache
from operator import or_

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.schemas.general import BaseAction, discount_mapping
from core.config import get_settings
from db.db_factory import get_session
from models.common import LoyaltyStatus, PromocodeType
from models.db_models import PersonalPromocode, PromocodeHistory, BasePromocode

conf = get_settings()


class PromocodeService:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def check_status(self, user_id: uuid, promocode: BasePromocode, action: BaseAction) -> LoyaltyStatus | None:
        promocode_history = await self.get_promocode_status(user_id, promocode)

        if not promocode_history:
            current_status = LoyaltyStatus.not_processed
        else:
            current_status = promocode_history[0].promocode_status

        if promocode.is_disposable:
            if current_status == discount_mapping[action.value]['current_status']:
                return discount_mapping[action.value]['required_status']
        # promocode_history == 'apply' - возможность многоразового использования промокода
        elif current_status == LoyaltyStatus.finished or current_status == discount_mapping[action.value]['current_status']:
            return discount_mapping[action.value]['required_status']
        return

    def check_promocode_expired(self, promocode: BasePromocode) -> bool:
        if promocode.expired_at < datetime.datetime.utcnow():
            return True
        return False

    async def change_promocode_status(
            self, user_id: uuid, promocode: BasePromocode, new_status: LoyaltyStatus, is_personal: bool):
        """Функция для изменения статуса персонального промокода."""

        promocode_history = await self.get_promocode_status(user_id, promocode)
        if not promocode_history:
            current_status = PromocodeHistory(
                promocode_id=promocode.id,
                user_id=user_id,
                promocode_status=new_status
            )
            self.session.add(current_status)
        else:
            current_status = promocode_history[0]
            current_status.promocode_status = new_status
        await self.session.commit()

    async def get_promocode(self, user_id: uuid.UUID, label: str) -> (BasePromocode | None, bool):
        """Функция для получения персонального промокода."""

        query = (select(BasePromocode)
        .join(
            BasePromocode.personal_promocodes,
            isouter=True
        )
        .where(
            or_(
                (
                        (BasePromocode.promocode_type == PromocodeType.all_users) &
                        (BasePromocode.label == label)
                ),
                (
                        (BasePromocode.label == label) &
                        (PersonalPromocode.user_id == user_id)
                )
            )
        )
        )
        promocode_data = await self.session.execute(query)
        promocode: BasePromocode = promocode_data.scalars().first()

        if not promocode:
            return None, False

        personal = False
        if promocode.personal_promocodes:
            personal = True
        return promocode, personal

    async def get_promocode_status(self, user_id: str, promocode: BasePromocode):
        promocode_history = await self.session.execute(
            select(PromocodeHistory)
            .where(
                (PromocodeHistory.user_id == user_id) &
                (PromocodeHistory.promocode_id == promocode.id)
            )
            .order_by(PromocodeHistory.created_at.desc())
        )

        return promocode_history.scalars().all()

    async def get_promocodes_history(self, user_id: uuid.UUID) -> list[PromocodeHistory]:
        """Возвращает историю применения промокодов для конкретного пользователя."""
        promocode_history = await self.session.execute(
            select(PromocodeHistory)
            .where(
                (PersonalPromocode.user_id == user_id)
            )
        )
        return list(promocode_history.scalars().all())


@lru_cache()
def get_promocode_service(
        session: AsyncSession = Depends(get_session)
) -> PromocodeService:
    return PromocodeService(session)
