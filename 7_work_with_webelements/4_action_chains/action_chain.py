from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.alert import Alert


chrome = webdriver.Chrome()
actions = ActionChains(chrome)
chrome.c

# chrome.get("https://sketch.io/sketchpad/en/")
# area = chrome.find_element_by_tag_name("sketch-scrollarea")
# actions.move_to_element_with_offset(area, 100, 100).click_and_hold().move_by_offset(150, 150).perform()

for i in dir(actions):
    Alert.accept()
    print(i)
