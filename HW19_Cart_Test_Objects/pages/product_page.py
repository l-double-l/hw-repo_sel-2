from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductPageObject:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, product_name):
        self.driver.get("http://localhost:8080/litecart/{}".format(product_name))
        return self

    def is_on_the_page(self):
        return len(self.driver.find_elements_by_css_selector("li.active")) > 0

    def add_product_to_cart(self):
        quantity = int(self.driver.find_element_by_css_selector("span.quantity").text)
        self.driver.find_element_by_name("add_cart_product").click()
        assert self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), "{}".format(quantity + 1)))
        return self