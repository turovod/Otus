def test_api_1(api_fixt):
    res = api_fixt.get(path='posts/1')

    print(res.json())


def test_api_2(api_fixt):
    js = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1,
    }
    headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }
    pos = api_fixt.post(path='posts', json=js)

    assert pos.json()['title'] == 'foo'
