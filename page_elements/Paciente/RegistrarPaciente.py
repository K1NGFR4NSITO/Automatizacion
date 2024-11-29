from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración automática del WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Maximizar la ventana del navegador
driver.maximize_window()

# Abrir url en el navegador
driver.get('https://www.multicine.com.bo/register')

# Espera hasta que el botón 'LA PAZ' sea interactuable
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()= ' LA PAZ ']"))).click()

# Aceptar pop-up
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()= 'Aceptar']"))).click()

# Llenar el formulario
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name= 'firstname' ]"))).send_keys("Jorge")
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name= 'lastname' ]"))).send_keys("Lima")
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name= 'address' ]"))).send_keys("jorgelima@gmail.com")

# Seleccionar una opción de ion-select
wait.until(EC.element_to_be_clickable((By.XPATH, "//ion-select[@name='mySelect']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class= 'alert-radio-group sc-ion-alert-md']"))).click()

# Elegir el sexo
wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text() = 'Hombre']//input[@id = 'sex']"))).click()

# Escribir la contraseña
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name= 'reg_passwd__' ]"))).send_keys("Gato1234")

# Seleccionar la fecha de nacimiento
wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='day']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@name= 'birthday_day' ]//option[text() = '17']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@name= 'birthday_month' ]//option[text() = 'ago']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@name= 'birthday_year' ]//option[text() = '2002']"))).click()

# Enviar el formulario
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name= 'websubmit' ]"))).click()

# Cerrar el navegador después de un pequeño tiempo
time.sleep(3)
driver.quit()

print("Prueba visual completada")
