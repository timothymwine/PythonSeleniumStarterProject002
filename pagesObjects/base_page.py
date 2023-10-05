from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage():

    def __init__(self, driver):
       self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, by_locator))).click()


    def do_send_keys(self, by_locator, text):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, by_locator)))
        element.clear()
        element.send_keys(text)
        

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(By.XPATH, by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(By.XPATH, by_locator))
        return bool(element)
    
    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(By.XPATH, by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 5).until(EC.title_is(title))
        return self.driver.title

    
