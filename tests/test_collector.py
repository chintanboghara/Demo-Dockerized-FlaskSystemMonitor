import time
from monitor.collector import Collector

def test_history_length():
    col = Collector(history_length=3)
    time.sleep(1.2)
    hist = col.get_current()['cpu']
    assert len(hist) <= 3
