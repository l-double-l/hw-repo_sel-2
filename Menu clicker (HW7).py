from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


import pytest
'''

@author: Kirill Markidonov

'''


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
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

    test_data = [
        "Appearence", "Catalog", "Countries",
        "Currencies", "Customers", "Geo Zones",
        "Languages", "Modules", "Ordeers",
        "Pages", "Reports", "Settings",
        "Sliders", "Tax", "Translations",
        "Users", "vQmods"]
    menu_index = 0

    for data in test_data:
        menu_index += 1

        wait = WebDriverWait(driver, 5) # seconds
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul li#app-:nth-child({}) .name".format(menu_index))))
        print("waited")
        element.click()
        print("clicked")


