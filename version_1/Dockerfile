# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install kafka-python

RUN pip install faker

# Run your Python script when the container launches
CMD ["python", "producer.py"]

CMD ["python", "producer2.py"]

