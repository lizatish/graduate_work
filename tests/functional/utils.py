from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


async def create_pg_records(session: AsyncSession, model, models_list_kwargs: list[tuple]):
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
    models_list_data = model.query.all()
    for model_data in models_list_data:
        await session.delete(model_data)
        await session.commit()
