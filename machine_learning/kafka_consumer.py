from confluent_kafka import Consumer, KafkaError

class KafkaConsumer:
    def __init__(self, kafka_servers, group_id, topics):
        self.consumer = Consumer({
            'bootstrap.servers': kafka_servers,
            'group.id': group_id,
            'auto.offset.reset': 'earliest'
        })
        self.topics = topics

    def consume_messages(self):
        self.consumer.subscribe(self.topics)

        try:
            while True:
                msg = self.consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition, ignore
                        continue
                    else:
                        # Handle other Kafka errors
                        print("Kafka error: {}".format(msg.error()))
                        break
                print('Received message: {}'.format(msg.value().decode('utf-8')))
                # Process and preprocess the message data here
                self.process_message(msg.value().decode('utf-8'))
        except KeyboardInterrupt:
            pass
        finally:
            self.consumer.close()

    def process_message(self, message):
        # Placeholder for message processing logic
        print("Processing message:", message)

# Kafka consumer configuration
kafka_servers = 'kafka:9092'  # Update with your Kafka broker address
group_id = 'tertiary-group'  # Update with your consumer group ID
topics = ['primary_parameters']  # Update with the Kafka topics you want to subscribe to

# Initialize KafkaConsumer instance and start consuming messages
consumer = KafkaConsumer(kafka_servers, group_id, topics)
consumer.consume_messages()
