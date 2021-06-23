import requests


def api():
    path = '/list/all'
    res = requests.get(url='https://dog.ceo/api/breeds' + path)
    return res


print(type(list(list(api().json().values())[0].keys())[0]))