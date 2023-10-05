from confingurations.config import TestData
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By
import datetime
import pytest

@pytest.mark.usefixtures("init_driver")
class BaseTest():
    pass
    # def navigate_to_url(self):
    #     # base_url = ReadConfig.get_application_url()
    #     self.driver.get(TestData.base_url)

    
    # def click_picker(self, locator):
    #     element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located
    #                                                   (By.XPATH, locator))
    #     element.click()

    # # method for dynamically generating new emails
    # def generate_email_with_stamp(self):
    #     time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    #     return "test"+time_stamp+"@gmail.com"

    # def wait_for_presence_of_all_elements(self, locator):
    #     list_of_elements = WebDriverWait(self.driver).until(EC.visibility_of_all_elements_located
    #                                                         (By.XPATH, locator))
    #     return list_of_elements
    
    # def wait_until_element_is_clickable(self, locator):
    #     element = WebDriverWait(self.driver).until(EC.element_to_be_clickable(By.XPATH, locator))
    #     return element