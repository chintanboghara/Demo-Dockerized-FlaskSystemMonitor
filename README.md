# Dockerized Flask System Monitor

A lightweight Flask web application that runs inside a Docker container and exposes real‑time CPU, memory, disk, and network usage metrics (with 5‑minute history) along with threshold‑based alerts. It’s designed to give you quick visibility into the container’s own resource utilization without external monitoring agents.

## Features

- **Real‑time metrics**: CPU, memory, disk, and network usage sampled every second.
- **Rolling history**: 5‑minute history for each metric, stored in a fixed‑size in‑memory buffer.
- **Threshold alerts**: Highlight when a metric exceeds a configured alert threshold.
- **JSON API**:  
  - `/api/metrics` returns all metrics and histories as JSON.  
  - `/health` for liveness checks.
- **Web UI**:  
  - Single‑page dashboard rendered via Chart.js.  
  - Dynamic coloring when thresholds are breached.
- **Production‑ready Docker**:  
  - Multi‑stage build for minimal image size.  
  - Runs as non‑root user.  
  - Built‑in HEALTHCHECK.  
  - Gunicorn WSGI server.

## Prerequisites

- Docker ≥ 20.10  
- Python ≥ 3.11 (for local development)  
- `make` (optional, for convenience)  

## Quickstart

1. **Clone the repo**  
   ```bash
   git clone https://github.com/chintanboghara/Dockerized-FlaskSystemMonitor.git
   cd Dockerized-FlaskSystemMonitor
   ````

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

## Configuration

### `config.json`

```json
{
  "alert_threshold": 80
}
```

* `alert_threshold` (integer, 1–99): default percentage above which metrics are highlighted.

### Environment Variables

You can override or supplement `config.json` via a `.env` file:

```dotenv
FLASK_ENV=production
ALERT_THRESHOLD=75
```

* `FLASK_ENV`: Flask environment (`development` or `production`).
* `ALERT_THRESHOLD`: overrides `alert_threshold` from `config.json`.

## API Endpoints

| Path           | Method | Description                                     |
| -------------- | ------ | ----------------------------------------------- |
| `/health`      | GET    | Returns `{ "status": "ok" }` for health checks. |
| `/api/metrics` | GET    | Returns JSON with current + historical metrics: |
|                |        | \`\`\`json                                      |
|                |        | {                                               |
|                |        | "cpu": \[ ... ],                                |
|                |        | "mem": \[ ... ],                                |
|                |        | "disk": \[ ... ],                               |
|                |        | "net": \[ ... ]                                 |
|                |        | }                                               |
|                |        | \`\`\`                                          |

## Running Tests & CI

This project uses **pytest**, **flake8**, and **safety**:

```bash
pip install --upgrade pip
pip install -r requirements.txt pytest flake8 safety
flake8 .
safety check
pytest -q
```
