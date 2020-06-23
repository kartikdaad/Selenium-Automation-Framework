"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
import os
class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits webDriverFactory class
        returns :
            none
        """
        self.browser = browser
        """
        Set Chrome driver and Iexplorer environment based on OS
        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
         
         OR
         
         PREFERED: Set the path on the machine where browser will be execcuted
        """
    def getWebDriverInstance(self):
        baseURL = "https://letskodeit.teachable.com/"
        if self.browser == "iexplorer":
            # Set Ie Driver before executing
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set Chrome Driver before executing
            chromedriver = "/Users/Lenovo/Documents/python/selenium/drivers/chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            self.driver = webdriver.Chrome(chromedriver)
            driver = webdriver.Chrome(chromedriver)
            driver.set_window_size(1440, 900)
        else:
            driver = webdriver.Firefox()

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(10)

        # Maximize the window
        driver.maximize_window()

        # Loading the browser with APP URL
        driver.get(baseURL)

        return driver
