from POMDocuments.HomePageObject import HomePage
from POMDocuments.LoginPageObject import LoginPage
from POMDocuments.CommentPageObject import CommentPage


class Test_CheckCommentByAdmin:

    def test_CheckComment(self,setup):

        self.driver = setup
        self.driver.get("https://www.blogger.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)

        #Login process
        self.lp.clickSignIn()
        self.lp.setUserMail(self.lp.user_Mail)
        self.lp.clickMailNext()
        self.lp.setPassword(self.lp.user_Password)
        self.lp.clickPassNext()

        #Home page go to comment section
        self.hp.clickCommentSection()
        self.cp = CommentPage(self.driver)
        self.cp.GetCommentTexts()
        self.cp.clickDeleteCommentIcon()
        self.cp.clickDeleteButton()
        self.driver.close()

