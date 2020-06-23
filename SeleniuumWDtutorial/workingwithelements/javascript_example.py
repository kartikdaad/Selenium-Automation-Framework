from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class JavaScript:
    def test(self):
        driver = webdriver.Firefox()
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(baseUrl)

        height = driver.execute_script(" return window.innerHeight;")
        width = driver.execute_script(" return window.innerWidth")
        print("Height "+ str(height))
        print("Width " + str(width))

        driver.quit()
ff = JavaScript()
ff.test()