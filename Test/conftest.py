import pytest
from selenium import webdriver

@pytest.fixture()
def setup(self,url):
        options = webdriver.ChromeOptions()

        # Disable automatic close
        options.add_experimental_option("detach", True)

        options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"

        # Adding argument to disable the AutomationControlled flag
        options.add_argument("--disable-blink-features=AutomationControlled")

        # Exclude the collection of enable-automation switches
        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        # Turn-off userAutomationExtension
        options.add_experimental_option("useAutomationExtension", False)
        from selenium.webdriver.chrome.service import Service
        #serv_obj = Service("C:\\Drivers\\chromedriver_win64\\chromedriver.exe")
        #driver = webdriver.Chrome(service=serv_obj)
        self.driver = webdriver.Chrome(options = options)
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        return self.driver

#def pytest_addoption(parser):    # This will get the value from CLI
  #  parser.addoption("--browser")

#@pytest.fixture()
#def browser(request):       # This will return the Browser value to setup method
 #   return request.config.getoption("--browser")