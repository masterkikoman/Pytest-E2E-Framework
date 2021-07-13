
import pytest

from UserActions.ContactPageUserActions import ContactPageUserActions
from Utils.BaseClass import BaseClass
from Validations.ContactPageValidations import ContactPageValidations
from Validations.HomePageValidations import HomePageValidations


class Test_SuccessfulSubmission(BaseClass):

    @pytest.mark.parametrize('execution_number', range(5))
    def test_successMessageSubmission(self, contactPageData, execution_number):
            log = self.getLogger()
            contactPageActions = ContactPageUserActions(self.driver)
            contactPageValidations = ContactPageValidations(self.driver)
            homePageValidations = HomePageValidations(self.driver)
            homePageValidations.validateSuccessfulLandingPage()
            contactPageActions.clickContactPage()
            contactPageActions.inputAllCredentails(contactPageData["forename"], contactPageData["surname"],
                                               contactPageData["email"], contactPageData["phone"],
                                               contactPageData["message"])
            contactPageActions.clickSubmitButton()
            contactPageValidations.validateSendingMessageIsDisplayed()
            contactPageValidations.validateSuccessMessageIsDisplayed(contactPageData["forename"])
            log.info("Test_SuccessfulSubmission Run Successfully")






