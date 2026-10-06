import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_exitoso():
    driver = webdriver.Edge()

    try:
        driver.get("https://www.saucedemo.com/")

        usario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID, "login-button")

        usario.  send_keys("standard_user")
        password.send_keys("secret_sauce")

        boton_login.click()

        assert "/inventory.html" in driver.current_url
        
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"

        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
        assert titulo.text == "Products"

    finally:
        driver.quit()
        


