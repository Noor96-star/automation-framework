from pages.login_page import LoginPage
from pages.cart_page import CartPage

def test_add_to_cart(driver, base_url):
    driver.get(base_url)

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    cart = CartPage(driver)
    cart.add_product()
    cart.open_cart()

    product = cart.get_product_name()
    assert "Backpack" in product
