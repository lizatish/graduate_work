from aio_pika import connect, Connection, Channel
from broker.callbacks import callback_auth_discounts

from core.config import get_settings

conf = get_settings()

_connection: Connection | None = None
_channel: Channel | None = None

BROKER_QUEUE_CALLBACK_DICT: dict = {
    'auth.discounts': callback_auth_discounts,
}


async def init_broker_connection():
    """Инициализация соединения с брокером"""
    global _channel, _connection
    _connection = await connect(conf.BROKER_URL)
    _channel = await _connection.channel()
    for queue_name, callback_name in BROKER_QUEUE_CALLBACK_DICT.items():
        queue = await _channel.declare_queue(queue_name)
        await queue.consume(callback_name, no_ack=True)
