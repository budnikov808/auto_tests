import math
import os
import re
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


def calc_math_task(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def get_num_from_alert_text(text):
    return re.findall("\d{1,5}\.\d{14}", text)[0][:-10]


def custom_assert(boolean, file):
    if boolean:
        print(f'{os.path.basename(file)} passed')
    else:
        print(f'{os.path.basename(file)} failed')


def exec_test(test, browser, answer):
    try:
        test(browser, answer)
    except Exception as e:
        print(f'{test} failed due to exception: "{e}"')


def get_alert_text(browser):
    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()
    return alert_text
