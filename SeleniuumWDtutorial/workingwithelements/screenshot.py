from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class screenshot:
    def test(self):
        baseUrl = "https://learn.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(baseUrl)

        driver.find_element(By.LINK_TEXT, "Login").click()
        email = driver.find_element(By.ID, "user_email")
        email.send_keys("daadkartik@gmail.com")
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("1234567890")
        driver.find_element(By.NAME, "commit").click()
        address = "C:\\Users\\Lenovo\\Desktop\\test.png"

        try:
            driver.save_screenshot(address)
            print("Scrrenshot saved")
        except NotADirectoryError:
            print("Not an error")
ff = screenshot()
ff.test()