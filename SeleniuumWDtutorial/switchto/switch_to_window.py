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

        #Find parent handle ->Main window
        parentHandle = driver.current_window_handle
        print("Parent handle : "+str(parentHandle))

        #Find Open window button and click it
        driver.find_element_by_id("openwindow").click()

        #driver.find_element_by_id("opentab").click()
        time.sleep(5)
        #Find ALl handles , there should two handles after clicking open window button
        handles = driver.window_handles

        #Switch to window and search course
        for handle in handles:
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                searchbox = driver.find_element(By.ID , "search-courses")
                searchbox.send_keys("Javascript")
                time.sleep(3)
                driver.close()
                break


        #Switch back to parent handle
        driver.switch_to.window(parentHandle)
        driver.find_element_by_id("hide-textbox").click()
        time.sleep(3)


ff = SwitchtoWindow()
ff.test()