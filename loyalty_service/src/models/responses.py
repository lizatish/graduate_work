from pydantic import BaseModel


class StandardResponse(BaseModel):
    """Модель стандартного успешного ответа fastapi."""
    detail: str
