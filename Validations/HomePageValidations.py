from PageObjects.HomePage import HomePage


class HomePageValidations(HomePage):

    def validateSuccessfulLandingPage(self):
        homeMsg = self.getHomePage().text
        assert homeMsg == "Jupiter Toys"
