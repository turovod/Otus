from selenium import webdriver

from OpenCart.Drivers import get_driver_path

chrome = webdriver.Chrome(executable_path=get_driver_path())
chrome.get("http://localhost:8888/")

frames = chrome.find_elements_by_css_selector("iframe")

# chrome.switch_to.frame(frames[0])
# chrome.find_element_by_css_selector("button.header2__auth").click()
# chrome.switch_to.default_content()
# chrome.find_element_by_link_text("here3").click()

chrome.switch_to.frame("avito")
chrome.find_element_by_link_text("Личные вещи").click()
chrome.switch_to.default_content()
chrome.find_element_by_link_text("here2").click()

# chrome.switch_to.frame(frames[1])
# chrome.find_element_by_css_selector("#cn-accept-cookie").click()
# chrome.switch_to.default_content()
# chrome.find_element_by_link_text("here1").click()
