import pika
import json


class Publisher:
    def __init__(self, config):
        self.config = config

    def publish(self, queue, message):
        connection = self.create_connection()
        channel = connection.channel()
        channel.queue_declare(queue=queue)
        channel.basic_publish(exchange='', routing_key=queue, body=json.dumps(message))

    def create_connection(self):
        param = pika.ConnectionParameters(host=self.config['host'], port=self.config['port'])
        return pika.BlockingConnection(param)


config = {'host': 'localhost', 'port': 5672}
publisher = Publisher(config)
publisher.publish('registration', {"user_id": "123"})
publisher.publish('birthday', {"user_id": "321"})