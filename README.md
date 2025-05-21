# Demo: Dockerized Flask System Monitor

This project demonstrates a simple Flask web application that monitors the CPU and memory usage of the Docker container it's running in. It provides real-time usage statistics and alerts if either CPU or memory utilization exceeds 80%.

## Features

- Displays current CPU usage percentage of the container
- Displays current memory usage percentage of the container
- Displays current disk usage percentage of the container's root filesystem
- Displays network statistics (bytes sent and received)
- Displays historical CPU and memory usage over the last ~5 minutes as line graphs.
- Alerts if CPU, memory, or disk usage exceeds a configurable threshold (default 80%).
- Configurable alert threshold via `config.json`.

## Building and Running with Docker

### 1. Build the Docker image

In the project directory, run:

```bash
docker build -t demo-dockerized-flasksystemmonitor .
```

### 2. Run the Docker container

After building, run the container with:

```bash
docker run -d -p 5000:5000 demo-dockerized-flasksystemmonitor
```

This starts the Flask app inside a Docker container, accessible on port 5000.

## Usage

- Access the application at `http://localhost:5000`
- The page displays current CPU, memory, and disk usage of the container, network statistics, and historical graphs for CPU and memory usage, providing a trend view of resource consumption.
- An alert message appears if CPU, memory, or disk usage exceeds the configured threshold.

## Configuration

The alert threshold for CPU, memory, and disk usage can be configured by creating or editing a `config.json` file in the root directory of the project.

The structure of `config.json` should be as follows:

```json
{
  "alert_threshold_percent": 80
}
```

- `alert_threshold_percent`: This is the value (0-100) at which an alert will be triggered if CPU, memory, or disk usage exceeds this percentage.

If `config.json` is missing, malformed, or the `alert_threshold_percent` key is not found, a default threshold of 80% will be used.
