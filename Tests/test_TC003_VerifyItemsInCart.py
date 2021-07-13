from UserActions.ShopPageUserActions import ShopPageUserActions
from Utils.BaseClass import BaseClass
from Validations.HomePageValidations import HomePageValidations
from Validations.CartPageValidations import CartPageValidations


class Test_VerifyItemsInCart(BaseClass):

    def test_verifyItems(self, shopPageData):
        log = self.getLogger()
        homePageValidations = HomePageValidations(self.driver)
        shopPageUserActions = ShopPageUserActions(self.driver)
        cartPageValidations = CartPageValidations(self.driver)
        homePageValidations.validateSuccessfulLandingPage()
        shopPageUserActions.clickShopButton()
        shopPageUserActions.orderingItems(shopPageData["funnyCow"], 2)
        shopPageUserActions.orderingItems(shopPageData["fluffyBunny"], 1)
        shopPageUserActions.getItemCount()
        shopPageUserActions.clickCart()
        cartPageValidations.verifyItemCount()
        cartPageValidations.verifyItemsAdded(shopPageData["funnyCow"])
        cartPageValidations.verifyItemsAdded(shopPageData["fluffyBunny"])
        log.info("Test_VerifyItemsInCart Run Successfully")



