from POMDocuments.GuestPageObject import GuestPage
import pytest
from configuration import basefunction, config

"""Test Case Steps:

1 - Open browser and visit https://automationtestcase.blogspot.com/
2 - Check the post visibility
3 - Check comment is deleted
4 - Close browser

"""

class Test_GuestCommentCheck:
    @pytest.mark.order(7)
    def test_CommentCheck(self):
        self.logger = basefunction.loggerInit(self, self.__class__.__name__)
        self.driver = basefunction.browsersetup(self, config.guest_blog_Url)
        self.gp = GuestPage(self.driver)
        self.gp.CommentCheck()

        self.tearDown()
    def tearDown(self):
        self.driver.close()
