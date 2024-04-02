from POMDocuments.LoginPageObject import LoginPage
from POMDocuments.HomePageObject import HomePage
from POMDocuments.PostPageObject import PostPage
import pytest
from configuration import basefunction, config

""" Test Case Steps:
    1. Open browser and visit Blogger.com
    2. Check the login page and click Signin button
    3. Enter your email address and password, then log in
    4. Check the home page after login
    5. Click the post that has been published
    6. Click the page 
    7. Edit the text with "Editted Post"
    8. Click Update button
    9. Close browser
"""

class Test_PostEdit:
    @pytest.mark.order(3)
    def test_PostEdit(self):
        self.logger = basefunction.loggerInit(self, self.__class__.__name__)
        self.driver = basefunction.browsersetup(self, config.adminblogurl)
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.npp = PostPage(self.driver)

        #Login Process
        self.lp.clicksignin()
        self.lp.setusermail(self.lp.usermail)
        self.lp.clickmailnext()
        self.lp.setpassword(self.lp.userpassword)
        self.lp.clickpassnext()

        #Home page Published post Click
        self.hp.clickPostPublished()

        #Post Page Post Edit
        self.npp.SwitchFrame_to_TextArea()
        self.npp.setText_to_TextArea(self.npp.Text)
        self.npp.SwitchDefaultFrame()
        self.npp.clickUpdateButton()

        self.tearDown()
    def tearDown(self):
        self.driver.close()