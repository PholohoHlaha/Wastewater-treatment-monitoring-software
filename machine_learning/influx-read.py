import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "influx"
url = "http://localhost:8086"

client = influxdb_client.InfluxDBClient(
    url = url
)

query_api = client.query_api()
query = 'from(bucket:"influx")\
|> range(start: -10m)\
|> filter(fn:(r) => r._measurement == "kafka_consumer")\
|> filter(fn:(r) => r.host == "058e286310c1")\
|> filter(fn:(r) => r._field == "Temperature")'

result = query_api.query(query=query)

results = []

for table in result:
    for record in table.records:
        result.append((record.get_field(), record.get_value()))

print(results)
