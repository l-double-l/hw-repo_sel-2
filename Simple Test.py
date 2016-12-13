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
    driver.get("https://obtest18.centaurportal.com/d4w/0315/org-91/landing")

    WebDriverWait(driver, 10).until(EC.title_contains("Welcome to eServices"))

    sign_in_lnk = driver.find_element_by_link_text("Sign In")
    sign_in_lnk.click()

    WebDriverWait(driver, 10).until(EC.title_contains("Sign In"))
