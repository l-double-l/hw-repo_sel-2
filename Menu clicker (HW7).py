from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

import pytest
'''

@author: Kirill Markidonov

'''


@pytest.fixture
def driver(request):
    binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
    wd = webdriver.Firefox(firefox_binary=binary)
    wd.implicitly_wait(10)
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_menu(driver):
    # Please check the PORT!!!!!
    driver.get("http://localhost:8080/litecart/admin/login.php")

    WebDriverWait(driver, 10).until(EC.title_contains("My Store"))

    login_box = driver.find_element_by_name("username")
    login_box.send_keys("admin")

    password_box = driver.find_element_by_name("password")
    password_box.send_keys("admin")

    login_btn = driver.find_element_by_name("login")
    login_btn.click()

    main_menu = driver.find_elements_by_css_selector("ul li#app-")

    menu_index = 0

    for data in main_menu:
        menu_index += 1
        time.sleep(1)
        wait = WebDriverWait(driver, 5) # seconds
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul li#app-:nth-child({}) .name".format(menu_index))))
        print("waited")
        element.click()
        print("clicked")


