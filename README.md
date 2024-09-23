# System Resource Monitor with Flask and psutil

This is a simple Python Flask application that monitors and displays the CPU and memory usage of the server using the `psutil` library. The application runs on port 5000 and provides a real-time snapshot of system resources.

## Features

- Real-time CPU usage monitoring
- Real-time memory usage monitoring
- Lightweight and easy to set up

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/system-monitor-flask.git
    cd system-monitor-flask
    ```

2. **Install the dependencies:**

    Ensure you have `pip` installed, then run:

    ```bash
    pip3 install -r requirements.txt
    ```

## Usage

1. **Run the Flask application:**

    ```bash
    python3 app.py
    ```

2. **Open the application in your web browser:**

    Navigate to [http://localhost:5000/](http://localhost:5000/) to see the current CPU and memory usage of the server.

## Example Output

Once you open the application in a browser, you'll see the current CPU and memory usage, updated each time the page is refreshed.