import pytest
import requests

import appmanager


class ApiClient:
    def __init__(self, path):
        self.app = appmanager.AppManager()
        self.base_url = self.app.base_url
        self.path = path

    def post(self, params=None, headers=None, json=None):
        url = self.base_url + self.path
        return requests.post(url, params=params, json=json, headers=headers)

    def get(self, params=None, headers=None):
        url = self.base_url + self.path
        return requests.get(url, params=params, headers=headers)


def pytest_addoptions(parser):
    parser.addoption(
        "--path",
        action="store",
        default="/list/all",
        help="This is request path"
    )


@pytest.fixture(scope='session', params='https://dog.ceo/api/breeds')
def api_client(request):
    return request.param
