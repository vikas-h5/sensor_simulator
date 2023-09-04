# Sensor Data Simulation and Monitoring

This project simulates the behavior of sensors, monitors their readings, and provides APIs to retrieve data based on specific criteria. It involves creating MQTT publishers and subscribers, integrating with MongoDB and Redis for data storage, and building FastAPI endpoints for data retrieval.

## Table of Contents

* Overview
* Project Structure
* Getting Started
* Usage
* Endpoints
* Dependencies

## Overview

The project's main goal is to simulate sensor data, publish it using MQTT, subscribe to the data, store it in MongoDB and Redis, and provide API endpoints for accessing the stored data. The key components are:

* MQTT Broker: A Mosquitto MQTT broker is deployed using Docker to handle communication between publishers and subscribers.
* MQTT Publisher: Python MQTT clients simulate sensor data and publish it to MQTT topics.
* MQTT Subscriber (MongoDB): Python MQTT clients subscribe to topics and store received data in MongoDB.
* MQTT Subscriber (Redis): Python MQTT clients subscribe to topics and store the latest sensor readings in Redis.
* FastAPI Application: A FastAPI application exposes API endpoints to retrieve sensor data based on specific criteria.

## Project Structure

The project directory structure is organized as follows:

sensor_simulator/\
│\
├── mqtt_broker/\
│   ├── Dockerfile\
│   └── mosquitto.conf\
│\
├── mqtt_publisher/\
│   ├── Dockerfile\
│   ├── main.py\
│   └── requirements.txt\
│\
├── mqtt_subscriber_mongo/\
│   ├── Dockerfile\
│   ├── main.py\
│   └── requirements.txt\
│\
├── mqtt_subscriber_redis/\
│   ├── Dockerfile\
│   ├── main.py\
│   └── requirements.txt\
│\
├── fastapi_app/\
│   ├── Dockerfile\
│   ├── main.py\
│   └── requirements.txt\
│\
└── docker-compose.yml\

## Getting Started

To run the project, follow these steps:

1. Clone this repository: `git clone https://github.com/vikas-h5/sensor_simulator.git`
2. Navigate to the project directory: `cd sensor_simulator`
3. Install Docker and Docker Compose if not already installed.
4. Update configuration files and scripts as needed (e.g., MQTT topics, MongoDB/Redis configurations).
5. Build and start the services using Docker Compose: `docker compose up`

## Usage

Once the services are up and running, you can:

* Use MQTT publishers to simulate and publish sensor data to MQTT topics.
* Observe MQTT subscribers storing data in MongoDB and Redis.
* Access FastAPI endpoints to retrieve sensor data.

Refer to the Endpoints section below for details on available API endpoints.

## Endpoints

The FastAPI application exposes the following endpoints:

* **Fetch Sensor Readings by Time Range:**

  GET /sensor-readings?start=<start_time>&end=<end_time>

  ```
  curl -X GET "http://localhost:8000/sensor-readings?start=2023-01-01T00:00:00&end=2023-01-02T00:00:00"
  ```

  Retrieve sensor readings within the specified time range.
* **Fetch Latest Sensor Readings:**

  GET /latest-readings/<sensor_id>

  ```
  curl -X GET "http://localhost:8000/latest-readings/sensor_1"
  ```

  Retrieve the latest ten sensor readings for the specified sensor ID.

## Dependencies

The project uses the following major dependencies:

* Eclipse Mosquitto (MQTT broker)
* Paho MQTT (Python MQTT client)
* MongoDB (NoSQL database for storing sensor data)
* Redis (In-memory data store for latest sensor readings)
* FastAPI (Python web framework for building APIs)
* Uvicorn (ASGI server for running FastAPI application)
