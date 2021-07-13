import pytest

from TestData.ShopPageData import ShopPageData
from UserActions.ShopPageUserActions import ShopPageUserActions
from Utils.BaseClass import BaseClass
from Validations.CartPageValidations import CartPageValidations
from Validations.HomePageValidations import HomePageValidations


class Test_ComputeTotalValues(BaseClass, ShopPageData):

    def test_calculateItems(self, shopPageData):
        log = self.getLogger()
        homePageValidations = HomePageValidations(self.driver)
        shopPageUserActions = ShopPageUserActions(self.driver)
        cartPageValidations = CartPageValidations(self.driver)
        homePageValidations.validateSuccessfulLandingPage()
        shopPageUserActions.clickShopButton()
        shopPageUserActions.orderingItems(shopPageData["stuffedFrog"], 2)
        shopPageUserActions.orderingItems(shopPageData["fluffyBunny"], 5)
        shopPageUserActions.orderingItems(shopPageData["valentineBear"], 3)
        shopPageUserActions.getItemCount()
        shopPageUserActions.clickCart()
        cartPageValidations.verifyItemCount()
        cartPageValidations.verifyPricePerItem(shopPageData["stuffedFrog"], "$10.99")
        cartPageValidations.verifyPricePerItem(shopPageData["fluffyBunny"], "$9.99")
        cartPageValidations.verifyPricePerItem(shopPageData["valentineBear"],"$14.99")
        cartPageValidations.verifySubtotal(21.98)
        cartPageValidations.verifySubtotal(49.95)
        cartPageValidations.verifySubtotal(44.97)
        cartPageValidations.verifyTotal(116.9)
        log.info("Test_ComputeTotalValues Run Successfully")
