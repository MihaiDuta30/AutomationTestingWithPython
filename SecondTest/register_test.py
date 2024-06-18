from selenium import webdriver
from homepage_selectors import HomePage as HP, LoggedInHomePage
from signup_login_selectors import Signup
from signup_page_selectors import SignupPage
from account_create_page import AccountCreate
from delete_account_page_selectors import DeleteAccount
import time


def first_test():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/")
    driver.maximize_window()
    home_page(driver)
    signup_test(driver)
    signup_page_test(driver)
    account_create_page_test(driver)
    logged_in_page_test(driver)
    account_deleted_page_test(driver)


def home_page(driver):
    page = HP(driver)

    # Check if homepage is visible
    assert page.homepage_check.text == "FEATURES ITEMS", f"Actual Title: {page.homepage_check.text}"
    time.sleep(2)

    # Click on 'Signup / Login' button
    page.signup_button.click()
    time.sleep(2)


def signup_test(driver):
    signup = Signup(driver)

    # Verify 'New User Signup!' is visible
    assert signup.signup_check.text == "New User Signup!", f"Actual text: {signup.signup_check.text}"

    # Enter name and email address
    signup.name.send_keys(signup.signup_username)
    signup.email.send_keys(signup.signup_email)
    time.sleep(2)

    # Click 'Signup' button
    signup.new_user_signup_button.click()


def signup_page_test(driver):
    signup_page = SignupPage(driver)
    # Verify that 'ENTER ACCOUNT INFORMATION' is visible
    assert signup_page.account_information_check.text == "ENTER ACCOUNT INFORMATION", f"Actual text: {signup_page.account_information_check.text}"

    # Fill details: Title, Name, Email, Password, Date of birth
    signup_page.title_select.click()
    signup_page.password.send_keys(signup_page.signup_password)
    signup_page.dob_day.select_by_index(25)
    signup_page.dob_month.select_by_index(8)
    signup_page.dob_year.select_by_value('1995')

    # Select checkbox 'Sign up for our newsletter!'
    signup_page.newsletter.click()

    # Select checkbox 'Receive special offers from our partners!'
    signup_page.optin.click()

    # Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    signup_page.first_name.send_keys("Dan")
    signup_page.last_name.send_keys("Andrei")
    signup_page.company.send_keys("Sogefi SRL")
    signup_page.address1.send_keys("Mioveni, Ipswich")
    signup_page.address2.send_keys("Str. Gheorghe")
    signup_page.country.select_by_value('Australia')
    signup_page.state.send_keys("Queensland")
    signup_page.city.send_keys("Brisbane")
    signup_page.zipcode.send_keys("117751")
    signup_page.mobile_number.send_keys("0758625412")

    # Click 'Create Account button'
    signup_page.create_account.click()


def account_create_page_test(driver):
    account_create_page = AccountCreate(driver)

    # Verify that 'ACCOUNT CREATED!' is visible
    assert account_create_page.account_created.text == "ACCOUNT CREATED!", f"Actual text: {account_create_page.account_created.text}"

    # Click 'Continue' button
    account_create_page.continue_button.click()


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


first_test()
