# Sensor Monitoring System (FastAPI + Python)

Industrial-style telemetry monitoring backend that simulates real-time temperature, pressure, and vibration sensor streams with automated threshold-based alert detection.

## Features

- Simulated real-time sensor data generation
- Temperature, pressure, vibration monitoring
- Threshold-based alert detection system
- Background threaded sensor stream processing
- REST API endpoints for retrieving live sensor data
- SQLite database storage using SQLAlchemy ORM
- Swagger UI API documentation

## Tech Stack

Python
FastAPI
SQLAlchemy
SQLite
Threading
REST API
Pydantic

## API Endpoints

GET /sensors

Returns latest sensor readings from telemetry stream.

## Example Output

{
  "sensor_name": "temperature",
  "sensor_value": 87.4,
  "timestamp": "2026-04-04T09:02:56"
}

## Use Case

Designed as a simulation of industrial automation telemetry pipelines used in:

- manufacturing monitoring systems
- predictive maintenance platforms
- robotics sensor integration
- SCADA-style backend services
