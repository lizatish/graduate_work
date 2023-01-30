import asyncio
from asyncio import AbstractEventLoop
from typing import AsyncGenerator, Generator

import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from models.db_models import PersonalPromocode, PromocodeHistory, BasePromocode, BaseDiscount, PersonalDiscount, Base
from tests.functional.settings import get_settings, TestSettings
from tests.functional.testdata.discounts import personal_discounts_init_data, base_discounts_init_data
from tests.functional.testdata.promocodes import personal_promocodes_init_data, \
    base_promocodes_init_data, promocode_history_init_data
from tests.functional.utils import create_pg_records, delete_all_pg_records

conf = get_settings()


@pytest_asyncio.fixture(scope="session")
def event_loop() -> Generator:
    """Фикстура главного цикла событий."""
    loop = asyncio.get_event_loop()
    yield loop
    asyncio.get_event_loop().stop()


async def init():
    from broker.broker_connection import init_broker_connection
    from db.db_factory import init_session
    await init_session()
    await init_broker_connection()


async def shutdown():
    import broker.broker_connection
    from db.db_factory import get_session

    session = await get_session()
    await session.close()
    await broker.broker_connection._channel.close()
    await broker.broker_connection._connection.close()


@pytest_asyncio.fixture
def api_client(event_loop: AbstractEventLoop, mocker) -> Generator:
    """Фикстура апи-клиента с моком es и redis."""
    mocker.patch("core.config.get_settings", wraps=get_settings)
    mocker.patch("core.config.Settings", wraps=TestSettings)

    from main import app

    client = AsyncClient(app=app, base_url=conf.BASE_URL)

    asyncio.get_event_loop().run_until_complete(init())

    yield client
    asyncio.get_event_loop().run_until_complete(shutdown())


@pytest_asyncio.fixture
async def promocodes_api_client(
        api_client: AsyncClient,
        postgres_promocodes_data: AsyncSession,
        mocker
) -> AsyncGenerator:
    """Фикстура апи-клиента с заполненными данными es для тестирования промокодов."""
    yield api_client


@pytest_asyncio.fixture(scope="session")
async def discounts_api_client(api_client: AsyncClient, postgres_discounts_data: AsyncSession) -> AsyncGenerator:
    """Фикстура апи-клиента с заполненными данными es для тестирования скидок."""
    yield api_client


@pytest_asyncio.fixture
async def postgres_promocodes_data(mocker) -> AsyncGenerator:
    """Фикстура алхимии для бд postgres c заполненными данными о промокодах."""
    mocker.patch("core.config.get_settings", wraps=get_settings)
    mocker.patch("core.config.Settings", wraps=TestSettings)
    from db.db_factory import get_session, get_engine

    session = await get_session()
    engine = await get_engine()

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    await create_pg_records(session, BasePromocode, base_promocodes_init_data)
    await create_pg_records(session, PersonalPromocode, personal_promocodes_init_data)
    await create_pg_records(session, PromocodeHistory, promocode_history_init_data)

    yield session

    await delete_all_pg_records(session, PromocodeHistory)
    await delete_all_pg_records(session, PersonalPromocode)
    await delete_all_pg_records(session, BasePromocode)


@pytest_asyncio.fixture
async def postgres_discounts_data(mocker) -> AsyncGenerator:
    """Фикстура алхимии для бд postgres c заполненными данными о скидках."""
    mocker.patch("core.config.get_settings", wraps=get_settings)
    mocker.patch("core.config.Settings", wraps=TestSettings)
    from db.db_factory import get_session, get_engine

    session = await get_session()

    engine = await get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    await create_pg_records(session, BaseDiscount, base_discounts_init_data)
    await create_pg_records(session, PersonalDiscount, personal_discounts_init_data)

    yield session

    await delete_all_pg_records(session, BaseDiscount)
    await delete_all_pg_records(session, PersonalDiscount)
