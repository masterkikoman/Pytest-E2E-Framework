import time

from PageObjects.ShopPage import ShopPage


class ShopPageUserActions(ShopPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickShopButton(self):
        self.getPageButton().click()

    def clickBuyButton(self):
        self.getBuyButton().click()


    def getItemCount(self):
        count = self.getCountOfItems()
        return count.text


    def clickCart(self):
        self.getCartButton().click()

    def orderingItems(self, item, count):
        lists = self.getShopPageList()
        for list in lists:
            names = list.find_element_by_xpath("div/h4").text
            if names == item:
                i = 0
                while i < count:
                    list.find_element_by_xpath("div/p/a").click()
                    i=i+1











