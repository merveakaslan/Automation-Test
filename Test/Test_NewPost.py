from POMDocuments.LoginPageObject import LoginPage
from POMDocuments.HomePageObject import HomePage
from POMDocuments.PostPageObject import PostPage
import pytest
from configuration import basefunction, config

""" Test Case Steps:
    1. Open browser and visit Blogger.com
    2. Enter your email address and password, then log in
    4. Check the home page after login
    5. Click New Post Button
    6. Click Insert Image icon
    7. Click By Url button
    8. Enter image url 
    9. Click select button
    10. Click publish button
    11. Click confirm button
    12. close browser 
"""

class Test_NewPost:
    @pytest.mark.order(2)
    def test_NewPost(self):
        self.logger = basefunction.loggerInit(self, self.__class__.__name__)
        self.driver = basefunction.browsersetup(self, config.adminblogurl)
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.npp = PostPage(self.driver)

        #----Login Process-----
        self.lp.clicksignin()
        self.lp.setusermail(self.lp.usermail)
        self.lp.clickmailnext()
        self.lp.setpassword(self.lp.userpassword)
        self.lp.clickpassnext()

        #-----Home page new post Click----
        self.hp.clickNewPost()

        #----- New post creation and image upload and Publishing--------
        self.npp.clickAddImage()
        self.npp.clickAdd_Image_W_URL()
        self.npp.SwitchFrame_to_AddURL()
        self.npp.setImageURL_to_Input(self.npp.ImageURL)
        self.npp.click_Select_URL_Button()
        self.npp.clickPublishButton()
        self.npp.clickConfirmButton()

        self.tearDown()
    def tearDown(self):
        self.driver.close()





