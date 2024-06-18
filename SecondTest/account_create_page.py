from selenium.webdriver.common.by import By


class AccountCreate:
    account_created_selector = ".col-sm-9 .title"  # css selector
    continue_button_selector = ".col-sm-9 .pull-right a[data-qa='continue-button']"  # css selector

    def __init__(self, driver):
        self.driver = driver
        self.account_created = driver.find_element(By.CSS_SELECTOR, self.account_created_selector)
        self.continue_button = driver.find_element(By.CSS_SELECTOR, self.continue_button_selector)
