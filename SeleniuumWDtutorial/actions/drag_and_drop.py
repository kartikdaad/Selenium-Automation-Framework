from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
class Draganddrop():
    def test(self):
        driver = webdriver.Firefox()
        baseUrl = "https://jqueryui.com/droppable/"
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(20)

        driver.switch_to.frame(0)

        fromElement = driver.find_element(By.ID, "draggable")
        toElement = driver.find_element(By.ID, "droppable")
        time.sleep(2)
        try:
            action = ActionChains(driver)
            action.drag_and_drop(fromElement, toElement).perform()
            print("Drag and drop element successful")
            time.sleep(2)
        except:
            print("Failed")

ff = Draganddrop()
ff.test()