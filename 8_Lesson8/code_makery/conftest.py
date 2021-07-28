import time

import pytest
from selenium import webdriver


@pytest.fixture
def set_up(request):
    webdriver_path = __file__.replace('conftest.py', '') + 'drivers/chromedriver'
    wd = webdriver.Chrome(executable_path=webdriver_path)
    wd.get('https://www.html5rocks.com/ru/tutorials/dnd/basics//')

    wd.fullscreen_window()
    request.addfinalizer(wd.close)
    return wd
