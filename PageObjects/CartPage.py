from selenium.webdriver.common.by import By

class CartPage():
    def __init__(self, driver):
        self.driver = driver

    cartPageItemCount = (By.XPATH, "//*[@ui-if='cart.getCount() > 0']//*[@class='cart-count ng-binding']")
    cartPagewholeTable = (By.XPATH, "//*[@class='table table-striped cart-items']/tbody")

    def getCartItemCount(self):
        return self.driver.find_element(*CartPage.cartPageItemCount)

    def getItemsInTable(self):
        return self.driver.find_element(*CartPage.cartPagewholeTable)

