"""
Utility methods
"""
import time


def time_to_epoch(t):
    """
    A simple utility to turn a datetime object into a timestamp
    :param t: datetime object
    :return: integer
    """
    return int(time.mktime(t.timetuple()))