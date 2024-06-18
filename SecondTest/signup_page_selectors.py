from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignupPage:
    account_information_check_selector = ".container div > h2 b"  # css selector
    title_select_selector = "id_gender1"  # id
    password_selector = "password"  # id
    dob_day_selector = "days"  # id
    dob_month_selector = "months"  # id
    dob_year_selector = "years"  # id
    newsletter_selector = "newsletter"  # id
    optin_selector = "optin"  # id
    firstname_selector = "first_name"  # id
    lastname_selector = "last_name"  # id
    company_selector = "company"  # id
    address1_selector = "address1"  # id
    address2_selector = "address2"  # id
    country_selector = "country"  # id
    state_selector = "state"  # id
    city_selector = "city"  # id
    zipcode_selector = "zipcode"  # id
    mobile_number_selector = "mobile_number"  # id
    create_account_selector = ".login-form button[data-qa='create-account']"  # css selector

    def __init__(self, driver):
        self.driver = driver
        self.account_information_check = driver.find_element(By.CSS_SELECTOR, self.account_information_check_selector)
        self.title_select = driver.find_element(By.ID, self.title_select_selector)
        self.password = driver.find_element(By.ID, self.password_selector)
        self.signup_password = "123"
        self.dob_day = Select(driver.find_element(By.ID, self.dob_day_selector))
        self.dob_month = Select(driver.find_element(By.ID, self.dob_month_selector))
        self.dob_year = Select(driver.find_element(By.ID, self.dob_year_selector))
        self.newsletter = driver.find_element(By.ID, self.newsletter_selector)
        self.optin = driver.find_element(By.ID, self.optin_selector)
        self.first_name = driver.find_element(By.ID, self.firstname_selector)
        self.last_name = driver.find_element(By.ID, self.lastname_selector)
        self.company = driver.find_element(By.ID, self.company_selector)
        self.address1 = driver.find_element(By.ID, self.address1_selector)
        self.address2 = driver.find_element(By.ID, self.address2_selector)
        self.country = Select(driver.find_element(By.ID, self.country_selector))
        self.state = driver.find_element(By.ID, self.state_selector)
        self.city = driver.find_element(By.ID, self.city_selector)
        self.zipcode = driver.find_element(By.ID, self.zipcode_selector)
        self.mobile_number = driver.find_element(By.ID, self.mobile_number_selector)
        self.create_account = driver.find_element(By.CSS_SELECTOR, self.create_account_selector)
