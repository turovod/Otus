import pytest
import requests


class APIClient:
    def __init__(self, base_url, param):
        self.base_url = base_url
        self.param = param
        
    def get(self, path=None, params=None, **kwargs):
        return requests.get(self.base_url + path, params, **kwargs)

    def post(self, path=None, data=None, json=None, **kwargs):
        return requests.post(self.base_url + path, data, json, **kwargs)


@pytest.fixture(scope='session', params=[1, 2])
def api_fixt(request):
    return APIClient('https://jsonplaceholder.typicode.com/', request.param)