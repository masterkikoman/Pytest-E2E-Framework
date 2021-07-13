from selenium.webdriver.common.by import By

class ShopPage():
    def __init__(self, driver):
        self.driver = driver

    shopPageButton = (By.ID, "nav-shop")
    shopPageItemList = (By.XPATH, "//*[@class='product ng-scope']")
    shopPageBuyButton = (By.XPATH, "(//div/p/a)")
    shopPageItemName = (By.XPATH, "//div/h4")
    shopPagecartButton = (By.XPATH, "//*[@href='#/cart']")
    shopPageItemCount = (By.XPATH, "//*[@class='cart-count ng-binding']")

    def getPageButton(self):
        return self.driver.find_element(*ShopPage.shopPageButton)

    def getItemName(self):
        return self.driver.find_elements(*ShopPage.shopPageItemName)

    def getCartButton(self):
        return self.driver.find_element(*ShopPage.shopPagecartButton)

    def getShopPageList(self):
        return self.driver.find_elements(*ShopPage.shopPageItemList)

    def getCountOfItems(self):
        return self.driver.find_element(*ShopPage.shopPageItemCount)

