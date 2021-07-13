from logging import getLogger

from PageObjects.CartPage import CartPage
from selenium.webdriver.support import expected_conditions as EC
from UserActions.ShopPageUserActions import ShopPageUserActions
from Utils.BaseClass import BaseClass


class CartPageValidations(CartPage, ShopPageUserActions, BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    xloc = "//*[@class='table table-striped cart-items']/tbody/"

    def verifyItemCount(self):
        shopPageCount = self.getItemCount()
        cartPageCount = self.synchronization().until(EC.presence_of_element_located(self.cartPageItemCount))
        assert shopPageCount == cartPageCount.text
    def verifyItemsAdded(self, toys):
        table = self.synchronization().until(EC.presence_of_element_located(self.cartPagewholeTable))
        assert toys in table.text

    def verifyPricePerItem(self, item, price):
        table = self.getItemsInTable()
        column = table.find_elements_by_xpath("tr")
        colCount = len(column)
        for i in range (1, colCount + 1):
            if i <= colCount:
                itemName = table.find_element_by_xpath(self.xloc+"tr["+str(i)+"]/td[1]").text
                if item == itemName:
                    assert item in itemName
                    itemPrice = table.find_element_by_xpath(self.xloc + "tr["+str(i)+"]/td[2]").text
                    assert price in itemPrice

    def verifySubtotal(self, sub):
        table = self.getItemsInTable()
        column = table.find_elements_by_xpath("tr")
        colCount = len(column)
        for i in range (1, colCount + 1):
                itemQuantity = table.find_element_by_xpath(self.xloc + "tr["+str(i)+"]/td[3]/input")
                quantity = itemQuantity.get_attribute("value")
                itemPrice = table.find_element_by_xpath(self.xloc + "tr[" + str(i) + "]/td[2]").text
                itemPrice =itemPrice[1:]
                subtotal = float(itemPrice) * float(quantity)
                if float(sub) == subtotal:
                    assert sub == subtotal
                    break

    def verifyTotal(self, totalVal):
        table = self.getItemsInTable()
        column = table.find_elements_by_xpath("tr")
        colCount = len(column)
        total = 0
        for i in range (1, colCount + 1):
                subTotal = table.find_element_by_xpath(self.xloc + "tr[" + str(i) + "]/td[4]").text
                subTotal = subTotal[1:]
                strToflt = float(subTotal)
                total = total + strToflt
        assert totalVal == total






























