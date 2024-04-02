from selenium.webdriver.chrome import webdriver
import logging
from selenium import webdriver
import inspect
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def take_screenshot(self, method=None):

    # Hata mesajının olduğu yerin ekran görüntüsünü alın
    if method is None:
        method = inspect.stack()[2].function  # Çağrıldığı methodun üstündeki methodun adını alın [x] x kadar üstteki parent method
        file_name = f"C:\\Users\\10132589\\PycharmProjects\\AutomationProject\\screenshots\\Screenshoot_{method}.png"
        self.driver.save_screenshot(file_name)
    else:
        method = inspect.stack()[1].function  # Çağrıldığı methodun üstündeki methodun adını alın [x] x kadar üstteki parent method
        file_name = f"C:\\Users\\10132589\\PycharmProjects\\AutomationProject\\screenshots\\Screenshoot_{method}.png"
        self.driver.save_screenshot(file_name)
    print(f"Ekran görüntüsü '{file_name}' olarak kaydedildi.")

def browsersetup(self, url):
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
    # serv_obj = Service("C:\\Drivers\\chromedriver_win64\\chromedriver.exe")
    # driver = webdriver.Chrome(service=serv_obj)
    self.driver = webdriver.Chrome(options=options)
    self.driver.get(url)
    self.driver.maximize_window()
    self.driver.implicitly_wait(15)
    return self.driver

def loggerInit(self, test_class_name):
    self.logger = logging.getLogger(test_class_name)
    self.logger.setLevel(logging.INFO)
    # Dosyaya logları yazma
    file_name = f"C:\\Users\\10132589\\PycharmProjects\\AutomationProject\\testlogs\\{test_class_name}.log"
    file_handler = logging.FileHandler(file_name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    self.logger.addHandler(file_handler)
    self.logger.info("")
    self.logger.info("__________New Test Logs__________")
    self.logger.info("")
    return self.logger