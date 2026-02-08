import pytest
import os
from datetime import datetime
from utils.driver_factory import get_driver
import allure

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return "https://www.saucedemo.com"


# 🔥 Screenshot on failure hook
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshots_dir = "reports/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)

            # attach to allure
            allure.attach.file(file_path,
                               name="Failure Screenshot",
                               attachment_type=allure.attachment_type.PNG)
