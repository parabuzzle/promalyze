from promalyze.timeseries import TimeSeries


class TestTimeSeries:

    @staticmethod
    def meta():
        return {
            '__name__': 'test_metric',
            'tag1': 'value1'
        }

    @staticmethod
    def ts_data():
        return [
            [1234, 1],
            [5678, 2]
        ]


    def setup(self):
        self.timeseries = TimeSeries(self.meta(), self.ts_data())

    def teardown(self):
        self.timeseries = None

    def test_timestamps(self):
        assert self.timeseries.timestamps() == [1234, 5678]

    def test_values(self):
        assert self.timeseries.values() == [1,2]

    def test_as_json(self):
        assert self.timeseries.as_json()['values'] == self.ts_data()
        assert self.timeseries.as_json()['name'] == 'test_metric'

    def test_as_pandas_dataframe(self):
        assert str(type(self.timeseries.as_pandas_dataframe())) == "<class 'pandas.core.frame.DataFrame'>"