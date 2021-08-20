import pytest
from selenium import webdriver


def get_driver_path():
    return str(__file__).replace('conftest.py', '') + 'Drivers/chromedriver'


@pytest.fixture(scope='session')
def setup_teardown():
    driver_path = get_driver_path()
    print('==========', driver_path)
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get('http://localhost:8888/opencart3/upload/')
    driver.fullscreen_window()
    yield driver
    driver.close()
