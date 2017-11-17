Promalyze
===

The library to get data out of Prometheus to analyze.

# Install

```python
pip install promalyze
```

# Usage

```python
from promalyze import Client

client = Client('http://localhost:9090')

ts_data = client.range_query('go_gc_duration_seconds') # returns PrometheusData object

ts = ts_data.timeseries[0] # returns a TimeSeries object

json_data = ts.as_json()

dataframe = ts.as_pandas_dataframe()

```
