from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import os
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


def test_logs(driver):
    driver.get("http://localhost:8080/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    products = driver.find_elements_by_css_selector(".dataTable td:nth-child(3) img + a")
    for product_index in range(0, len(products)):
        products[product_index].click()
        assert driver.get_log("browser") == []
        driver.back()
        products = driver.find_elements_by_css_selector(".dataTable td:nth-child(3) img + a")