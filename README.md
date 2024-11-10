
# Demo-Dockerized-FlaskSystemMonitor

This is a simple Flask application that monitors the CPU and memory usage of the system. It provides an alert message if either CPU or memory utilization exceeds 80%.

## Running with Docker

### 1. Build the Docker image

In the project directory, build the Docker image using:

```bash
docker build -t demo-dockerized-flasksystemmonitor .
```

### 2. Run the Docker container

Run the Docker container with the following command:

```bash
docker run -d -p 5000:5000 demo-dockerized-flasksystemmonitor
```

## Usage

- The app displays the current CPU and memory usage.
- If either the CPU or memory utilization exceeds 80%, an alert message will be displayed.
