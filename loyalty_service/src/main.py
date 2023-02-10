import uuid
import logging
import contextvars

import uvicorn as uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse

from api.v1 import discount, promocode
from core.logging_setup import setup_root_logger
from core.config import get_settings
from db.db_factory import init_session, get_session
from broker import broker_connection
from broker.broker_connection import init_broker_connection

conf = get_settings()
if not conf.TESTING:
    setup_root_logger()


app = FastAPI(
    title=conf.PROJECT_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)

_request_id = contextvars.ContextVar(
    'request_id', default=f'system:{uuid.uuid4()}'
)

factory = logging.getLogRecordFactory()


def record_factory(*args, **kwargs):
    record = factory(*args, **kwargs)
    record.request_id = _request_id.get()
    return record


@app.middleware("http")
async def request_id_middleware(request: Request, call_next):
    request_id = (
            request.headers.get('X-Request-Id')
            or f'direct:{uuid.uuid4()}'
    )
    _request_id.set(request_id)
    return await call_next(request)

logging.setLogRecordFactory(record_factory)


@app.on_event('startup')
async def startup():
    await init_session()
    await init_broker_connection()


@app.on_event('shutdown')
async def shutdown():
    session = await get_session()
    await session.close()
    await broker_connection._channel.close()
    await broker_connection._connection.close()

app.include_router(discount.router, prefix='/api/v1/discount', tags=['discount'])
app.include_router(promocode.router, prefix='/api/v1/promocode', tags=['promocode'])


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=conf.APP_HOST,
        port=conf.APP_PORT
    )
