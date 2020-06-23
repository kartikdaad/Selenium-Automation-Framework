import utilities.custom_logger as cl
from base.basepage import BasePage
import logging
import time
class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    _search_box = "search-courses" #id
    _search_button = "search-course-button" #id
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _enroll_button = "enroll-button-top" #id
    _cc_num = "//input[@aria-label='Credit or debit card number']" #xpath
    _cc_exp = "exp-date" #name
    _cc_cvv = "cvc" #name
    _postal_code = "postal" #name
    _check_box= "agreed_to_terms_checkbox" #id
    _submit_enroll = "spc__button-text" #class
    _enroll_error_message = "The card was declined." #text

    def clickLoginLink(self):
        time.sleep(10)
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        time.sleep(10)
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        time.sleep(10)
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        time.sleep(10)
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def enterCourseName(self, name):
        time.sleep(10)
        self.sendKeys(name, self._search_box)
        self.elementClick(self._search_button, "id")

    def selectCourseToEnroll(self, fullCourseName):
        time.sleep(10)
        self.elementClick(self._course.format(fullCourseName), "xpath")

    def enterCardNum(self, num):
        self.switchToFrame(name="__privateStripeFrame13")
        self.sendKeys(num, self._cc_num, "xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.switchToFrame(name="__privateStripeFrame14")
        self.sendKeys(exp, self._cc_exp, "name")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        self.switchToFrame(name="__privateStripeFrame15")
        self.sendKeys(cvv, self._cc_cvv, "name")
        self.switchToDefaultContent()

    def enterZip(self, zip):
        self.switchToFrame(name="__privateStripeFrame16")
        self.sendKeys(zip, self._postal_code, "name")
        self.switchToDefaultContent()

    def enterCreditCardInformation(self, num, exp, cvv,zip):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.enterZip(zip)

    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll, "class")

    def enrollCourse(self, num="", exp="", cvv="", zip=""):
        time.sleep(10)
        self.elementClick(self._enroll_button, "id")
        time.sleep(10)
        self.webScroll("down")
        self.enterCreditCardInformation(num, exp, cvv, zip)
        self.elementClick(self._check_box, "id")
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        time.sleep(10)
        result = self.isEnabled(locator=self._submit_enroll,
                                       locatorType="xpath", info="Enroll Button")
        return not result

    def verifyPaymentFailed(self):
        time.sleep(10)
        result = self.isElementPresent("//div[@class='payment-error-box only-on-mobile']",
                                       locatorType="xpath")
        return result






