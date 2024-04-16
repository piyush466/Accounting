from selenium import webdriver
from selenium.webdriver.common.by import By

class Shoppage:
    click_shop_xpath = "//a[text()='Shop']"
    books_text_xpath = '//h3'
    btn_add_to_basket_xpath = "//a[text()='Add to basket']"
    items_xpath = "//a[@title='View your shopping cart']"
    proceed_check_xpath = "//a[@class='checkout-button button alt wc-forward']"

    def __init__(self,driver):
        self.driver= driver

    def click_on_shop(self):
        self.driver.find_element(By.XPATH, self.click_shop_xpath).click()

    def Select_books(self):
        self.driver.find_elements(By.XPATH, self.books_text_xpath)

    def button_click(self):
        self.driver.find_element(By.XPATH, self.btn_add_to_basket_xpath).click()

    def click_items(self):
        self.driver.find_element(By.XPATH, self.items_xpath).click()

    def proceed_checkout(self):
        self.driver.find_element(By.XPATH, self.proceed_check_xpath).click()

