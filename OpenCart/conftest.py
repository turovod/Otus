import pytest
from selenium import webdriver
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
import logging

logger = None


@pytest.fixture(scope='session')
def setup_teardown():
    global logger
    logger = set_logger()
    driver_path = get_driver_path()
    driver = EventFiringWebDriver(webdriver.Chrome(executable_path=driver_path), MyListener())
    driver.get('http://localhost:8888/opencart3/upload/')
    driver.fullscreen_window()
    yield driver, logger
    # browser log
    for l in driver.get_log('browser'):
        with open('../browser_log', 'a', encoding='utf-8') as log:
            log.write(l)

    driver.close()


class MyListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        global logger
        logger.info(f'Find element by {by}, value {value}')

    def on_exception(self, exception, driver: webdriver):
        driver.save_screenshot('exception.png')
        logger.critical(f'Exception {exception}')


def set_logger():
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.FileHandler('../pytest.log')
    stream_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def get_driver_path():
    return str(__file__).replace('conftest.py', '') + 'Drivers/chromedriver'
