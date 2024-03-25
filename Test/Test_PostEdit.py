from POMDocuments.LoginPageObject import LoginPage
from POMDocuments.HomePageObject import HomePage
from POMDocuments.PostPageObject import PostPage

class Test_PostEdit:

    def test_PostEdit(self,setup):

        self.driver = setup
        self.driver.get("https://www.blogger.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.npp = PostPage(self.driver)

        #----Login Process-----
        self.lp.clickSignIn()
        self.lp.setUserMail(self.lp.user_Mail)
        self.lp.clickMailNext()
        self.lp.setPassword(self.lp.user_Password)
        self.lp.clickPassNext()

        #-----Home page Published post Click----
        self.hp.clickPostPublished()

        #---- Post Page Post Edit------
        self.npp.SwitchFrame_to_TextArea()
        self.npp.setText_to_TextArea(self.npp.Text)
        self.npp.SwitchDefaultFrame()
        self.npp.clickUpdateButton()
        self.driver.close()

