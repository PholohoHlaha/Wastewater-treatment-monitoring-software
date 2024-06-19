from kafka import KafkaProducer
from faker import Faker
import json
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    faker = Faker()

    def generate_ss():
        data = {
            'SS': faker.random_int(min=10, max=50),  # Suspended Solids (SS)
        }
        return json.dumps(data)
        
    def generate_bod():
        data = {
            'BOD': faker.random_int(min=1, max=10),  # Biochemical Oxygen Demand (BOD)
        }
        return json.dumps(data)
        
    def generate_ph():
        data = {
            'pH': round(faker.pyfloat(min_value=6, max_value=8, right_digits=2), 2),  # pH
        }
        return json.dumps(data)
        
    def generate_temperature():
        data = {
            'Temperature': round(faker.pyfloat(min_value=10, max_value=30, right_digits=2), 2),  # Temperature
        }
        return json.dumps(data)
        
    while True:
        # Generate simulated data
        ss = generate_ss()
        ss_response = producer.send('primary_parameter', ss.encode("utf-8"))
        logger.info(f"Sent message: {ss_response}")
        print("Data produced:", ss)
        
        bod = generate_bod()
        bod_response = producer.send('primary_parameter', bod.encode("utf-8"))
        logger.info(f"Sent message: {bod_response}")
        print("Data produced:", bod)
        
        ph = generate_ph()
        ph_response = producer.send('primary_parameter', ph.encode("utf-8"))
        logger.info(f"Sent message: {ph_response}")
        print("Data produced:", ph)
        
        temperature = generate_temperature()
        temperature_response = producer.send('primary_parameter', temperature.encode("utf-8"))
        logger.info(f"Sent message: {temperature_response}")
        print("Data produced:", temperature)
        
        time.sleep(2)

except Exception as e:
    logger.exception("An error occurred during message production: %s", e)

finally:
    # Flush and close the producer
    producer.flush()
    producer.close()

