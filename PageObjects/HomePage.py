from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    homeName = (By.CLASS_NAME, "brand")

    def getHomePage(self):
        return self.driver.find_element(*HomePage.homeName)


