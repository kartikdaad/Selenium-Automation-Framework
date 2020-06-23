from selenium import webdriver

class FindByXpathCss():
    def test(self):
        baseUrl="https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")
        if elementByXpath is not None:
            print("Element Found By Xpath")

        elementByCss = driver.find_element_by_css_selector("#displayed-text")
        if elementByCss is not None:
            print("Eement found By Css")

ff = FindByXpathCss()
ff.test()