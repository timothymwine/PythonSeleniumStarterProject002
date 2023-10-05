from testCases.base_test import BaseTest
from pagesObjects.login_page_functionality import Signin
from confingurations.config import TestData

class Test_login(BaseTest):

    def test_login_page_title(self):
        self.signin = Signin(self.driver)
        title = self.signin.get_login_page_title(TestData.login_page_title)
        assert title == TestData.login_page_title

    def test_login(self):
        self.signin = Signin(self.driver)
        self.signin.do_login(TestData.useremail, TestData.password)
        

    
    
