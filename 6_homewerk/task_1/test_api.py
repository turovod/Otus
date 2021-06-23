import pytest
import requests


# def test_api(api_client):
#     response = api_client.get()
#
#     print(response.json())
# @pytest.mark.parametrize('path', ['/list/all', '/image/random'])
def test_api(api_client, path=None):
    res = requests.get(url=api_client[0] + api_client[1])
    print(res.json())

    assert "affenpinscher" in list(list(res.json().values())[0].keys())[0], 'hera vam'


@pytest.mark.parametrize('path', ['/list/all', '/image/random'])
def test_api2(path):
    res = requests.get(url='https://dog.ceo/api/breeds' + path)
    print(res.json())
