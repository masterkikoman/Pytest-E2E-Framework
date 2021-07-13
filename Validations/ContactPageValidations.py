from PageObjects.ContactPage import ContactPage
from PageObjects.HomePage import HomePage
from selenium.webdriver.support import expected_conditions as EC

from Utils.BaseClass import BaseClass


class ContactPageValidations(HomePage, ContactPage, BaseClass):

    def validateHeaderErrorMessage(self, msg):
        alertHeader = self.getHeader()
        assert msg in alertHeader.text

    def validateAllContextError(self, nameError, mailError, msgError):
        fornameError  = self.getForenameError().text
        emailError = self.getEmailError().text
        messageError = self.getMessageError().text
        assert fornameError == nameError
        assert emailError == mailError
        assert messageError == msgError

    def validateIfAllErrorNotPresent(self, msg):
        alertHeader = self.getHeader()
        self.synchronization().until(EC.invisibility_of_element_located(self.contactPageAllErrorMessage))
        assert msg not in alertHeader.text

    def validateSendingMessageIsDisplayed(self):
        sendingMessage = self.synchronization().until(EC.visibility_of_element_located(self.contactPageSubmitMessage))
        assert sendingMessage.text == "Sending Feedback"

    def validateSuccessMessageIsDisplayed(self, user):
        successMessage = self.synchronization().until(EC.presence_of_element_located(self.contactPageSuccessMessage))
        assert "Thanks " + user in successMessage.text

    # methods if test case need to validate error per field

    def validateNameError(self):
        fornameError = self.getForenameError().text

    def validateMailError(self):
        emailError = self.getEmailError().text

    def validateMsgError(self):
        messageError = self.getMessageError().text



