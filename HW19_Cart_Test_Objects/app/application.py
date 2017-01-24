from selenium import webdriver
from HW19_Cart_Test_Objects.pages.main_page import MainPageObject
from HW19_Cart_Test_Objects.pages.product_page import ProductPageObject
from HW19_Cart_Test_Objects.pages.cart_page import CartPageObject

import random


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPageObject(self.driver)
        self.product_page = ProductPageObject(self.driver)
        self.cart_page = CartPageObject(self.driver)

    def quit(self):
        self.driver.quit()

    def add_some_product(self):
        pop_products_count = self.main_page.open().get_products_count()
        number = random.randrange(pop_products_count)
        self.main_page.click_on_nth_product(number)

        assert self.product_page.is_on_the_page()
        self.product_page.add_product_to_cart()

    def remove_all_products(self):
        self.cart_page.open().remove_all_products()
