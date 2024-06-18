from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    homepage_check_selector = ".features_items .title"  # css selector
    signup_button_selector = ".shop-menu .nav .fa.fa-lock"  # css selector

    def __init__(self, driver):
        self.driver = driver
        self.homepage_check = self.driver.find_element(By.CSS_SELECTOR, self.homepage_check_selector)
        self.signup_button = self.driver.find_element(By.CSS_SELECTOR, self.signup_button_selector)


class LoggedInHomePage:
    logged_in_selector = "div.col-sm-8 > div > ul > li:nth-child(10)"  # css selector
    delete_account_selector = ".nav .fa.fa-trash-o"  # css selector

    def __init__(self, driver):
        self.driver = driver
        self.logged_in = self.driver.find_element(By.CSS_SELECTOR, self.logged_in_selector)
        self.delete_account = self.driver.find_element(By.CSS_SELECTOR, self.delete_account_selector)