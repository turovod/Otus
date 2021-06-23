import pytest
import requests


class APIClient():
    def __init__(self, path):
        self.base_url = 'https://api.openbrewerydb.org/'
        self.path = path

    def get(self):
        return requests.get(url=self.base_url + self.path)


@pytest.fixture(scope='session',
                params=['breweries?by_city=san_diego', 'breweries?by_dist=38.8977,77.0365'])
def api_fix(request):
    return APIClient(request.param)
