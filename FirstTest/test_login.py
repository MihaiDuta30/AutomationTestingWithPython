from selenium import webdriver
from selenium.webdriver.common.by import By
from web_selectors import LoginPage
import time


def main():
    driver = webdriver.Chrome()
    login(driver)

    driver.quit()


def login(driver):
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, LoginPage.username)
    password = driver.find_element(By.ID, LoginPage.password)
    button = LoginPage.button

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    LoginPage.button.click()

    time.sleep(2)
    element = driver.find_element(By.CLASS_NAME, "title")
    assert element.text == "Products", f"Actual title: {element.text}"


main()
