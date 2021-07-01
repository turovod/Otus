import requests


def test_ya(url_fixt):
    res = requests.get(url_fixt)
    print(res.text)