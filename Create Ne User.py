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
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_create_new_user(driver):
    user_profile = {
        'tax_id': "777 777",
        'company': "Centaur",
        'firstname': "Kirill",
        'lastname': "Markidonov",
        'address1': "Moscow",
        'address2': "Perovo 1",
        'postcode': "111394",
        'city': "Moscow",
        'zone_code': "",
        'newsletter' : '0',
        'email': "markidonov@mail.ru",
        'phone': "89266146868",
        'password': "123456",
        'confirmed_password': "123456"
    }

    driver.get("http://localhost:8080/litecart")
    driver.find_element_by_css_selector("form a").click()
    inputs = driver.find_elements_by_css_selector("tr input")
    for input in inputs:
        if input.get_attribute("name") != 'zone_code':
            input.send_keys(user_profile[input.get_attribute("name")])

    select_elem = driver.find_element_by_css_selector(".select2-hidden-accessible")
    select = Select(select_elem)
    select.select_by_visible_text("Hong Kong")

    driver.find_element_by_name("create_account").click()


def test_approve_user(driver):
    driver.get("http://localhost:8080/litecart")
    driver.find_element_by_css_selector("[name=email]").send_keys("markidonov@mail.ru")
    driver.find_element_by_css_selector("[name=password]").send_keys("123456" + Keys.ENTER)

    assert "Kirill Markidonov" in driver.find_element_by_css_selector("div.success").text