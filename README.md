Wastewater Treatment Control System

This repository provides a Docker-based setup for a data analysis application that integrates various services, including Grafana, Zookeeper, Kafka, Kafka Manager, Logstash, InfluxDB, Telegraf, and a Django web application.

Prerequisites

    Docker
    Docker Compose
    Python 3.11

Getting Started
Clone the Repository

bash

git clone https://github.com/PholohoHlaha/Wastewater-treatment-monitoring-software.git

cd Wastewater-treatment-monitoring-software

Start Docker Services

bash

docker-compose up -d

Install Python Dependencies

bash

pip install pipenv
pipenv install

Run Django Application

bash

pipenv run python manage.py runserver

Accessing the Services

    Grafana: http://localhost:3000
    Kafka Manager: http://localhost:9001
    Django Application: http://localhost:8000

Repository Structure
docker-compose.yml

Defines the Docker services and their configurations.
Pipfile

Specifies the Python dependencies for the Django application.
requirements.txt

Lists specific versions of required Python packages.
Services
Grafana

    Image: grafana/grafana:latest
    Ports: 3000
    Volumes:
        grafana_data:/var/lib/grafana
        ./defaults.ini:/usr/share/grafana/conf/defaults.ini:ro
    Environment Variables:
        GF_SECURITY_ADMIN_USER=admin
        GF_SECURITY_ADMIN_PASSWORD=admin

Zookeeper

    Image: confluentinc/cp-zookeeper:7.4.4
    Ports: 2181
    Environment Variables:
        ZOOKEEPER_CLIENT_PORT=2181
        ZOOKEEPER_TICK_TIME=2000

Kafka

    Image: confluentinc/cp-kafka:7.4.4
    Ports: 9092, 9093
    Environment Variables:
        KAFKA_BROKER_ID=1
        KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181
        KAFKA_ADVERTISED_LISTENERS=INTERNAL://kafka:9092,EXTERNAL://kafka:9093
        KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=INTERNAL:PLAINTEXT,EXTERNAL:PLAINTEXT
        KAFKA_INTER_BROKER_LISTENER_NAME=INTERNAL
        KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1

Kafka Manager

    Image: hlebalbau/kafka-manager:stable
    Ports: 9001
    Environment Variables:
        ZK_HOSTS=zookeeper:2181
        APPLICATION_SECRET=random-secret

Logstash

    Image: logstash:7.9.1
    Ports: 5044
    Volumes:
        ./logstash-kafka.conf:/usr/share/logstash/pipeline/logstash-kafka.conf
    Healthcheck:
        test: ["CMD", "curl", "--silent", "--fail", "http://logstash-cntr:9600"]
        interval: 30s
        timeout: 15s
        retries: 3

Producer Applications

    Image: producer-app
    Command: python3 producer.py, python3 producer2.py, python3 producer3.py
    Volumes:
        ./producer.py:/app/producer.py
        ./producer2.py:/app/producer2.py
        ./producer3.py:/app/producer3.py

Telegraf

    Image: telegraf
    Ports: 8125
    Volumes: ./telegraf.conf:/etc/telegraf/telegraf.conf:ro

InfluxDB

    Image: influxdb:1.8-alpine
    Ports: 8086
    Volumes: influxdb_data:/var/lib/influxdb
    Environment Variables:
        INFLUXDB_DB=influx
        INFLUXDB_ADMIN_USER=admin
        INFLUXDB_ADMIN_PASSWORD=admin

Python Dependencies
Pipfile

Lists the Python dependencies for the Django application, including:

    django
    django-heroku
    gunicorn
    psycopg2
    djangorestframework
    django-cors-headers
    django-filter
    markdown
    django-ckeditor
    folium
    geocoder

requirements.txt

Specific versions of required Python packages:

    Django==4.0.3
    django-extensions==3.1.5
    plotly==5.6.0

Django Application
Files

    views.py: Contains the views for rendering data.
    models.py: Defines the WaterData and WaterData2 models.
    forms.py: Defines the DateForm for filtering data by date.

Example Libraries Used

    plotly.express for data visualization
    Django shortcuts and models for web handling and ORM

Volumes

    grafana_data: Persistent storage for Grafana data.
    influxdb_data: Persistent storage for InfluxDB data.
