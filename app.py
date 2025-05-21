import psutil
from flask import Flask, render_template
import threading
import time
import collections
import json
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Global variable for alert threshold
ALERT_THRESHOLD = 80 # Default value

def load_config():
    """Loads alert threshold from config.json."""
    global ALERT_THRESHOLD
    config_path = 'config.json'
    try:
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config_data = json.load(f)
                ALERT_THRESHOLD = config_data.get('alert_threshold_percent', ALERT_THRESHOLD)
                logging.info(f"Loaded alert threshold from {config_path}: {ALERT_THRESHOLD}%")
        else:
            logging.warning(f"{config_path} not found. Using default alert threshold: {ALERT_THRESHOLD}%")
    except json.JSONDecodeError:
        logging.warning(f"Error decoding {config_path}. Using default alert threshold: {ALERT_THRESHOLD}%")
    except KeyError:
        logging.warning(f"'alert_threshold_percent' key not found in {config_path}. Using default alert threshold: {ALERT_THRESHOLD}%")
    except Exception as e:
        logging.error(f"An unexpected error occurred while loading {config_path}: {e}. Using default alert threshold: {ALERT_THRESHOLD}%")

# Load configuration at startup
load_config()

# Global Data Stores for historical data
cpu_history = collections.deque(maxlen=60)
mem_history = collections.deque(maxlen=60)
timestamp_history = collections.deque(maxlen=60)

def collect_system_metrics():
    """Collects and stores system metrics (CPU, Memory) at regular intervals."""
    while True:
        cpu_percent = psutil.cpu_percent()
        mem_percent = psutil.virtual_memory().percent
        current_time = time.strftime('%H:%M:%S')

        cpu_history.append(cpu_percent)
        mem_history.append(mem_percent)
        timestamp_history.append(current_time)
        
        time.sleep(5) # Collect data every 5 seconds

# Start the background thread for data collection
metrics_thread = threading.Thread(target=collect_system_metrics)
metrics_thread.daemon = True
metrics_thread.start()

@app.route("/")
def index():
    # Current values for gauges
    current_cpu_percent = psutil.cpu_percent()
    current_mem_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    
    message = None
    if current_cpu_percent > ALERT_THRESHOLD or current_mem_percent > ALERT_THRESHOLD or disk_percent > ALERT_THRESHOLD:
        message = f"High CPU, memory, or disk utilization detected (Threshold: {ALERT_THRESHOLD}%)!"

    # Network statistics
    net_io = psutil.net_io_counters()
    bytes_sent = bytes_to_readable(net_io.bytes_sent)
    bytes_recv = bytes_to_readable(net_io.bytes_recv)

    return render_template("index.html", 
                           cpu_percent=current_cpu_percent, 
                           mem_percent=current_mem_percent, 
                           disk_percent=disk_percent, 
                           message=message, 
                           bytes_sent_readable=bytes_sent, 
                           bytes_recv_readable=bytes_recv,
                           cpu_history=list(cpu_history),
                           mem_history=list(mem_history),
                           timestamp_history=list(timestamp_history))

def bytes_to_readable(b):
    """Converts bytes to a human-readable format (KB, MB, GB)."""
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if b < 1024:
            return f"{b:.2f}{unit}B"
        b /= 1024
    return f"{b:.2f}PB"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
