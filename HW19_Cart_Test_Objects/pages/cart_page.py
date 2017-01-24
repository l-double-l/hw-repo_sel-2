from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CartPageObject:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost:8080/litecart/checkout")
        return self

    def remove_all_products(self):
        products = self.driver.find_elements_by_name("remove_cart_item")
        for i in range(len(products)):
            product = self.driver.find_element_by_name("remove_cart_item")
            product.click()
            self.wait.until(EC.staleness_of(product))

        confirm_text = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "em")))
        assert confirm_text.text == "There are no items in your cart."
        return self