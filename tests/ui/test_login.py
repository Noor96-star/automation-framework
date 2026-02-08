from pages.login_page import LoginPage
from utils.read_data import read_json

def test_login_valid(driver, base_url):
    driver.get(base_url)

    data = read_json("test_data/login_data.json")
    username = data["valid_user"]["username"]
    password = data["valid_user"]["password"]

    login = LoginPage(driver)
    login.login(username, password)

    # ❌ wrong assertion to fail test
    assert "inventory123" in driver.current_url

