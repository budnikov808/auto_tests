from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utils import custom_assert, get_num_from_alert_text, get_alert_text


def calc(x1, x2):
    return str(int(x1)+int(x2))


def test_3(browser, answer):
    browser.get("http://suninjuly.github.io/selects1.html")

    x1_element = browser.find_element(By.ID, "num1")
    x1 = x1_element.text

    x2_element = browser.find_element(By.ID, "num2")
    x2 = x2_element.text

    y = calc(x1, x2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)  # ищем элемент с текстом "Python"

    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    button.click()

    custom_assert(get_num_from_alert_text(get_alert_text(browser)) == answer, __file__)
