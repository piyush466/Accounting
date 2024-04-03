from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjectModule.LoginPage import LoginPage
from Utilities.loggerfile import LogGen

class TestLogin:
    log = LogGen.logger()

    def test_logins(self,setup):
        self.log.info("**********Exicution Started*********")
        self.driver = setup
        self.lp=LoginPage(self.driver)
        self.lp.set_username("piyushdravyakar48@gmail.com")
        self.lp.set_password("Piyush@123")
        self.lp.login()
        self.emailcheck = self.driver.find_element(By.XPATH,"//p/strong").text
        if self.emailcheck == "piyushdravyakar4":
            print("test case Passed")
        else:
            print("Test case failed")
            self.driver.save_screenshot(r"C:\Users\ASUS\PycharmProjects\pythonProject1\Screenshots\login.png")