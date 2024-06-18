from selenium import webdriver
from homepage_selectors import HomePage as HP, LoggedInHomePage
from signup_login_selectors import Login
from delete_account_page_selectors import DeleteAccount
import time


def second_test():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/")
    driver.maximize_window()
    home_page(driver)
    login_user_test(driver)


def home_page(driver):
    page = HP(driver)

    # Check if homepage is visible
    assert page.homepage_check.text == "FEATURES ITEMS", f"Actual Title: {page.homepage_check.text}"
    time.sleep(2)

    # Click on 'Signup / Login' button
    page.signup_button.click()
    time.sleep(2)


def login_user_test(driver):
    login = Login(driver)

    # Verify 'Login to your account' is visible
    assert login.login_check.text == "Login to your account", f"Actual text: {login.login_check.text}"

    # Enter correct email address and password
    login.user_email.send_keys(login.login_email)
    login.user_password.send_keys(login.login_password)

    # Click 'login' button
    login.login_button.click()


def logged_in_page_test(driver):
    logged_in_page = LoggedInHomePage(driver)

    # Verify that 'Logged in as username' is visible
    assert logged_in_page.logged_in.text == f"Logged in as test21", f"Actual text: {logged_in_page.logged_in.text}"

    # Click 'Delete Account' button
    logged_in_page.delete_account.click()


def account_deleted_page_test(driver):
    account_deleted_page = DeleteAccount(driver)

    # Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    assert account_deleted_page.account_deleted.text == "ACCOUNT DELETED!", f"Actual text: {account_deleted_page.account_deleted.text}"
    account_deleted_page.continue_delete_button.click()


second_test()
