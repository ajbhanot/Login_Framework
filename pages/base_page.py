from selenium.webdriver.support.ui import WebDriverWait as WB
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config
from utilities.logger import logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WB(self.driver, Config.TIMEOUT)

    def send_keys(self, locator, text):
        logger.info(f"Entering text into: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        logger.info(f"Entering text into element: {locator}")



        logger.info("Text entered successfully")

    def click(self, locator):
        logger.info(f"Clicking on element: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        logger.info("Element clicked successfully")

    def is_displayed(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.is_displayed()

    def is_enabled(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.is_enabled()

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def scroll(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def take_screenshot(self, path):
        self.driver.save_screenshot(path)