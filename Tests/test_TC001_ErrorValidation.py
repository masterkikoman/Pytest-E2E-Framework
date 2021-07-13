import pytest

from TestData.ContactPageData import ContactPageData
from UserActions.ContactPageUserActions import ContactPageUserActions
from Utils.BaseClass import BaseClass
from Validations.ContactPageValidations import ContactPageValidations
from Validations.HomePageValidations import HomePageValidations


class Test_ErrorValidation(BaseClass):

    def test_errorValidation(self, getErrorMessage, contactPageData):
        log = self.getLogger()
        contactPageActions = ContactPageUserActions(self.driver)
        contactPageValidations = ContactPageValidations(self.driver)
        homePageValidations = HomePageValidations(self.driver)
        homePageValidations.validateSuccessfulLandingPage()
        contactPageActions.clickContactPage()
        contactPageActions.clickSubmitButton()
        contactPageValidations.validateHeaderErrorMessage(getErrorMessage["headerErrMsg"])
        contactPageValidations.validateAllContextError(getErrorMessage["nameError"], getErrorMessage["mailError"], getErrorMessage["msgError"])
        contactPageActions.inputAllCredentails(contactPageData["forename"], contactPageData["surname"],
                                               contactPageData["email"], contactPageData["phone"],
                                               contactPageData["message"])
        contactPageValidations.validateIfAllErrorNotPresent(getErrorMessage["headerErrMsg"])
        log.info("Test_ErrorValidation Run Successfully")

    @pytest.fixture(params=ContactPageData.test_ContactPage_errorMessage)
    def getErrorMessage(self, request):
        return request.param








