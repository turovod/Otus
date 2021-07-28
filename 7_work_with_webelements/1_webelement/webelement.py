from selenium import webdriver

firefox = webdriver.Firefox()
firefox.implicitly_wait(10)
firefox.get("https://yandex.ru")

home_tabs = firefox.find_element_by_css_selector(".home-tabs")
search_input = firefox.find_element_by_css_selector("input#text")

for i in dir(home_tabs):
  print(i)

firefox.close()
