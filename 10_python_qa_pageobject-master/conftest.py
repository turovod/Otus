import time

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome",
                     help="choose your browser")
    parser.addoption("--url", "-U", action="store",
                     default="http://localhost:8888/opencart3/upload/", help="choose url")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request, url):
    """ Фикстура инициализации браузера """
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(
            executable_path='/Users/s.loginov/Desktop/Otus/10_python_qa_pageobject-master/Drivers/chromedriver')
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")
    driver.implicitly_wait(5)

    def fin():
        time.sleep(5)
        driver.close()
    request.addfinalizer(fin)

    def open(path=""):
        return driver.get(url + path)

    driver.open = open
    driver.open()
    return driver
