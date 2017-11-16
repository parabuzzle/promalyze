"""
Time Series handling
"""

class TimeSeries(object):
    """
    TimeSeries object handles matrix objects from Prometheus
    """

    def __init__(self, meta, ts):
        self.ts = ts
        self.name = meta['__name__']
        del meta['__name__']
        self.metadata = meta

    def timestamps(self):
        """
        returns all the timestamps as a list
        :return: list
        """
        return [x[0] for x in self.ts]

    def values(self):
        """
        returns all the values as a list
        :return: list
        """
        return [x[1] for x in self.ts]

    def as_json(self):
        """
        transforms the data for this object into a dict
        :return: dict
        """
        return {
            'name': self.name,
            'metadata': self.metadata,
            'values': self.ts
        }

    def as_pandas_dataframe(self):
        """
        transforms the data for this object into a pandas dataframe
        :return: pandas.DataFrame
        """
        import pandas as pd
        return pd.DataFrame(data=self.values(), index=self.timestamps(), columns=['values'])