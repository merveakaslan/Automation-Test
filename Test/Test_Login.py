from POMDocuments.LoginPageObject import LoginPage
from POMDocuments.HomePageObject import HomePage

class Test_Login:

    def test_login(self,setup):

        self.driver = setup
        self.driver.get("https://www.blogger.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)

        # ----Login Process-----
        self.lp.clickSignIn()
        self.lp.setUserMail(self.lp.user_Mail)
        self.lp.clickMailNext()
        self.lp.setPassword(self.lp.user_Password)
        self.lp.clickPassNext()
        self.driver.close()



































