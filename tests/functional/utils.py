import sqlalchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


async def create_pg_records(session: AsyncSession, model, models_list_kwargs: list[dict]):
    """Добавляет запись в таблицу postgres, конвертируя в модель входящий словарь"""
    for model_data in models_list_kwargs:
        instance = model(**model_data)
        session.add(instance)
        try:
            await session.commit()
        except IntegrityError as _:
            await session.rollback()


async def delete_all_pg_records(session: AsyncSession, model):
    """Удаляет все записи о конкретной модели (из конкретной таблицы)."""
    query = sqlalchemy.delete(model)
    await session.execute(query)
    await session.commit()
