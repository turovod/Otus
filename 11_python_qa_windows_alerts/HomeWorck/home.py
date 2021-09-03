import time

import pytest
from selenium import webdriver
from OpenCart.Drivers import get_driver_path


@pytest.fixture
def fix():
    dw = webdriver.Chrome(executable_path=get_driver_path())
    yield dw
    time.sleep(5)
    dw.close()


def test_home(fix):
    dw = fix
    home_win = dw.current_window_handle
    dw.execute_script('window.open();')
    new_window = dw.window_handles
    dw.switch_to.window(new_window[1])
    dw.get('http://turovod.ru/')
    dw.switch_to.window(home_win)
    dw.get('http://demo.guru99.com/test/upload/')