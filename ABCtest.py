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

    #############################################################
    # Please check the PORT!!!!!
    wd.get("http://localhost:8080/litecart/admin/login.php")

    WebDriverWait(wd, 10).until(EC.title_contains("My Store"))

    login_box = wd.find_element_by_name("username")
    login_box.send_keys("admin")

    password_box = wd.find_element_by_name("password")
    password_box.send_keys("admin")

    login_btn = wd.find_element_by_name("login")
    login_btn.click()
    #############################################################

    request.addfinalizer(wd.quit)
    return wd

def test_countries(driver):
    driver.find_element_by_css_selector("ul li#app-:nth-child(3) .name").click()

    countries = driver.find_elements_by_css_selector(".dataTable .row td:nth-child(5) a")
    countries_names = []
    for country in countries:
        countries_names.append(country.text)
    unsorted = list(countries_names)
    countries_names.sort()

    assert countries_names == unsorted


def test_zones(driver):
    driver.find_element_by_css_selector("ul li#app-:nth-child(3) .name").click()

    countries = driver.find_elements_by_css_selector(".dataTable .row")
    countries_with_zones = []
    for country in countries:
        if country.find_element_by_css_selector("td:nth-child(6)").text != "0":
            countries_with_zones.append(country.find_element_by_css_selector("td:nth-child(5) a").text)

    for country_with_zones in countries_with_zones:
        country_row = driver.find_element_by_link_text(country_with_zones)

        country_row.click()

        countries_zones = driver.find_elements_by_css_selector(".dataTable tr td:nth-child(3)")
        del countries_zones[-1]

        countries_names = []
        for country_zone in countries_zones:
            countries_names.append(country_zone.text)
        unsorted = list(countries_names)
        countries_names.sort()

        assert countries_names == unsorted

        driver.find_element_by_css_selector("ul li#app-:nth-child(3) .name").click()



def test_geo_zones(driver):
    driver.find_element_by_css_selector("ul li#app-:nth-child(6) .name").click()

    geo_zones = driver.find_elements_by_css_selector(".dataTable .row td:nth-child(5) a")

    for i in range(len(geo_zones)):
        driver.find_element_by_css_selector(".dataTable .row:nth-child({}) td:nth-child(3) a".format(i+2)).click()

        countries_zones = driver.find_elements_by_css_selector(".dataTable td:nth-child(3) select [selected=selected]")
        zones_names = []
        for zone in countries_zones:
            zones_names.append(zone.text)
        unsorted = list(zones_names)
        zones_names.sort()

        assert zones_names == unsorted

        driver.find_element_by_css_selector("ul li#app-:nth-child(6) .name").click()