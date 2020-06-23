from selenium import webdriver

class FindByIdName():
    def test(self):
        baseUrl="https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")
        if elementById is not None:
            print("Element Found By Id")

        elementByName = driver.find_element_by_name("show-hide")
        if elementByName is not None:
            print("Eement found By Name")

ff = FindByIdName()
ff.test()