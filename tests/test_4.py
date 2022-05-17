from selenium.webdriver.common.by import By

from utils import calc_math_task, custom_assert, get_num_from_alert_text, get_alert_text


def test_4(browser, answer):
    browser.get("http://suninjuly.github.io/execute_script.html")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc_math_task(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    custom_assert(get_num_from_alert_text(get_alert_text(browser)) == answer, __file__)
