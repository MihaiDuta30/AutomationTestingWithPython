from selenium.webdriver.common.by import By


class DeleteAccount:
    account_deleted_selector = ".col-sm-9 .title b"  # css selector
    continue_delete_button_selector = ".col-sm-9 .pull-right .btn"  # css selector

    def __init__(self, driver):
        self.driver = driver
        self.account_deleted = driver.find_element(By.CSS_SELECTOR, self.account_deleted_selector)
        self.continue_delete_button = driver.find_element(By.CSS_SELECTOR, self.continue_delete_button_selector)
