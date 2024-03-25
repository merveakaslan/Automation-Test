import pyperclip
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

class PostPage:

    #-----Locators------
    Locator_AddImage_Xpath = "(//span[@class='DPvwYc sm8sCf GHpiyd'][contains(text(),'')])[1]"
    Locator_AddImage_URL_Xpath = "/html[1]/body[1]/div[7]/c-wiz[2]/div[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/div[3]/span[1]/div[1]/div[1]/div[1]/div[1]/div[24]/div[1]/div[1]/span[4]/div[3]/div[1]"
    Locator_iframe_AddURL_Xpath = "/html/body/div[11]/div[2]/div/iframe"
    Locator_PasteImageURL_Input_Xpath = "/html[1]/body[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]"
    Locator_Select_URL_Button_ID = "picker:ap:0"
    Locator_PublishButton_CSS = "div[aria-label='Publish'] span[class='CwaK9']"
    Locator_ConfirmButton_Xpath = "(//span[@class='RveJvd snByac'][normalize-space()='Confirm'])[2]"
    Locator_iframe_TextArea_Xpath = "/html[1]/body[1]/div[7]/c-wiz[1]/div[1]/c-wiz[1]/div[1]/div[2]/div[1]/div[1]/div[3]/span[1]/div[1]/div[1]/div[2]"
    Locator_iframe_TextArea_CSS = "iframe[class='ZW3ZFc editable']"
    Locator_TextArea_Xpath = "(//body)[1]"
    Locator_UpdateButton_CSS = "div[aria-label='Publish'] div[class='A2yzVd']"

    #-----Variable_Values-----
    ImageURL = "https://img.freepik.com/free-photo/painting-mountain-lake-with-mountain-background_188544-9126.jpg"
    Text = "Editted Post"

    #-----Methods-----
    def __init__(self,driver):
        self.driver=driver

    def clickAddImage(self):
        sleep(3)
        self.driver.find_element(By.XPATH,self.Locator_AddImage_Xpath).click()

    def clickAdd_Image_W_URL(self):
        sleep(3)
        self.driver.find_element(By.XPATH, self.Locator_AddImage_URL_Xpath).click()

    def SwitchFrame_to_AddURL(self):
        sleep(3)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, self.Locator_iframe_AddURL_Xpath))

    def setImageURL_to_Input(self,url):
        sleep(3)
        pyperclip.copy(url)
        self.driver.find_element(By.XPATH,self.Locator_PasteImageURL_Input_Xpath).send_keys(Keys.CONTROL, 'v')

    def click_Select_URL_Button(self):
        sleep(5)
        self.driver.find_element(By.ID, self.Locator_Select_URL_Button_ID).click()

    def SwitchDefaultFrame(self):
        self.driver.switch_to.default_content()

    def clickPublishButton(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, self.Locator_PublishButton_CSS).click()

    def clickUpdateButton(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, self.Locator_UpdateButton_CSS).click()

    def clickConfirmButton(self):
        sleep(3)
        self.driver.find_element(By.XPATH, self.Locator_ConfirmButton_Xpath).click()

    def SwitchFrame_to_TextArea(self):
        sleep(3)
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, self.Locator_iframe_TextArea_CSS))

    def setText_to_TextArea(self,Text):
        sleep(3)
        pyperclip.copy(Text)
        self.driver.find_element(By.XPATH,self.Locator_TextArea_Xpath).send_keys(Keys.CONTROL, 'v')
