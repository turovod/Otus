from selenium.common.exceptions import StaleElementReferenceException

# Исключение, сообщает нам что такой элемент больше не является частью DOM дерева 
# (самый распространненый вариант - произошло обновление страницы)
