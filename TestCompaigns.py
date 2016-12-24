from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
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

def test_prices_and_names(driver):
    # Please check the PORT!!!!!
    driver.get("http://localhost:8080/litecart")

    WebDriverWait(driver, 10).until(EC.title_contains("Online Store"))

    campaign_camp_prices_obj = driver.find_elements_by_css_selector("#box-campaigns li .campaign-price")
    campaign_reg_prices_obj  = driver.find_elements_by_css_selector("#box-campaigns li .regular-price")
    campaign_names_obj       = driver.find_elements_by_css_selector("#box-campaigns li .name")

    campaign_camp_prices_str = []
    campaign_reg_prices_str = []
    campaign_names_str = []

    for price in campaign_camp_prices_obj:
        campaign_camp_prices_str.append(price.text)

    for price in campaign_reg_prices_obj:
        campaign_reg_prices_str.append(price.text)

    for name in campaign_names_obj:
        campaign_names_str.append(name.text)

    assert (len(campaign_camp_prices_obj) == len(campaign_reg_prices_obj))

    for indx in range(len(campaign_camp_prices_str)):
        for name in driver.find_elements_by_css_selector("#box-campaigns div.name "):
            if name.text == campaign_names_str[indx]:
                name.click()
                break

        global_name = driver.find_element_by_css_selector("h1.title").text
        global_reg_price = driver.find_element_by_css_selector(".regular-price").text
        global_camp_price = driver.find_element_by_css_selector(".campaign-price").text

        assert global_name       == campaign_names_str[indx]
        assert global_camp_price == campaign_camp_prices_str[indx]
        assert global_reg_price  == campaign_reg_prices_str[indx]

        driver.back()



def test_styles(driver):
    # Please check the PORT!!!!!
    driver.get("http://localhost:8080/litecart")

    WebDriverWait(driver, 10).until(EC.title_contains("Online Store"))

    campaign_camp_prices_obj = driver.find_elements_by_css_selector("#box-campaigns li .campaign-price")
    campaign_reg_prices_obj  = driver.find_elements_by_css_selector("#box-campaigns li .regular-price")
    campaign_names_obj       = driver.find_elements_by_css_selector("#box-campaigns li .name")

    campaign_camp_prices_str = []
    campaign_reg_prices_str = []
    campaign_names_str = []

    for price in campaign_camp_prices_obj:
        assert price.value_of_css_property("color") == 'rgba(204, 0, 0, 1)'
        assert price.value_of_css_property("font-weight") == "bold"

    for price in campaign_reg_prices_obj:
        assert price.value_of_css_property("text-decoration") == "line-through"
        assert price.value_of_css_property("font-weight") == "normal"

    for name in campaign_names_obj:
        campaign_names_str.append(name.text)

    for indx in range(len(campaign_camp_prices_str)):
        for name in driver.find_elements_by_css_selector("#box-campaigns div.name "):
            if name.text == campaign_names_str[indx]:
                name.click()
                break

        global_reg_price = driver.find_element_by_css_selector(".regular-price")
        global_camp_price = driver.find_element_by_css_selector(".campaign-price")

        assert global_camp_price.value_of_css_property("color") == 'rgba(204, 0, 0, 1)'
        assert global_camp_price.value_of_css_property("font-weight") == "bold"

        assert global_reg_price.value_of_css_property("text-decoration") == "line-through"
        assert global_reg_price.value_of_css_property("font-weight") == "normal"

        driver.back()

