from selenium import webdriver

from tests.test_1 import test_1
from tests.test_2 import test_2
from tests.test_3 import test_3
from tests.test_4 import test_4
from tests.test_5 import test_5
from tests.test_6 import test_6
from tests.test_7 import test_7
from utils import exec_test


browser = webdriver.Firefox()

exec_test(test_1, browser, '28.8778')
exec_test(test_2, browser, '29.0123')
exec_test(test_3, browser, '28.9233')
exec_test(test_4, browser, '28.9246')
exec_test(test_5, browser, '28.9255')
exec_test(test_6, browser, '28.9255')
exec_test(test_7, browser, '28.9690')

browser.quit()
