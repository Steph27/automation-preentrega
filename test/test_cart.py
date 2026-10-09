import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Caso de prueba carrito
def test_cart():
    driver = webdriver.Edge()

    wait = WebDriverWait(driver, 10)

    try:
        #Login

        driver.get("https://www.saucedemo.com/")

        #En este login hacemos menos verificaciones ya que estamos enfocados en el carrito

        wait.until(EC.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
        password = driver.find_element(By.ID,"password")
        boton_login = driver.find_element(By.ID,"login-button")

        password.send_keys("secret_sauce")


        boton_login.click()

        #Verificar que el contador del carrito se incremente correctamente  

        primer_producto = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))
        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")

        boton_agregar.click()

        contador_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        assert contador_carrito.text == "1"

        #Navegar dentro del carrito
        #Verificar que puedo clickear el elemento
        
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click() 

        #Verificar que aparece el producto en el carrito

        nombre_producto_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))).text
        assert nombre_producto_carrito == nombre_producto

    finally:
        driver.quit()