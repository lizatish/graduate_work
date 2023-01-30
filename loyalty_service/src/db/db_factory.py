from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from core.config import get_settings

conf = get_settings()

async_session: AsyncSession | None = None
engine: AsyncEngine | None = None


async def init_session():
    """Инициализирует сессию алхимии и модели."""
    global async_session
    global engine
    if not async_session:
        engine = create_async_engine(conf.DATABASE_URL_ASYNC, echo=False, pool_size=50, max_overflow=0)
        async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    """Вовзаращет сессию алхимии."""
    async with async_session() as session:
        return session


async def get_engine() -> AsyncEngine:
    """Вовзаращет engine текущей сессии."""
    return engine
