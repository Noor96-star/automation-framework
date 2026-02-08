from selenium.webdriver.common.by import By

class CartLocators:
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")
