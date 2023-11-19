from myModule.point_income_api import base
from myModule.my_html.html_base import HtmlBase
from myModule.selenium_driver.selenium_element import seleniumElement

class Login(base.Base):
    ORIGIN_URL = "https://pointi.jp/"

    def login(self, driver, email_address, password):

        if len(email_address) < 0:
            return
        
        if len(password) < 0:
            return
        
        html_base = HtmlBase()
        login_driver = seleniumElement(driver)
        login_url = html_base.create_url(f"{self.ORIGIN_URL}entrance.php")

        print(f"Login::login login_url: {login_url}")
        driver.get(login_url)

        submit = login_driver.get_element_by_xpath('//form[@name="login"]/input[@name="Submit"]')
        email_elm = login_driver.get_element_by_xpath('//input[@name="email_address"]')
        email_elm.send_keys(email_address)
        password_elm = login_driver.get_element_by_xpath('//input[@name="password"]')
        password_elm.send_keys(password)

        driver.save_screenshot("obj/debug/login_inputed.png")

        submit.click()

        driver.save_screenshot("obj/debug/logined.png")

        
        if len(login_driver.get_elements_by_xpath('//a[@href="/logout.php"]')) <= 0:
            print("login failed")
            return False
        
        return True
