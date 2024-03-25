from selenium.webdriver.common.by import By
from time import sleep
from POMDocuments.GuestPageObject import GuestPage
from selenium.webdriver.common.action_chains import ActionChains

class CommentPage:

    # Ziyaretçi sayfasında yapılan yorum textini otomatik olarak getCommentText içerisinde assert edebilmek için sınıfı burda çağırdık.
    gp = GuestPage

    #Locators
    Locator_CommentTexts_CSS = "div[class='Opvl3b']"
    Locator_CommentTexts_XPath = "//div[normalize-space()='Ben Misafir Kullanıcıyım']"
    Locator_CommentDeleteIcon_Xpath = "//c-wiz[@class='zQTmif SSPGKf eejsDc qWnhY O3LMFb haXJ6e']//div[@role='list']//div[1]//span[1]//div[1]//div[1]//div[4]//div[3]//span[1]//span[1]//span[1]"
    Locator_CommentDeleteButton_Xpath = "//*[@id='yDmH0d']/div[4]/div/div[2]/div[2]/div[2]"
    Locator_CommentListItems_Xpath = "(//div[@class='opmHNc'])[1]"
    Locator_CommentListItems_CSS = "div[role='list'] div:nth-child(1) span:nth-child(1) div:nth-child(1) div:nth-child(1) div:nth-child(4)"

    #Methods
    def __init__(self,driver):
        self.driver=driver

    def GetCommentTexts(self):
        sleep(3)
        element = self.driver.find_element(By.XPATH,self.Locator_CommentTexts_XPath)
        print(element.text)
        print(self.gp.CommentText)
        if element.text == self.gp.CommentText:
            assert True
        else:
            assert False

    def clickDeleteCommentIcon(self):
        sleep(2)
        action = ActionChains(self.driver)
        delete_item_list = self.driver.find_element(By.XPATH,self.Locator_CommentListItems_Xpath)
        action.move_to_element(delete_item_list).perform()
        sleep(3)
        self.driver.find_element(By.XPATH,self.Locator_CommentDeleteIcon_Xpath).click()

    def clickDeleteButton(self):
        sleep(3)
        self.driver.find_element(By.XPATH,self.Locator_CommentDeleteButton_Xpath).click()
