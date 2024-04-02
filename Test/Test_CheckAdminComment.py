from POMDocuments.HomePageObject import HomePage
from POMDocuments.LoginPageObject import LoginPage
from POMDocuments.CommentPageObject import CommentPage
import pytest
from configuration import basefunction, config

"""Test Case Steps:
    1 - Open browser and visit Blogger.com
    2 - Enter your email address and password, then log in.
    4 - Check the home page after login
    5 - Click Comment Button
    6 - Check comment is visible and validate comment text
    7 - Click delete icon 
    8 - Click delete confirm button
    9 - Browser Closed
"""

class Test_CheckCommentByAdmin:
    @pytest.mark.order(6)
    def test_CheckComment(self):
        self.logger = basefunction.loggerInit(self, self.__class__.__name__)
        self.driver = basefunction.browsersetup(self, config.adminblogurl)
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)

        #Login process
        self.lp.clicksignin()
        self.lp.setusermail(self.lp.usermail)
        self.lp.clickmailnext()
        self.lp.setpassword(self.lp.userpassword)
        self.lp.clickpassnext()

        #Home page go to comment section
        self.hp.clickCommentSection()
        self.cp = CommentPage(self.driver)
        self.cp.GetCommentTexts()
        self.cp.clickDeleteCommentIcon()
        self.cp.clickDeleteButton()

        self.tearDown()
    def tearDown(self):
        self.driver.close()

