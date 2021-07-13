from PageObjects.ContactPage import ContactPage
from PageObjects.HomePage import HomePage


class ContactPageUserActions(ContactPage):

    def clickContactPage(self):
        self.getContact().click()

    def clickSubmitButton(self):
        self.getSubmitButton().click()

    def inputAllCredentails(self, name, surname, email, phone, message):
        self.getName().send_keys(name)
        self.getSurname().send_keys(surname)
        self.getEmail().send_keys(email)
        self.getPhone().send_keys(phone)
        self.getMessage().send_keys(message)

    # methods if test case need to input message one by one
    def inputName(self):
        self.getName().send_keys("")

    def inputSurname(self):
        self.getSurname().send_keys("")
    def inputEmail(self):
        self.getEmail().send_keys("")

    def inputPhone(self):
        self.getPhone().send_keys("")

    def inputMessage(self):
        self.getMessage().send_keys("")






