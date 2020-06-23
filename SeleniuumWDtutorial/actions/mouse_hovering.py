from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
class MouseHovering():
    def test(self):
        driver = webdriver.Firefox()
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(20)

        driver.execute_script("window.scrollBy(0,900);")
        time.sleep(3)
        element = driver.find_element_by_id("mousehover")
        itemToClickLocater = "//div[@class='mouse-hover-content']//a[text()='Top']"
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse Hovered on element")
            time.sleep(2)

            toplink = driver.find_element(By.XPATH, itemToClickLocater)
            actions.move_to_element(toplink).click().perform()
            print("Item Clicked")
        except:
            print("Mouse Hover failed on element")

ff = MouseHovering()
ff.test()


