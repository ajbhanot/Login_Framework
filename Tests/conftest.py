import pytest
from selenium.webdriver import Chrome
from config.config import Config
from utilities.screenshot import Screenshot

@pytest.fixture()
def setup():
    driver = Chrome()
    driver.maximize_window()
    driver.get(Config.URL)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["setup"]

        Screenshot.capture(driver)