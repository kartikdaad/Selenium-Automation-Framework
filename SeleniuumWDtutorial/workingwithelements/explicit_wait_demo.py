from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitDemo():
    def test(self):
        baseUrl = "https://www.expedia.co.in/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(baseUrl)
        driver.find_element(By.ID,"tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("06/06/2020")
        returndate = driver.find_element(By.ID,"flight-returning-hp-flight")

        returndate.click()
        time.sleep(3)
        driver.execute_script("arguments[0].value = ''; ", returndate)
        returndate.send_keys("08/06/2020")

        driver.find_element(By.XPATH, "//form[@id='gcw-flights-form-hp-flight']//button[@class='btn-primary btn-action gcw-submit']").click()

        wait = WebDriverWait(driver, 20 , poll_frequency = 5 , ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID,"stopFilter_stops-0")))
        element.click()

        time.sleep(10)
        driver.quit()
ff= ExplicitWaitDemo()
ff.test()


