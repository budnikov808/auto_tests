from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc(x1, x2):
    return str(int(x1)+int(x2))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1_element = browser.find_element_by_id("num1")
    x1 = x1_element.text

    x2_element = browser.find_element_by_id("num2")
    x2 = x2_element.text

    y = calc(x1, x2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)  # ищем элемент с текстом "Python"

    button = browser.find_element_by_css_selector("body > div > form > button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла