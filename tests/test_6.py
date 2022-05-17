from selenium.webdriver.common.by import By

from utils import calc_math_task, custom_assert, get_num_from_alert_text, get_alert_text


def test_6(browser, answer):
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc_math_task(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
    button.click()

    custom_assert(get_num_from_alert_text(get_alert_text(browser)) == answer, __file__)
