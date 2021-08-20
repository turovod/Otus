import time

import pytest
from selenium import webdriver

wd = None


@pytest.fixture(scope='session')
def fixture_tests(request):
    global wd
    browser = request.config.getoption("--wb")
    wait = request.config.getoption("--wt")
    if browser == 'Ch':
        wd = webdriver.Chrome(executable_path=get_wd_path())
        wd.get(url='http://localhost:8888/opencart3/upload/')
        wd.implicitly_wait(wait)
        wd.fullscreen_window()
        time.sleep(1)
    return wd


@pytest.fixture(autouse=True)
def final(request):
    request.addfinalizer(wd.close)


def get_wd_path():
    return __file__.replace('conftest.py', '') + 'drivers/chromedriver'


def pytest_addoption(parser):
    """PyTest method for adding custom console parameters"""

    parser.addoption("--wb", action="store", default='Ch', type=str,
                     help="Set browser")

    parser.addoption("--wt", action="store", default='10', type=str,
                     help="Set wait")
