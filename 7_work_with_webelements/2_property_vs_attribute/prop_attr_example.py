from selenium import webdriver

firefox = webdriver.Firefox()
firefox.implicitly_wait(10)
firefox.get("https://yandex.ru")

home_tabs = firefox.find_element_by_css_selector(".home-tabs")
search_input = firefox.find_element_by_css_selector("input#text")

html = home_tabs.get_property("innerHTML")
# print(html)

attr = home_tabs.get_attribute("data-bem")
# print(attr)

css = home_tabs.value_of_css_property("margin-bottom")
# print(css)

firefox.close()
