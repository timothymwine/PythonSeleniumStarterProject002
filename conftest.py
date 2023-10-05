# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options


# base_url = "https://demoqa.com"
# @pytest.fixture(scope="class", autouse=True )
# def browser_setup(request):
#     chrome_options = Options()
#     chrome_options.add_experimental_option("detach", True)
#     # driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options=chrome_options)
#     request.cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
#     driver.maximize_window()
#     driver.get(base_url)
#     driver.quit()