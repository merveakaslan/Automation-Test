from POMDocuments.GuestPageObject import GuestPage
from POMDocuments.LoginPageObject import LoginPage
import pytest
from configuration import basefunction, config

"""Test Case Steps:
1 - Open browser and visit https://automationtestcase.blogspot.com/
2 - Click "Post a Comment" button
3 - Click "Sign in With Google" button
4 - Enter email and Password then login
5 - Click Enter Comment textbox
6 - Enter a comment
7 - Click Publish button
8 - Check comment if it is added or not
9 - Close browser
"""

class Test_GuestPostComment:
    @pytest.mark.order(5)
    def test_postComment(self):
        self.logger = basefunction.loggerInit(self, self.__class__.__name__)
        self.driver = basefunction.browsersetup(self, config.guestblogurl)

        #guest page Check if post is visible
        self.gp = GuestPage(self.driver)
        self.gp.PostCheck()

        #Click to comment button
        self.gp.PostComment()
        self.gp.SwitchFrame_to_CommentSign()
        self.gp.click_GoogleSignIn_ForComment()

        #Login Process
        self.lp = LoginPage(self.driver)
        self.lp.setusermail(self.lp.guestmail)
        self.lp.clickmailnext()
        self.lp.setpassword(self.lp.guestpassword)
        self.lp.clickpassnext()

        #set comment and publish after sign in
        self.gp.SwitchFrame_to_CommentSign()
        self.gp.setCommentText()
        self.gp.clickPublishCommentButton()

        self.tearDown()
    def tearDown(self):
        self.driver.close()



