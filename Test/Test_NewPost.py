from POMDocuments.LoginPageObject import LoginPage
from POMDocuments.HomePageObject import HomePage
from POMDocuments.PostPageObject import PostPage

class Test_NewPost:

    def test_NewPost(self,setup):

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

        #-----Home page new post Click----
        self.hp.clickNewPost()

        #----- New post creation and image upload and Publishing--------
        self.npp.clickAddImage()
        self.npp.clickAdd_Image_W_URL()
        self.npp.SwitchFrame_to_AddURL()
        self.npp.setImageURL_to_Input(self.npp.ImageURL)
        self.npp.click_Select_URL_Button()
        self.npp.clickUpdateButton()
        self.npp.clickConfirmButton()
        self.driver.close()





