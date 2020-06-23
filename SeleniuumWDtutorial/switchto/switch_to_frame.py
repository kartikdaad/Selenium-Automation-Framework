from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class SwitchtoWindow():
    def test(self):
        driver = webdriver.Firefox()
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(20)
        driver.execute_script("window.scrollBy(0,1000);")

        #Switch to frame using ID
#        driver.switch_to.frame("courses-iframe")

        #Switch to frame using name
       # driver.switch_to.frame("iframe-name")

        #Switch to frame using numbers
        #driver.



        time.sleep(3)
        searchBox = driver.find_element_by_id("search-courses")
        searchBox.send_keys("python")
        time.sleep(3)

        #Switch back to the parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(3)
        driver.find_element_by_id("name").send_keys("Test Successful")
