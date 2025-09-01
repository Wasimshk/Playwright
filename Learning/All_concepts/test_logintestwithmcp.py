# test_logintestwithmcp.py
# Selenium test using Page Object Model for login and product verification

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.CSS_SELECTOR, "input#username")
        self.password_input = (By.CSS_SELECTOR, "input#password")
        self.checkbox = (By.CSS_SELECTOR, "input[type='checkbox']")
        self.signin_button = (By.CSS_SELECTOR, "input#signInBtn")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.signin_button).click()

class ShopPage:
    def __init__(self, driver):
        self.driver = driver
    def is_iphone_x_present(self):
        try:
            # Looks for product card with 'iphone X' text
            self.driver.find_element(By.XPATH, "//h4[contains(text(), 'iphone X')]")
            return True
        except:
            return False

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_and_verify_iphone_x(driver):
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = LoginPage(driver)
    login_page.login("rahulshettyacademy", "learning")
    # Wait for navigation to shop page
    WebDriverWait(driver, 10).until(EC.url_contains("/angularpractice/shop"))
    shop_page = ShopPage(driver)
    assert shop_page.is_iphone_x_present(), "iphone X product not found on the shop page!"
