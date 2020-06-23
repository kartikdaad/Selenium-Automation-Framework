from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class SouthWest_Example:
    def test(self):
        baseUrl = "https://www.southwest.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(baseUrl)

        