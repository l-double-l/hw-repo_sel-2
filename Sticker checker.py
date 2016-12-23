from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
'''

@author: Kirill Markidonov

'''


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(3)
    wd.maximize_window()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_most_popular(driver):
    # Please check the PORT!!!!!
    driver.get("http://localhost:8080/litecart")

    WebDriverWait(driver, 10).until(EC.title_contains("Online Store"))

    most_popular = driver.find_elements_by_css_selector("#box-most-popular li")

    if most_popular:
        for good in most_popular:
            stickers = good.find_elements_by_css_selector(".sticker")
            assert len(stickers) == 1

def test_latest_products(driver):
    # Please check the PORT!!!!!
    driver.get("http://localhost:8080/litecart")

    WebDriverWait(driver, 10).until(EC.title_contains("Online Store"))

    latest_products = driver.find_elements_by_css_selector("#box-latest-products li")

    if latest_products:
        for good in latest_products:
            stickers = good.find_elements_by_css_selector(".sticker")
            assert len(stickers) == 1
