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

    #############################################################
    # Please check the PORT!!!!!
    wd.get("http://localhost:8080/litecart/admin/?app=countries&doc=edit_country")

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

def test_links_in_country(driver):
    link_list = driver.find_elements_by_css_selector("i.fa-external-link")
    for link in link_list:
        main_window = driver.current_window_handle
        old_windows = driver.window_handles
        link.click()
        time.sleep(2)
        new_windows = driver.window_handles
        new_windows.remove(main_window)
        new_window = new_windows[0]
        driver.switch_to_window(new_window)

        assert driver.find_elements_by_css_selector("head")

        driver.close()
        driver.switch_to_window(main_window)

def there_is_window_other_than(dr, old_windows):
    while len(dr.window_handles) == len(old_windows):
        time.sleep(1)
    return True


