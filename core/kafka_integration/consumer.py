from confluent_kafka import Consumer, KafkaException
from django.conf import settings

# Конфигурация Kafka-консьюмера
consumer_conf = {
    'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVERS,
    'group.id': 'my-django-app',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_conf)

# Функция для получения сообщений из Kafka
def consume_messages(topic):
    consumer.subscribe([topic])

    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                raise KafkaException(msg.error())
        else:
            print('Received message: {}'.format(msg.value().decode('utf-8')))

# Пример использования
if __name__ == "__main__":
    consume_messages('test_topic')