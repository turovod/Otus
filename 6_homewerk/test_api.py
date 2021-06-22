import pytest
import requests


# def test_api(api_client):
#     response = api_client.get()
#
#     print(response.json())
@pytest.mark.parametrize('path', ['/list/all', '/image/random'])
def test_api(api_client, path):
    res = requests.get(url=api_client + path)

    print(res.json())

@pytest.mark.parametrize('path', ['/list/all', '/image/random'])
def test_api2(path):
    res = requests.get(url='https://dog.ceo/api/breeds' + path)
    print(res.json())

