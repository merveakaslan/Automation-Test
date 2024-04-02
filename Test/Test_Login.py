from POMDocuments.LoginPageObject import LoginPage
from POMDocuments.HomePageObject import HomePage
import pytest
from configuration import basefunction, config

""" Test Case Steps:
    1. Open browser and visit Blogger.com
    2. To log in, enter your email address and password, then log in
    3. Close browser 
"""

class Test_Login:
    @pytest.mark.order(1)
    def test_login(self):
        self.logger = basefunction.loggerInit(self,self.__class__.__name__)
        self.driver = basefunction.browsersetup(self,config.adminblogurl)

        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)

        # ----Login Process-----
        self.lp.clicksignin()
        self.lp.setusermail(self.lp.usermail)
        self.lp.clickmailnext()
        self.lp.setpassword(self.lp.userpassword)
        self.lp.clickpassnext()

        self.tearDown()
    def tearDown(self):
        self.driver.close()



































