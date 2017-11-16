import time
from datetime import datetime
from promalyze.utils import time_to_epoch


def test_time_to_epoch():
    t = datetime.now()
    assert time_to_epoch(t) == int(time.mktime(t.timetuple()))