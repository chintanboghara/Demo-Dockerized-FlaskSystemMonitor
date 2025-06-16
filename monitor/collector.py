import psutil
from collections import deque
import threading, time

class Collector:
    def __init__(self, history_length=300):
        self.history = {
            name: deque(maxlen=history_length)
            for name in ('cpu', 'mem', 'disk', 'net')
        }
        self.lock = threading.Lock()
        threading.Thread(target=self._background, daemon=True).start()

    def _collect(self):
        net = psutil.net_io_counters()
        return {
            'cpu': psutil.cpu_percent(),
            'mem': psutil.virtual_memory().percent,
            'disk': psutil.disk_usage('/').percent,
            'net': net.bytes_sent + net.bytes_recv,
        }

    def _background(self):
        while True:
            try:
                point = self._collect()
                with self.lock:
                    for k, v in point.items():
                        self.history[k].append(v)
            except Exception:
                pass
            time.sleep(1)

    def get_current(self):
        with self.lock:
            return {k: list(v) for k, v in self.history.items()}
