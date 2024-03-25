from selenium.webdriver.common.by import By
from time import sleep

class LoginPage:

    #Locators
    Locator_SignIn_CSS = "a[class='sign-in ga-header-sign-in'] span"
    Locator_UserMail_ID = "identifierId"
    Locator_UserPassword_Name = "Passwd"
    Locator_User_Next_Button_ID = "identifierNext"
    Locator_Password_Next_Button_ID = "passwordNext"

    #Variable_Values
    user_Mail = "bloggerautomationcase@gmail.com"
    user_Password = "Qwert54321."
    guest_Mail = "guestautomated1@gmail.com"
    guest_password= "Guest123"

    #-----Methods-----
    def __init__(self,driver):
        self.driver=driver

    def setUserMail(self,mail):
        sleep(3)
        userMailtxt=self.driver.find_element(By.ID,self.Locator_UserMail_ID)
        userMailtxt.clear()
        userMailtxt.send_keys(mail)

    def setPassword(self,password):
        sleep(3)
        passwordtxt=self.driver.find_element(By.NAME,self.Locator_UserPassword_Name)
        passwordtxt.clear()
        passwordtxt.send_keys(password)

    def clickSignIn(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,self.Locator_SignIn_CSS).click()

    def clickMailNext(self):
        sleep(3)
        self.driver.find_element(By.ID,self.Locator_User_Next_Button_ID).click()

    def clickPassNext(self):
        sleep(3)
        self.driver.find_element(By.ID, self.Locator_Password_Next_Button_ID).click()
