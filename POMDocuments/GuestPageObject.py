from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver

class GuestPage:

    #-----Locators-----
    Locator_NoPostMessage_CSS = "div[class='no-posts-message']"
    Locator_PostFeatured_ID = "FeaturedPost1"
    Locator_PostComment_CSS = "span[class='num_comments']"
    Locator_iframe_Comment_NAME = "comment-editor"
    Locator_GoogleSignIn_CSS ="div[aria-label='Sign in with Google'] span[class='RveJvd snByac']"
    Locator_CommentTextArea_CSS = "textarea[aria-label='Enter Comment']"
    Locator_PublishCommentButton_CSS = "div[aria-label='Publish'] span[class='RveJvd snByac']"
    Locator_PublishedComment_CSS= ".comment-content"


    #-----Variable_Value-----
    CommentText = "Ben Misafir Kullanıcıyım"

    #-----Methods-----

    def __init__(self,driver):
        self.driver = driver

    def PostCheck(self):
        sleep(3)
        elements = self.driver.find_elements(By.ID,self.Locator_PostFeatured_ID)
        # Eğer liste boşsa, element yoktur
        if not elements:
            assert False
        else:
            assert True

    def PostComment(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,self.Locator_PostComment_CSS).click()

    def SwitchDefaultFrame(self):
        self.driver.switch_to.default_content()

    def SwitchFrame_to_CommentSign(self):
        sleep(3)
        self.driver.switch_to.frame(self.driver.find_element(By.NAME, self.Locator_iframe_Comment_NAME ))

    def click_GoogleSignIn_ForComment(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, self.Locator_GoogleSignIn_CSS).click()

    def setCommentText(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, self.Locator_CommentTextArea_CSS).send_keys(self.CommentText)

    def clickPublishCommentButton(self):
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, self.Locator_PublishCommentButton_CSS).click()
        sleep(3)

    def CommentCheck(self):
        sleep(3)
        elements = self.driver.find_elements(By.CSS_SELECTOR, self.Locator_PublishedComment_CSS)
        # Eğer liste boşsa, element yoktur
        if not elements:
            assert True
        else:
            assert False