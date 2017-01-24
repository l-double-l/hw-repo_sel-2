from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class MainPageObject:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost:8080/litecart")
        return self

    def get_products_count(self):
        products = self.driver.find_elements_by_css_selector("#box-most-popular .product")
        return len(products)

    def click_on_nth_product(self, number):
        self.driver.find_element_by_css_selector("#box-most-popular .product:nth-child({})".format(number+1)).click()