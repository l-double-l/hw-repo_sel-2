from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import pytest
'''

@author: Kirill Markidonov

'''


@pytest.fixture
def f_driver(request):
    wd = webdriver.Firefox()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

@pytest.fixture
def f_n_driver(request):

    binary = FirefoxBinary('C:\Program Files\Nightly\\firefox.exe')
    wd = webdriver.Firefox(firefox_binary=binary)
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

@pytest.fixture
def i_driver(request):
    wd = webdriver.Ie()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

@pytest.fixture
def ch_driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_f_n(f_n_driver):
    # Please check the PORT!!!!!
    f_n_driver.get("http://localhost:8080/litecart/admin/login.php")

    WebDriverWait(f_n_driver, 10).until(EC.title_contains("My Store"))

    login_box = f_n_driver.find_element_by_name("username")
    login_box.send_keys("admin")

    password_box = f_n_driver.find_element_by_name("password")
    password_box.send_keys("admin")

    login_btn = f_n_driver.find_element_by_name("login")
    login_btn.click()
