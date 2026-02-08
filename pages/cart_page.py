from locators.cart_locators import CartLocators

class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def add_product(self):
        self.driver.find_element(*CartLocators.ADD_TO_CART_BTN).click()

    def open_cart(self):
        self.driver.find_element(*CartLocators.CART_ICON).click()

    def get_product_name(self):
        return self.driver.find_element(*CartLocators.CART_ITEM).text
