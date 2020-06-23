from selenium import  webdriver
from selenium.webdriver.common.by import By
import  time
class ImplicitWaitDemo():
    def test(self):
        baseUrl = "https://learn.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(baseUrl)

        loginlink = driver.find_element(By.XPATH,"//div[contains(@class,'navbar')]//a[@href='/sign_in']")
        loginlink.click()

        email = driver.find_element(By.ID,"user_email")
        email.send_keys("daadkartik@gmail.com")

ff = ImplicitWaitDemo()
ff.test()