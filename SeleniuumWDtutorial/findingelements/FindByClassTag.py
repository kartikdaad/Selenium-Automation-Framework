from selenium import webdriver
from selenium.webdriver.common.by import By
class FindByClassTag():
    def test(self):
        baseUrl="https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByClass = driver.find_element_by_class_name("displayed-class")
        if elementByClass is not None:
            print("Element Found By Class")

        elementByTag = driver.find_element_by_tag_name("a")
        if elementByTag is not None:
            print("Eement found By Tag")

        elementBy = driver.find_element(By.NAME,"id")
ff = FindByClassTag()

ff.test()
