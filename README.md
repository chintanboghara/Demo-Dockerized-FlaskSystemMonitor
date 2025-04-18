# Demo: Dockerized Flask System Monitor

This project demonstrates a simple Flask web application that monitors the CPU and memory usage of the Docker container it's running in. It provides real-time usage statistics and alerts if either CPU or memory utilization exceeds 80%.

## Features

- Displays current CPU usage percentage of the container
- Displays current memory usage percentage of the container
- Alerts if CPU or memory usage exceeds 80%

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
- The page displays current CPU and memory usage of the container
- An alert message appears if either usage exceeds 80%
