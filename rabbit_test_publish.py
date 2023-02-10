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
publisher.publish('discounts', {"user_id": "6bc9c710-d580-4acb-86c4-b28e825ac752", "discount_type": "registration"})