import os

from selenium.webdriver.common.by import By

from utils import custom_assert, get_num_from_alert_text, get_alert_text


def test_5(browser, answer):
    browser.get("http://suninjuly.github.io/file_input.html")

    input1 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(2)")
    input1.send_keys("name")

    input2 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(4)")
    input2.send_keys("last name")

    input3 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(6)")
    input3.send_keys("name@name")

    element = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    button.click()

    custom_assert(get_num_from_alert_text(get_alert_text(browser)) == answer, __file__)
