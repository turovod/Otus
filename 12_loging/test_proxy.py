import time

from browsermobproxy import Server,  Client
import pytest
import urllib.parse
from selenium import webdriver
from OpenCart.Drivers import get_driver_path

# Реализация с опциями вебдрайвера
# server = Server(r"/Users/s.loginov/Desktop/Otus/12_loging/browsermob-proxy-2.1.4/bin/browsermob-proxy")
# server.start()
# client = Client("localhost:8080")
# client.port
# # proxy = server.create_proxy()
# client.new_har('otus')
# client.har


# @pytest.fixture
# def chrome_browser(request):
#
#     chrome_options = webdriver.ChromeOptions()
#     url = urllib.parse.urlparse(client.proxy).path
#     chrome_options.add_argument('--proxy-server=%s' % url)
#     driver_path = get_driver_path()
#     driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
#     request.addfinalizer(driver.quit)
#     return driver

client: Client = None


# Реализация с простым формированием прокси
@pytest.fixture
def chrome_browser(request):
    start_proxy()
    driver_path = get_driver_path()
    driver = webdriver.Chrome(executable_path=driver_path)
    request.addfinalizer(driver.quit)
    return driver


def start_proxy():
    global client
    server = Server(
        r"/Users/s.loginov/Desktop/Otus/12_loging/browsermob-proxy-2.1.4/bin/browsermob-proxy")
    server.start()
    client = Client("localhost:8080")
    client.new_har('otus')


def test_proxy(chrome_browser):

    chrome_browser.get('https://otus.ru/')
    # Теперь в браузере заходим на урл http://localhost:8080/proxy/8085/har
    time.sleep(20)
    print(' ')
    print(client.port)
    print(client.har)
