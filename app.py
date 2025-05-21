import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    message = None
    if cpu_percent > 80 or mem_percent > 80 or disk_percent > 80:
        message = "High CPU, memory, or disk utilization detected!"

    # Network statistics
    net_io = psutil.net_io_counters()
    bytes_sent = bytes_to_readable(net_io.bytes_sent)
    bytes_recv = bytes_to_readable(net_io.bytes_recv)

    return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, disk_percent=disk_percent, message=message, bytes_sent_readable=bytes_sent, bytes_recv_readable=bytes_recv)

def bytes_to_readable(b):
    """Converts bytes to a human-readable format (KB, MB, GB)."""
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if b < 1024:
            return f"{b:.2f}{unit}B"
        b /= 1024
    return f"{b:.2f}PB"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
