import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options
import time

@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        chr_options = Options()
        chr_options.add_experimental_option("detach", True)
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chr_options)
    elif request.param == "firefox":
        web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    web_driver.maximize_window()
    request.cls.driver = web_driver
    web_driver.implicitly_wait(5)
    yield
    web_driver.close()
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):

#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extras = getattr(report, "extras", [])

#     if report.when == "call" or report.when == "setup":
#         # always add url to report
#         # extras.append(pytest_html.extras.url("http://www.example.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img scr="%s" alt="screenshot" style="width:384px; height:228px; onclick="window.open(this.src) align="right"/></div>' %file_name
#                 # only add additional html on failure
#                 extras.append(pytest_html.extras.html(html))
#         report.extras = extras


# def _capture_screenshot(self, name):
#     self.driver.get_screenshot_as_file(name)


# def pytest_html_report_title(report):
#     report.title = "Automation Report"

# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'Tim'

# def pytest_addoption(parser):
#     # parser.addoption("--browser", action="store")
#     parser.addoption("--browser", action="store")
#     # parser.addoption("--browser", action="store", default=settings.browser)
#     # parser.addoption("--env", action="store", default=settings.env)

# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
