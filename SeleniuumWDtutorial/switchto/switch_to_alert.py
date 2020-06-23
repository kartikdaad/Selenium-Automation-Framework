from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class SwitchtoAlert():
    def test(self):
        driver = webdriver.Firefox()
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(20)

        driver.find_element_by_id("name").send_keys("kartik")
        driver.find_element_by_id("alertbtn").click()
        time.sleep(2)
        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(2)
        driver.find_element_by_id("name").send_keys("kartik")
        driver.find_element_by_id("confirmbtn").click()
        alert2 = driver.switch_to.alert
        alert2.dismiss()
        driver.c
ff =  SwitchtoAlert()
ff.test()
