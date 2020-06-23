from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class ScrollingElement():
    def test(self):
        driver = webdriver.Firefox()
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(20)

        #scroll down
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(3)
        #scroll Up
        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(3)
        #scroll element into view

        element = driver.find_element(By.ID,"mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);",element)
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-150)")

        #native Way to scroll INto View
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,-1000);")
        location = element.location_once_scrolled_into_view
        print("Location : "+str(location))

ff = ScrollingElement()
ff.test()
