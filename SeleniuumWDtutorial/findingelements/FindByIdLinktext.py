from selenium import webdriver

class FindByLinkText():
    def test(self):
        baseUrl="https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByLinkText = driver.find_element_by_link_text("Login")
        if elementByLinkText is not None:
            print("Element Found By Link Text")

        elementByPartialLinkText = driver.find_element_by_partial_link_text("Prac")
        if elementByPartialLinkText is not None:
            print("Eement found By Partial Link Text")

ff = FindByLinkText()
ff.test()