from POMDocuments.GuestPageObject import GuestPage

class Test_GuestPostCheck:

    def test_PostCheck(self, setup):

        self.driver = setup
        self.driver.get("https://automationtestcase.blogspot.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.gp = GuestPage(self.driver)
        self.gp.PostCheck()
        self.driver.close()

