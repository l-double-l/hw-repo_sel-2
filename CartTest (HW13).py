from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    wd.delete_all_cookies()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_prices_and_names(driver):
    # Please check the PORT!!!!!
    driver.get("http://localhost:8080/litecart")
    wait = WebDriverWait(driver, 5)

    for indx in range(1, 4):
        driver.find_element_by_css_selector("#box-most-popular img").click()
        driver.find_element_by_name("add_cart_product").click()
        assert wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), "{}".format(indx)))

        driver.back()

    driver.find_element_by_css_selector("#cart .link").click()

    products = driver.find_elements_by_name("remove_cart_item")
    for i in range(len(products)):
        product = driver.find_element_by_name("remove_cart_item")
        product.click()
        wait.until(EC.staleness_of(product))

    confirm_text = wait.until(EC.presence_of_element_located((By.TAG_NAME, "em")))
    assert confirm_text.text == "There are no items in your cart."

