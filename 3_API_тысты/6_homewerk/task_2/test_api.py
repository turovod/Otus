def test_api(api_fix):
    print(api_fix.get().json()[0])


def test_api(api_fix):
    res = api_fix.get().json()[0]
    assert res['id'] == 8041