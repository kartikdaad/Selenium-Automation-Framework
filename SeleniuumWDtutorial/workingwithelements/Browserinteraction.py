from selenium import webdriver

class BrowserInteractions():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver  = webdriver.Firefox()
        #maximize Window
        driver.maximize_window()
        #open url
        driver.get(baseUrl)

        title = driver.title
        print("Title of the web page " + title)

        currentUrl = driver.current_url
        print("Current Url "+ currentUrl)

        driver.refresh()
        print("Browser Referesh 1st")

        driver.get(driver.current_url)
        print("Browser Referesh 2st")

        #open another Url
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")

        #back
        driver.back()
        print("One step backward")

        #forword
        driver.forward()
        print("One step forward")

        #page source
        pagesource = driver.page_source

        driver.close()

ff =BrowserInteractions()
ff.test()