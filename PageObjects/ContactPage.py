from selenium.webdriver.common.by import By

class ContactPage:
    def __init__(self, driver):
        self.driver = driver

    contactPageContact = (By.ID, "nav-contact")
    contactPageSubmit = (By.XPATH, "//*[@class='btn-contact btn btn-primary']")
    contactPageAlertHeader = (By.ID, "header-message")
    contactPageForenameError = (By.ID, "forename-err")
    contactPageEmailError = (By.ID, "email-err")
    contactPageMessageError = (By.ID, "message-err")
    contactPageName = (By.ID, "forename")
    contactPageSurname = (By.ID, "surname")
    contactPageEmail = (By.ID, "email")
    contactPagePhone = (By.ID, "telephone")
    contactPageMessage= (By.ID, "message")
    contactPageAllErrorMessage = (By.XPATH, "//*[@class='help-inline ng-scope']")
    contactPageSubmit = (By.XPATH, "//*[@class='btn-contact btn btn-primary']")
    contactPageSubmitMessage = (By.XPATH, "//h1")
    contactPageSuccessMessage = (By.XPATH, "//*[@class='alert alert-success']")


    def getContact(self):
        return self.driver.find_element(*ContactPage.contactPageContact)

    def getSubmitButton(self):
        return self.driver.find_element(*ContactPage.contactPageSubmit)

    def getHeader(self):
        return self.driver.find_element(*ContactPage.contactPageAlertHeader)

    def getForenameError(self):
        return self.driver.find_element(*ContactPage.contactPageForenameError)

    def getEmailError(self):
        return self.driver.find_element(*ContactPage.contactPageEmailError)

    def getMessageError(self):
        return self.driver.find_element(*ContactPage.contactPageMessageError)

    def getName(self):
        return self.driver.find_element(*ContactPage.contactPageName)

    def getSurname(self):
        return self.driver.find_element(*ContactPage.contactPageSurname)

    def getEmail(self):
        return self.driver.find_element(*ContactPage.contactPageEmail)

    def getPhone(self):
        return self.driver.find_element(*ContactPage.contactPagePhone)

    def getMessage(self):
        return self.driver.find_element(*ContactPage.contactPageMessage)

    def getAllErrorMessage(self):
        return self.driver.find_element(*ContactPage.contactPageAllErrorMessage)

    def getSubmitButton(self):
        return self.driver.find_element(*ContactPage.contactPageSubmit)

    def getSubmitMessage(self):
        return self.driver.find_element(*ContactPage.contactPageSubmitMessage)

    def getSuccessMessage(self):
        return self.driver.find_element(*ContactPage.contactPageSuccessMessage)

