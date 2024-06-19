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

    def generate_turbidity():
        data = {
            'Turbidity': faker.random_int(min=-1, max=1),  # Turbidity(T)
        }
        return json.dumps(data)
        
    def generate_tss():
        data = {
            'TSS': faker.random_int(min=-5, max=5),  # Biochemical Oxygen Demand (BOD)
        }
        return json.dumps(data)
        
    def generate_ph():
        data = {
            'pH': round(faker.pyfloat(min_value=6.5, max_value=9, right_digits=2), 2),  # pH
        }
        return json.dumps(data)
        
    def generate_bod():
        data = {
            'BOD': round(faker.pyfloat(min_value=0, max_value=10, right_digits=2), 2),  # bod
        }
        return json.dumps(data)
        
    def generate_Coliforms():
        data = {
            'Corliforms': round(faker.pyfloat(min_value=60, max_value=120, right_digits=2), 2),  #coliform
        }
        return json.dumps(data)
        
    def generate_average_inflow():
        data = {
            'Average_inflow': round(faker.pyfloat(min_value=9000, max_value=10000, right_digits=2), 2),  #AVI
        }
        return json.dumps(data)

    def generate_total_grid():
        data = {
            'Total_grid': round(faker.pyfloat(min_value=0.1, max_value=100, right_digits=2), 2),  #total_grid
        }
        return json.dumps(data)
        
        
    while True:
        # Generate simulated data
        turbidity = generate_turbidity()
        turbidity_response = producer.send('tertiary_parameter', turbidity.encode("utf-8"))
        logger.info(f"Sent message: {turbidity_response}")
        print("Data produced:", turbidity)
        
        tss = generate_tss()
        tss_response = producer.send('tertiary_parameter', tss.encode("utf-8"))
        logger.info(f"Sent message: {tss_response}")
        print("Data produced:", tss)
        
        ph = generate_ph()
        ph_response = producer.send('tertiary_parameter', ph.encode("utf-8"))
        logger.info(f"Sent message: {ph_response}")
        print("Data produced:", ph)
        
        bod = generate_bod()
        bod_response = producer.send('tertiary_parameter', bod.encode("utf-8"))
        logger.info(f"Sent message: {bod_response}")
        print("Data produced:", bod)

        coliforms = generate_Coliforms()
        coliforms_response = producer.send('tertiary_parameter', coliforms.encode("utf-8"))
        logger.info(f"Sent message: {coliforms_response}")
        print("Data produced:", coliforms)
        
        average_inflow = generate_average_inflow()
        average_inflow_response = producer.send('tertiary_parameter', average_inflow.encode("utf-8"))
        logger.info(f"Sent message: {average_inflow_response}")
        print("Data produced:", average_inflow)
        
        total_grid = generate_total_grid()
        total_grid_response = producer.send('tertiary_parameter', total_grid.encode("utf-8"))
        logger.info(f"Sent message: {total_grid_response}")
        print("Data produced:", total_grid)
        
        time.sleep(2)

except Exception as e:
    logger.exception("An error occurred during message production: %s", e)

finally:
    # Flush and close the producer
    producer.flush()
    producer.close()

