from pages.home.navigation_page import NavigationPage
import utilities.custom_logger as cl
import logging
import time
from base.basepage import BasePage
class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def clickLoginLink(self):
        time.sleep(10)
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        time.sleep(10)
        element = self.getElement(self._email_field, "id")
        element.clear()
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        time.sleep(10)
        #self.getElement(self._password_field, id).clear()
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        time.sleep(10)
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        time.sleep(10)
        result = self.isElementPresent("//*[@id='navbar']//li[@class='dropdown']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        time.sleep(10)
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Let's Kode It")

    def logout(self):
        self.nav.navigateToUserSettingsIcon()
        logoutLinkElement = self.waitForElement(locator="//div[@id='navbar']//a[@href='/sign_out']", locatorType="xpath", pollFrequency=1)
        self.elementClick(element=logoutLinkElement)