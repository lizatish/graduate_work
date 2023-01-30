import asyncio
from asyncio import AbstractEventLoop
from typing import AsyncGenerator, Generator

import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from models.db_models import PersonalPromocode, PromocodeHistory, BasePromocode, BaseDiscount, PersonalDiscount
from tests.functional.settings import get_settings, TestSettings
from tests.functional.testdata.discounts import personal_discounts_init_data, base_discounts_init_data
from tests.functional.testdata.promocodes import personal_promocodes_init_data, \
    base_promocodes_init_data, promocode_history_init_data
from tests.functional.utils import create_pg_records, delete_all_pg_records

conf = get_settings()


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    """Фикстура главного цикла событий."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


async def init():
    from broker.broker_connection import init_broker_connection
    from db.db_factory import init_session
    await init_session()
    await init_broker_connection()


@pytest.fixture
def api_client(event_loop: AbstractEventLoop, mocker) -> Generator:
    """Фикстура апи-клиента с моком es и redis."""
    mocker.patch("core.config.get_settings", wraps=get_settings)
    mocker.patch("core.config.Settings", wraps=TestSettings)

    from main import app

    client = AsyncClient(app=app, base_url=conf.BASE_URL)

    asyncio.get_event_loop().run_until_complete(init())

    yield client
    event_loop.run_until_complete(client.aclose())


@pytest_asyncio.fixture
async def promocodes_api_client(api_client: AsyncClient, postgres_promocodes_data: AsyncSession) -> AsyncGenerator:
    """Фикстура апи-клиента с заполненными данными es для тестирования промокодов."""
    yield api_client


@pytest_asyncio.fixture(scope="session")
async def discounts_api_client(api_client: AsyncClient, postgres_discounts_data: AsyncSession) -> AsyncGenerator:
    """Фикстура апи-клиента с заполненными данными es для тестирования скидок."""
    yield api_client


@pytest.fixture(scope="session")
async def postgres_promocodes_data() -> AsyncGenerator:
    """Фикстура алхимии для бд postgres c заполненными данными о промокодах."""
    from db.db_factory import get_session

    session = await get_session()

    await create_pg_records(session, BasePromocode, base_promocodes_init_data)
    await create_pg_records(session, PersonalPromocode, personal_promocodes_init_data)
    await create_pg_records(session, PromocodeHistory, promocode_history_init_data)

    yield session

    await delete_all_pg_records(session, BasePromocode)
    await delete_all_pg_records(session, PersonalPromocode)
    await delete_all_pg_records(session, PromocodeHistory)


@pytest.fixture(scope="session")
async def postgres_discounts_data() -> AsyncGenerator:
    """Фикстура алхимии для бд postgres c заполненными данными о скидках."""
    from db.db_factory import get_session

    session = await get_session()

    await create_pg_records(session, BaseDiscount, base_discounts_init_data)
    await create_pg_records(session, PersonalDiscount, personal_discounts_init_data)

    yield session

    await delete_all_pg_records(session, BaseDiscount)
    await delete_all_pg_records(session, PersonalDiscount)
