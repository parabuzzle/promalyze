"""
Prometheus Data handler object
"""

class PrometheusData(object):
    """
    PrometheusData object handles vectors and matrix data in unified way
    """

    def __init__(self):
        self.vectors = []
        self.timeseries = []

    def has_vectors(self):
        """
        returns True if there are vectors present in this object
        :return: Boolean
        """
        return len(self.vectors) != 0

    def has_timeseries(self):
        """
        returns True if there are timeseries' present in this object
        :return: Boolean
        """
        return len(self.timeseries) != 0

    def as_json(self):
        """
        Returns the data in this object as a dict
        :return: dict
        """
        data = {}

        if self.has_vectors():
            data['vectors'] = []
            for vector in self.vectors:
                data['vectors'].append(vector.as_json())

        if self.has_timeseries():
            data['timeseries'] = []
            for ts in self.timeseries:
                data['timeseries'].append(ts.as_json())
        return data
