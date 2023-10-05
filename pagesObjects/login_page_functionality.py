from pagesObjects.dashboard_page import DashboardPage
from pagesObjects.login_page import LoginPage
from pagesObjects.base_page import BasePage
from confingurations.config import TestData

"""
This contains all the loginpage functionalities
"""

class Signin(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(TestData.base_url)

    def get_login_page_title(self, title):
        return self.get_title(title)
    
    def login_btn_exist(self):
        return self.is_visible(LoginPage.login_button_xpath)
    
    # input login details and press logi n button
    def do_login(self, useremail, password):
        self.do_send_keys(LoginPage.login_email_input_xpath, useremail)
        self.do_send_keys(LoginPage.login_password_input_xpath, password)
        self.do_click(LoginPage.login_button_xpath)