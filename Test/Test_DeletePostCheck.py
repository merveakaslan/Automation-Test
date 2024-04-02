from POMDocuments.HomePageObject import HomePage
from POMDocuments.LoginPageObject import LoginPage
from POMDocuments.PostPageObject import PostPage
import pytest
from configuration import basefunction, config

"""Test Case Steps:
    1 - Open browser and visit Blogger.com
    2 - To log in, enter your email address and password, then log in.
    4 - Check the home page after login
    5 - Click post delete icon
    6 - Click delete confirm button
    7 - Wait until home page refresh 
    8 - Close browser
"""

class Test_DeletePostCheck:
    @pytest.mark.order(8)
    def test_DeletePostCheck(self):
        self.logger = basefunction.loggerInit(self, self.__class__.__name__)
        self.driver = basefunction.browsersetup(self, config.adminblogurl)
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.npp = PostPage(self.driver)

        # Login process
        self.lp.clicksignin()
        self.lp.setusermail(self.lp.usermail)
        self.lp.clickmailnext()
        self.lp.setpassword(self.lp.userpassword)
        self.lp.clickpassnext()

        self.npp.PostList()
        self.npp.clickDeleteIcon()
        self.npp.clickTrashButton()
        self.npp.AfterDeletePostList()

        self.tearDown()
    def tearDown(self):
        self.driver.close()
