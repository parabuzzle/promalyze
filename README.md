Promalyze
===

The library to get data out of Prometheus to analyze.

# Install

```bash
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

# Development

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
nosetests
```

### With Coverage

```bash
nosetests --with-coverage --cover-package=promalyze
```

# Contribute

  1. Fork it
  1. Create your feature branch (git checkout -b my-new-feature)
  1. Commit your changes (git commit -am 'Add some feature')
  1. Push to the branch (git push origin my-new-feature)
  1. Create new Pull Request