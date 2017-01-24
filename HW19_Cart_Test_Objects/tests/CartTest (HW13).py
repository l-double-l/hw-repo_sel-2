from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from HW19_Cart_Test_Objects.app.application import Application

import os
import pytest
'''

@author: Kirill Markidonov

'''

@pytest.fixture
def app(request):
    app = Application()
    request.addfinalizer(app.quit)
    return app


def test_prices_and_names(app):
    for ind in range(3):
        app.add_some_product()

    app.remove_all_products()


"""
    #driver.find_element_by_css_selector("#cart .link").click()

    products = driver.find_elements_by_name("remove_cart_item")
    for i in range(len(products)):
        product = driver.find_element_by_name("remove_cart_item")
        product.click()
        wait.until(EC.staleness_of(product))

    confirm_text = wait.until(EC.presence_of_element_located((By.TAG_NAME, "em")))
    assert confirm_text.text == "There are no items in your cart."

"""