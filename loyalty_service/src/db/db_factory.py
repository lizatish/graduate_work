from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from core.config import get_settings


conf = get_settings()

async_session: AsyncSession | None = None


async def init_session():
    """Инициализирует сессию алхимии и модели."""
    global async_session
    if not async_session:
        engine: AsyncEngine = create_async_engine(conf.DATABASE_URL_ASYNC, echo=False)
        async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    """Вовзаращет сессию алхимии."""
    async with async_session() as session:
        return session
