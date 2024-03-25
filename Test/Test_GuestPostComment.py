from POMDocuments.GuestPageObject import GuestPage
from POMDocuments.LoginPageObject import LoginPage

class Test_GuestPostComment:

    def test_postComment(self, setup):
        self.driver = setup
        self.driver.get("https://automationtestcase.blogspot.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

        #----- guest page Check if post is visible------
        self.gp = GuestPage(self.driver)
        self.gp.PostCheck()

        #-------Click to comment button -------
        self.gp.PostComment()
        self.gp.SwitchFrame_to_CommentSign()
        self.gp.click_GoogleSignIn_ForComment()

        # ----Login Process-----
        self.lp = LoginPage(self.driver)
        self.lp.setUserMail(self.lp.guest_Mail)
        self.lp.clickMailNext()
        self.lp.setPassword(self.lp.guest_password)
        self.lp.clickPassNext()

        #------ set comment and publish after sign in ---------
        self.gp.SwitchFrame_to_CommentSign()
        self.gp.setCommentText()
        self.gp.clickPublishCommentButton()
        self.driver.close()



