from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

import pytest
'''

@author: Kirill Markidonov

'''

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(3)
    wd.maximize_window()

    #############################################################
    # Please check the PORT!!!!!
    wd.get("http://localhost:8080/litecart/admin/login.php")

    login_box = wd.find_element_by_name("username")
    login_box.send_keys("admin")

    password_box = wd.find_element_by_name("password")
    password_box.send_keys("admin")

    login_btn = wd.find_element_by_name("login")
    login_btn.click()
    #############################################################

    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_add_new_product(driver):

    driver.find_element_by_css_selector("ul li#app-:nth-child(2) .name").click()
    driver.find_element_by_css_selector(".button:last-child").click()
    driver.find_element_by_css_selector("[name=status]").click()
    driver.find_element_by_css_selector("[name=name\[en\]]").send_keys("Test")
    driver.find_element_by_css_selector("[name=code").send_keys("111111")
    driver.find_element_by_css_selector("[name=quantity").clear()
    driver.find_element_by_css_selector("[name=quantity").send_keys("3")
    driver.find_element_by_css_selector("[type=file").send_keys("C:\\test.png")
    driver.find_element_by_css_selector("div.tabs li:nth-child(4)").click()

    driver.find_element_by_css_selector("[name=purchase_price").clear()
    driver.find_element_by_css_selector("[name=purchase_price").send_keys("3")

    driver.find_element_by_css_selector("[name=save]").click()

def test_check_new_product(driver):
    driver.find_element_by_css_selector("ul li#app-:nth-child(2) .name").click()
    assert driver.find_elements_by_css_selector(".dataTable td:nth-child(3) a")[-1].text == "Test"