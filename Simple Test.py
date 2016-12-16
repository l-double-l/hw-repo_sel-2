from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
'''

@author: Kirill Markidonov

'''


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test1(driver):
    #Please check the PORT!!!!!
    driver.get("http://localhost:8080/litecart/admin/login.php")

    WebDriverWait(driver, 10).until(EC.title_contains("My Store"))

    login_box = driver.find_element_by_name("username")
    login_box.send_keys("admin")

    password_box = driver.find_element_by_name("password")
    password_box.send_keys("admin")

    login_btn = driver.find_element_by_name("login")
    login_btn.click()
