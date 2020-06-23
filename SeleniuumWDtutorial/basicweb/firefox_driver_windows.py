from selenium import webdriver
class RuffTests():
    def testMethod(self):
        driver= webdriver.Firefox()
        driver.get("http://www.letskodeit.com")

ff= RuffTests()
ff.testMethod()