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

    def generate_do():
        data = {
            'DO': faker.random_int(min=2.0, max=5.0),  # Dissolved Oxygen (DO)
        }
        return json.dumps(data)
        
    def generate_mlss():
        data = {
            'MLSS': faker.random_int(min=2000, max=5000),  # Mixed Liquor Suspended Solids
        }
        return json.dumps(data)
        
    def generate_MLVSS():
        data = {
            'MLVSS': round(faker.pyfloat(min_value=1500, max_value=4000, right_digits=2), 2),  # Mixed Liquor Volatile Suspended Solids 
        }
        return json.dumps(data)
        
    def generate_ammonia():
        data = {
            'ammonia': round(faker.pyfloat(min_value=0.5, max_value=10, right_digits=2), 2),  # ammonia
        }
        return json.dumps(data)

    def generate_nitrate():
        data = {
            'nitrate': round(faker.pyfloat(min_value=0.1, max_value=2.0, right_digits=2), 2),  # nitrate
        }
        return json.dumps(data)

    def generate_Phosphorus():
        data = {
            'Phosphorus': round(faker.pyfloat(min_value=1.0, max_value=10.0, right_digits=2), 2),  # Phosphorus
        }
        return json.dumps(data)

    def generate_turbidity():
        data = {
            'turbidity': faker.random_int(min=2, max=20),  # turbidity
        }
        return json.dumps(data)

    def generate_ORP():
        data = {
            'ORP': faker.random_int(min=2, max=20),  # ORP
        }
        return json.dumps(data)
        
        
    while True:
        # Generate simulated data
        do = generate_do()
        do_response = producer.send('secondary_parameter', do.encode("utf-8"))
        logger.info(f"Sent message: {do_response}")
        print("Data produced:", do)

        mlss = generate_mlss()
        mlss_response = producer.send('secondary_parameter', mlss.encode("utf-8"))
        logger.info(f"Sent message: {mlss_response}")
        print("Data produced:", mlss)
        
        mlvss = generate_MLVSS()
        mlvss_response = producer.send('secondary_parameter', mlvss.encode("utf-8"))
        logger.info(f"Sent message: {mlvss_response}")
        print("Data produced:", mlvss)

        ammonia = generate_ammonia()
        ammonia_response = producer.send('secondary_parameter', ammonia.encode("utf-8"))
        logger.info(f"Sent message: {ammonia_response}")
        print("Data produced:", ammonia)
        
        nitrate = generate_nitrate()
        nitrate_response = producer.send('secondary_parameter', nitrate.encode("utf-8"))
        logger.info(f"Sent message: {nitrate_response}")
        print("Data produced:", nitrate)
        
        phosphorus = generate_Phosphorus()
        phosphorus_response = producer.send('secondary_parameter', phosphorus.encode("utf-8"))
        logger.info(f"Sent message: {phosphorus_response}")
        print("Data produced:", phosphorus)
        
        turbidity = generate_turbidity()
        turbidity_response = producer.send('secondary_parameter', turbidity.encode("utf-8"))
        logger.info(f"Sent message: {turbidity_response}")
        print("Data produced:", turbidity)

        orp = generate_ORP()
        orp_response = producer.send('secondary_parameter', orp.encode("utf-8"))
        logger.info(f"Sent message: {orp_response}")
        print("Data produced:", orp)
        
        time.sleep(2)

except Exception as e:
    logger.exception("An error occurred during message production: %s", e)

finally:
    # Flush and close the producer
    producer.flush()
    producer.close()

