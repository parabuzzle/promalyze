"""
Client module to fetch data from a Prometheus server
"""

from datetime import datetime, timedelta
import requests
from promalyze.timeseries import TimeSeries
from promalyze.vector import Vector
from promalyze.prometheus_data import PrometheusData
from promalyze.utils import time_to_epoch


class Client(object):
    """
    Client object provides methods for fetching data from a Prometheus server
    """

    def __init__(self, prometheus_url="http://localhost:9090"):
        self.prometheus_url = prometheus_url if prometheus_url[-1:] != '/' else prometheus_url[:-1]

    def instant_query(self, metric, params=None):
        """
        Returns a PrometheusData object loaded with results from a query call
        :param metric: string of the metric query
        :param params: dict of additional parameters to send to the API
        :return: PrometheusData
        """
        if params is None:
            params = {}

        params['query'] = metric
        response = self._fetch('query', params)
        data = self._extract_data(response)
        return self._handle_results(data)

    def range_query(self, metric, start=None, end=None, step=60, params=None):
        """
        Returns a PrometheusData object loaded with results from a query_range call
        :param metric: string of the metric query
        :param start: an epoch time for the earliest data point in the range -- default is 24 hours ago
        :param end: an epoch time for the latest data point in the range -- default is the current time
        :param step: the step size
        :param params: additional params to send to the API
        :return: PrometheusData
        """
        if params is None:
            params = {}

        params['query'] = metric
        params['step'] = step

        if start is None:
            start = time_to_epoch((datetime.now() - timedelta(days=1)))

        if end is None:
            end = time_to_epoch(datetime.now())

        params['start'] = start
        params['end'] = end

        response = self._fetch('query_range', params)
        data = self._extract_data(response)
        return self._handle_results(data)

    @staticmethod
    def _api_base():
        return "/api/v1/"

    def _full_url(self, endpoint):
        return self.prometheus_url + self._api_base() + endpoint

    def _fetch(self, resource, params=None):
        if params is None:
            params = {}

        res = requests.get(self._full_url(resource), params)
        return res.json()

    @staticmethod
    def _extract_data(jsondata):
        if jsondata['status'] != 'success':
            data = []
        else:
            data = jsondata['data']
        return data

    @staticmethod
    def _handle_results(data):
        results = PrometheusData()

        if data['resultType'] == 'vector':
            for d in data['result']:
                results.vectors.append(Vector(d))

        if data['resultType'] == 'matrix':
            for d in data['result']:
                ts = TimeSeries(d['metric'], d['values'])
                results.timeseries.append(ts)

        return results
