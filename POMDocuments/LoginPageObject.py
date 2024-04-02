from selenium.webdriver.common.by import By
from time import sleep
from configuration import basefunction

class LoginPage:

    #Locators
    Locator_signin_CSS = "a[class='sign-in ga-header-sign-in'] span"
    Locator_usermail_ID = "identifierId"
    Locator_userpassword_Name = "Passwd"
    Locator_usernextbutton_ID = "identifierNext"
    Locator_passwordnextbutton_ID = "passwordNext"

    #Variable_Values
    usermail = "bloggerautomationcase@gmail.com"
    userpassword = "Qwert54321."
    guestmail = "guestautomated1@gmail.com"
    guestpassword = "Guest123"

    #-----Methods-----
    def __init__(self,driver):
        self.driver=driver

    def setusermail(self,mail):
        sleep(3)
        usermailtxt=self.driver.find_element(By.ID,self.Locator_usermail_ID)
        usermailtxt.clear()
        usermailtxt.send_keys(mail)
        basefunction.take_screenshot(self ,1)

    def setpassword(self,password):
        sleep(3)
        passwordtxt=self.driver.find_element(By.NAME,self.Locator_userpassword_Name)
        passwordtxt.clear()
        passwordtxt.send_keys(password)

    def clicksignin(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,self.Locator_signin_CSS).click()

    def clickmailnext(self):
        sleep(3)
        self.driver.find_element(By.ID,self.Locator_usernextbutton_ID).click()

    def clickpassnext(self):
        sleep(3)
        self.driver.find_element(By.ID, self.Locator_passwordnextbutton_ID).click()
