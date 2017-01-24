from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import time
import pytest
'''

@author: Kirill Markidonov

'''

@pytest.fixture
def remote_driver(request):
    driver = webdriver.Remote("http://192.168.0.113:4444/wd/hub", desired_capabilities={"browserName": "internet explorer"})
    print(driver.capabilities)
    request.addfinalizer(driver.quit)
    return driver


def test_f_n(remote_driver):
    # Please check the PORT!!!!!
    remote_driver.get("http://google.com")

    time.sleep(10)
