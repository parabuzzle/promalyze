from promalyze.prometheus_data import PrometheusData
from promalyze.vector import Vector
from promalyze.timeseries import TimeSeries


class TestPrometheusData:

    @staticmethod
    def meta():
        return {
            '__name__': 'test_metric',
            'tag1': 'value1'
        }

    @staticmethod
    def value():
        return [1234, 1]

    def mocktimeseries(self):
        return TimeSeries(meta=self.meta(), ts=[[1234,1], [5678,2]])

    def mockvector(self):
        return Vector({'metric': self.meta(), 'value': self.value()})

    def setup(self):
        self.pdata = PrometheusData()

    def teardown(self):
        self.pdata = None

    def test_vectors(self):
        assert len(self.pdata.vectors) == 0
        assert self.pdata.has_vectors() is False

        self.pdata.vectors.append(self.mockvector())
        assert len(self.pdata.vectors) == 1
        assert self.pdata.has_vectors() is True

    def test_timeseries(self):
        assert len(self.pdata.timeseries) == 0
        assert self.pdata.has_timeseries() is False

        self.pdata.timeseries.append(self.mocktimeseries())
        assert len(self.pdata.timeseries) == 1
        assert self.pdata.has_timeseries() is True

    def test_as_json(self):
        self.pdata.vectors.append(self.mockvector())
        self.pdata.timeseries.append(self.mocktimeseries())

        js = self.pdata.as_json()
        assert len(js['vectors']) == 1
        assert len(js['timeseries']) == 1

        assert js['timeseries'][0]['values'] == [[1234,1], [5678,2]]
        assert js['vectors'][0]['value'] == 1
