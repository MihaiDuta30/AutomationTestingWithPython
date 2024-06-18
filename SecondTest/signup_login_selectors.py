from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    login_check_selector = ".login-form h2"  # css selector
    user_email_selector = ".login-form input[data-qa='login-email']"  # css selector
    user_password_selector = ".login-form input[data-qa='login-password']"  # css selector
    login_button_selector = ".col-sm-4 .login-form .btn"  # css selector

    def __init__(self, driver):
        self.driver = driver
        self.login_check = driver.find_element(By.CSS_SELECTOR, self.login_check_selector)
        self.user_email = driver.find_element(By.CSS_SELECTOR, self.user_email_selector)
        self.user_password = driver.find_element(By.CSS_SELECTOR, self.user_password_selector)
        self.login_email = "test21@test.com"
        self.login_password = "123"
        self.login_button = driver.find_element(By.CSS_SELECTOR, self.login_button_selector)


class Signup:
    signup_check_selector = ".signup-form h2"  # css selector
    name_selector = ".col-sm-4 .signup-form input[data-qa='signup-name']"  # css selector
    email_selector = ".col-sm-4 .signup-form input[data-qa='signup-email']"  # css selector
    new_user_signup_button_selector = ".col-sm-4 .signup-form .btn"  # css selector

    def __init__(self, driver):
        self.driver = driver
        self.signup_check = driver.find_element(By.CSS_SELECTOR, self.signup_check_selector)
        self.name = driver.find_element(By.CSS_SELECTOR, self.name_selector)
        self.email = driver.find_element(By.CSS_SELECTOR, self.email_selector)
        self.signup_username = "test21"
        self.signup_email = "test21@test.com"
        self.new_user_signup_button = driver.find_element(By.CSS_SELECTOR, self.new_user_signup_button_selector)
