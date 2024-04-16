import time

from PageObjectModule.ProceedPage import Proceed_Checkout
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjectModule.LoginPage import LoginPage
from Utilities.loggerfile import LogGen
from PageObjectModule.ShopPage import Shoppage

class TestLogin:
    log = LogGen.logger()
    username = "piyushdravyakar48@gmail.com"
    password = "Piyush@123"

    def test_logins(self,setup):
        self.log.info("**********Exicution Started*********")
        self.driver = setup
        self.lp=LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.log.info("Your Username is: %s -", self.username)
        self.lp.set_password(self.password)
        self.log.info("Your password is: %s -", self.password)
        self.lp.login()
        self.log.info("Click on Login button")
        self.emailcheck = self.driver.find_element(By.XPATH,"//p/strong").text
        if self.emailcheck == "piyushdravyakar4":
            print("test case Passed")
            self.log.info("************Email verified************")

        else:
            print("Test case failed")
            self.log.error("Test case is failed")
            self.driver.save_screenshot(r"C:\Users\ASUS\PycharmProjects\pythonProject1\Screenshots\login.png")

        self.log.info("**********Exicution Succesful*********")


    def test_shopping(self, setup):
        self.driver = setup
        self.obj = TestLogin()
        self.obj.test_logins(self.driver)
        self.sp = Shoppage(self.driver)
        self.log.info("*********Test Case 2 Started**********")
        self.sp.click_on_shop()

        self.books = self.driver.find_elements(By.XPATH, self.sp.books_text_xpath)
        self.buttons = self.driver.find_elements(By.XPATH, self.sp.btn_add_to_basket_xpath)
        time.sleep(5)
        self.log.info("**********started for loop************")
        for self.book,self.button in zip(self.books,self.buttons):
            print(self.book.text)

            if self.book.text == "HTML5 Forms":
                self.button.click()
                break
        self.log.info("*********Test Case 2 Ended**********")
        self.driver.save_screenshot(r"C:\Users\ASUS\PycharmProjects\pythonProject1\Screenshots\Test_case2.png")
        self.sp.click_items()
        time.sleep(3)


    def test_proceed_To_Checkout(self,setup):
        self.driver = setup
        self.obj = TestLogin()

        self.obj.test_shopping(self.driver)
        self.pc = Proceed_Checkout(self.driver)
        self.elements = self.driver.find_elements(By.XPATH, "//a")
        for element in self.elements:
            print(element.text)
            if element.text == "HTML5 Forms":
                print("match with Book")
                break
        self.driver.execute_script("window.scrollBy(0,1500)")
        self.pc.proceed_btn()

        self.radios = self.driver.find_elements(By.XPATH, "//input[@type='radio']")
        self.payments = self.driver.find_elements(By.XPATH, "//li/label")

        for radio,payment in zip(self.radios,self.payments):
            print(payment.text)
            if payment.text == "Cash on Delivery":
                radio.click()
        time.sleep(3)
        self.pc.order_place_btn()
        time.sleep(5)
        self.order_details = self.driver.find_elements(By.XPATH, "//ul[@class='woocommerce-thankyou-order-details order_details']/li")
        lists = []
        for order_detail in self.order_details:
            # print(order_detail.text)
            lists.append(order_detail.text)

        print(lists)

        print("Your order number is:- ", lists[0])
        print("Date of booking is:- ", lists[1])
        print("Total price is:- ",lists[2])
        print("Your Payment method is:- ", lists[3])











