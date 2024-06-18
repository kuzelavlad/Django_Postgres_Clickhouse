from confluent_kafka import Producer

KAFKA_BOOTSTRAP_SERVERS = 'kafka:9092'

producer_conf = {
    'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
}

producer = Producer(producer_conf)

# Функция для отправки сообщений в Kafka
def send_message(topic, message):
    producer.produce(topic, message.encode('utf-8'))
    producer.flush()

# Пример использования
if __name__ == "__main__":
    send_message('test_topic', 'Hello from Django!')