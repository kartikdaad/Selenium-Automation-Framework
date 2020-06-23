from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DynamicXpathFormat():
    def test(self):
        baseUrl = "https://learn.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(baseUrl)

        driver.find_element(By.LINK_TEXT,"Login").click()
        email = driver.find_element(By.ID,"user_email")
        email.send_keys("daadkartik@gmail.com")
        password = driver.find_element(By.ID,"user_password")
        password.send_keys("1234567890")
        driver.find_element(By.NAME,"commit").click()

        searchBox = driver.find_element(By.ID,"search-courses")
        searchBox.send_keys("JavaScript")

        _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        _courseLocater = _course.format("JavaScript for beginners")

        courseElement = driver.find_element(By.XPATH,_courseLocater)
        courseElement.click()
ff =DynamicXpathFormat()
ff.test()
