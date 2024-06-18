from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


class LoginPage:
    username = 'user-name'
    password = 'password'
    # button = 'login-button'
    button = driver.find_element(By.ID, 'login-button')
