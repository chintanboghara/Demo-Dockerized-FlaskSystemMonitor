from flask import Flask, jsonify, render_template
from monitor.collector import Collector
from monitor.config import ALERT_THRESHOLD

import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

collector = Collector(history_length=300)

@app.route('/health')
def health():
    return jsonify(status='ok'), 200

@app.route('/api/metrics')
def metrics():
    try:
        return jsonify(collector.get_current()), 200
    except Exception as e:
        app.logger.error(f"Metrics error: {e}")
        return jsonify(error=str(e)), 500

@app.route('/')
def index():
    return render_template('index.html', threshold=ALERT_THRESHOLD)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
