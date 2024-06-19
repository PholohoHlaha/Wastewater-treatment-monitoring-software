import pytest
import yaml

@pytest.fixture
def docker_compose():
    with open('docker-compose.yml', 'r') as file:
        return yaml.safe_load(file)

def test_grafana_service(docker_compose):
    assert 'grafana' in docker_compose['services']
    grafana = docker_compose['services']['grafana']
    assert grafana['image'] == 'grafana/grafana:latest'
    assert grafana['restart'] == 'always'
    assert grafana['ports'] == ["3000:3000"]
    assert 'environment' in grafana
    assert grafana['environment'] == [
        'GF_SECURITY_ADMIN_USER=admin',
        'GF_SECURITY_ADMIN_PASSWORD=admin',
        'GF_INSTALL_PLUGINS='
    ]
    assert grafana['depends_on'] == ['influxdb']
    assert grafana['volumes'] == [
        'grafana_data:/var/lib/grafana',
        './defaults.ini:/usr/share/grafana/conf/defaults.ini:ro'
    ]

def test_zookeeper_service(docker_compose):
    assert 'zookeeper' in docker_compose['services']
    zookeeper = docker_compose['services']['zookeeper']
    assert zookeeper['image'] == 'confluentinc/cp-zookeeper:7.4.4'
    assert zookeeper['environment'] == {
        'ZOOKEEPER_CLIENT_PORT': 2181,
        'ZOOKEEPER_TICK_TIME': 2000
    }
    assert zookeeper['ports'] == ['22181:2181']

def test_kafka_service(docker_compose):
    assert 'kafka' in docker_compose['services']
    kafka = docker_compose['services']['kafka']
    assert kafka['image'] == 'confluentinc/cp-kafka:7.4.4'
    assert kafka['depends_on'] == ['zookeeper']
    assert kafka['ports'] == ['9092:9092', '9093:9093']
    assert kafka['environment'] == {
        'KAFKA_BROKER_ID': 1,
        'KAFKA_ZOOKEEPER_CONNECT': 'zookeeper:2181',
        'KAFKA_ADVERTISED_LISTENERS': 'INTERNAL://kafka:9092,EXTERNAL://kafka:9093',
        'KAFKA_LISTENER_SECURITY_PROTOCOL_MAP': 'INTERNAL:PLAINTEXT,EXTERNAL:PLAINTEXT',
        'KAFKA_INTER_BROKER_LISTENER_NAME': 'INTERNAL',
        'KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR': 1
    }

def test_producer_services(docker_compose):
    for i in range(1, 4):
        producer_name = f'producer{i}'
        assert producer_name in docker_compose['services']
        producer = docker_compose['services'][producer_name]
        assert producer['image'] == 'producer-app'
        assert producer['command'] == f'python3 producer{i}.py'
        assert producer['volumes'] == [f'./producer{i}.py:/app/producer{i}.py']
        assert producer['depends_on'] == ['kafka']

