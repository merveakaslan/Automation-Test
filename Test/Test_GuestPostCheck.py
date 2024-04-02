from POMDocuments.GuestPageObject import GuestPage
import pytest
from configuration import basefunction, config

""" Test Case Steps:
1 - Open browser and visit https://automationtestcase.blogspot.com/
2 - Wait until page loading 
3 - Check post visibility
4 - Close browser
"""

class Test_GuestPostCheck:
    @pytest.mark.order(4)
    def test_PostCheck(self):
        self.logger = basefunction.loggerInit(self, self.__class__.__name__)
        self.driver = basefunction.browsersetup(self, config.guestblogurl)
        self.gp = GuestPage(self.driver)
        self.gp.PostCheck()

        self.tearDown()
    def tearDown(self):
        self.driver.close()

