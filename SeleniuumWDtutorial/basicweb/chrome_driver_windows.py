from selenium import webdriver
'''class ChromeDriverWin():
    def Test(self):
        driver = webdriver.Chrome(executable_path="C:/Users/Lenovo/Documents/python/selenium/drivers/chromedriver.exe")
        driver.get("http://www.letskodeit.com")
rr=ChromeDriverWin()
rr.Test()
'''
driver = webdriver.Chrome()
driver.get("http://www.letskodeit.com")