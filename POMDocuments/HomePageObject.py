from selenium.webdriver.common.by import By
from time import sleep

class HomePage:

    #-----Locators------
    Locator_NewPost_Xpath = "//div[@class='SpTCHb']//span[@class='MIJMVe'][normalize-space()='New Post']"
    Locator_PostPublished_Xpath = "//c-wiz[@class='zQTmif SSPGKf eejsDc qWnhY O3LMFb haXJ6e']//a[@class='azat BJi0D']"
    Locator_CommentSection_CSS = "div[class='SpTCHb'] span[aria-label='Comments'] div[class='kurlme DQGx6d']"

    #-----Variable_Values-----

    #-----Methods------

    def __init__(self,driver):
        self.driver=driver

    def clickNewPost(self):
        sleep(3)
        self.driver.find_element(By.XPATH,self.Locator_NewPost_Xpath).click()

    def clickPostPublished(self):
        sleep(3)
        self.driver.find_element(By.XPATH,self.Locator_PostPublished_Xpath).click()

    def clickCommentSection(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,self.Locator_CommentSection_CSS).click()
