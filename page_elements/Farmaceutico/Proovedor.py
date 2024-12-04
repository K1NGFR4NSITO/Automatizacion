from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from applitools.selenium import Eyes, Target
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.maximize_window()
#loggin
driver.get('http://localhost:3000')
time.sleep(1)
driver.execute_script("window.scrollBy(0, 100);")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@inputid='email1']").send_keys('fabri@gmail.com')
time.sleep(1)
driver.find_element(By.XPATH, "//input[@inputid='password1']").send_keys('Fabri123')
time.sleep(1)
driver.find_element(By.XPATH, "//span[@class='p-button-label p-c']").click()
time.sleep(3)
#loggin

#Registrar proovedor 
driver.get('http://localhost:3000/farmproveedores/nuevoProveedor')

time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='nombre_proveedor']").send_keys('AlabinAlabon')
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='representante']").send_keys('a')
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='telefono']").send_keys('70567038')
time.sleep(2)
driver.find_element(By.XPATH, "//textarea[@id='descripcion']").send_keys('a')
time.sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Registrar']").click()
registrar_btn = driver.find_element(By.XPATH, "//button[@aria-label='Registrar']")
registrar_btn.send_keys(Keys.ENTER)
#Actualizar
time.sleep(3)

driver.find_element(By.XPATH, "//span[text()='Actualizar proveedor']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='search']").send_keys('AlabinAlabon')
time.sleep(2)

driver.find_element(By.XPATH, "//button[@class='p-button p-component mr-2 p-button-icon-only p-button-rounded p-button-info']").click()
time.sleep(2)
#actualizar datos del proveedor
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='nombre_proveedor']").send_keys('AlabinAlabon')
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='representante']").send_keys('a')
time.sleep(2)
input_element = driver.find_element(By.XPATH, "//input[@inputmode='numeric']")
input_element.clear()  # Limpia el contenido del input
input_element.send_keys('70707070')  # Ingresa el nuevo valor


time.sleep(2)
driver.find_element(By.XPATH, "//textarea[@id='descripcion_proveedor']").send_keys('a')
time.sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Guardar']").click()
time.sleep(2)
#anular 
driver.find_element(By.XPATH, "//input[@type='search']").send_keys('AlabinAlabon')
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class='p-button p-component p-button-icon-only p-button-rounded p-button-danger']").click()