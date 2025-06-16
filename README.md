# Dockerized Flask System Monitor

This is a lightweight Flask web application that runs inside a Docker container and exposes real-time CPU, memory, disk, and network usage metrics (with a 5-minute history) along with threshold-based alerts. It’s designed to provide quick visibility into the container’s own resource utilization without requiring external monitoring agents.

## Overview

The Dockerized Flask System Monitor offers a simple and efficient way to monitor a Docker container's resource usage. It provides a web-based dashboard and a JSON API for accessing metrics. Built with Flask and Chart.js for the dashboard, the application is production-ready, featuring a multi-stage Docker build, non-root user execution, built-in HEALTHCHECK, and the Gunicorn WSGI server.

## Features

- **Real-time metrics**: CPU, memory, disk, and network usage sampled every second.
- **Rolling history**: 5-minute history for each metric, stored in a fixed-size in-memory buffer.
- **Threshold alerts**: Highlights when a metric exceeds a configured alert threshold.
- **JSON API**:
  - `/api/metrics`: Returns all metrics and their histories as JSON.
  - `/health`: Provides liveness checks.
- **Web UI**:
  - Single-page dashboard rendered via Chart.js.
  - Dynamic coloring when thresholds are breached.
- **Production-ready Docker**:
  - Multi-stage build for minimal image size.
  - Runs as a non-root user.
  - Built-in HEALTHCHECK.
  - Gunicorn WSGI server.

## Prerequisites

- Docker ≥ 20.10
- Python ≥ 3.11 (for local development)
- `make` (optional, for convenience)

**Note**: Ensure Docker is installed and running on your system before proceeding.

## Quickstart

1. **Clone the repo**
   ```bash
   git clone https://github.com/chintanboghara/Dockerized-FlaskSystemMonitor.git
   cd Dockerized-FlaskSystemMonitor
   ```

2. **Copy & edit environment file**
   ```bash
   cp .env.example .env
   # Edit .env to adjust FLASK_ENV or ALERT_THRESHOLD if needed
   ```

3. **Build and run with Docker**
   ```bash
   docker build -t flask-monitor:latest .
   docker run -d \
     --name flask-monitor \
     -p 5000:5000 \
     --env-file .env \
     flask-monitor:latest
   ```

4. **Visit dashboard**
   Open your browser to `http://localhost:5000/`

   **Note**: If port 5000 is in use, specify a different port with the `-p` flag in the `docker run` command (e.g., `-p 8080:5000` maps host port 8080 to container port 5000).

## Configuration

The application can be configured using a `config.json` file and environment variables.

### `config.json`

```json
{
  "alert_threshold": 80
}
```

- `alert_threshold` (integer, 1–99): The default percentage above which metrics are highlighted.

### Environment Variables

Override or supplement `config.json` settings via a `.env` file:

```dotenv
FLASK_ENV=production
ALERT_THRESHOLD=75
```

- `FLASK_ENV`: Flask environment (`development` or `production`).
- `ALERT_THRESHOLD`: Overrides the `alert_threshold` from `config.json`.

## API Endpoints

| Path           | Method | Description                                     |
| -------------- | ------ | ----------------------------------------------- |
| `/health`      | GET    | Returns `{ "status": "ok" }` for health checks. |
| `/api/metrics` | GET    | Returns JSON with current and historical metrics: |
|                |        | ```json                                         |
|                |        | {                                               |
|                |        |   "cpu": [ ... ],                               |
|                |        |   "mem": [ ... ],                               |
|                |        |   "disk": [ ... ],                              |
|                |        |   "net": [ ... ]                                |
|                |        | }                                               |
|                |        | ```                                             |
|                |        | Each metric array contains the last 300 samples (5 minutes at 1 sample per second). |

## Running Tests & CI

This project uses **pytest** for testing, **flake8** for linting, and **safety** for dependency vulnerability checks.

To run the tests and checks:

1. Install required dependencies:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt pytest flake8 safety
   ```

2. Run the linter:
   ```bash
   flake8 .
   ```

3. Check for dependency vulnerabilities:
   ```bash
   safety check
   ```

4. Run the tests:
   ```bash
   pytest -q
   ```
