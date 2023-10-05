from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Selenium_Helper():
    
    def __init__(self, driver):
        self.driver = driver

    def send_keys_picker(self, locator, text):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)) \
                                            .send_keys(text)
        

    def click_picker(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).click()
        