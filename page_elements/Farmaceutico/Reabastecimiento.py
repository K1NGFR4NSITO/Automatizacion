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
#Registrar reabastecimiento 
driver.get('http://localhost:3000/farmreabastecimiento/nuevoReabaste')
time.sleep(2)
driver.find_element(By.XPATH, "//div[@id='producto_id']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='Paracetamol']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[@id='proveedor_id']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='Distribuidora Condo']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@name='cantidad_reabastecida']").send_keys('2')
time.sleep(1)
driver.find_element(By.XPATH, "//button[@class='p-button p-component p-datepicker-trigger p-button-icon-only']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//td[@class='p-datepicker-today']").click()
time.sleep(1)
input_element = driver.find_element(By.XPATH, "//input[@name='costo_total']")
input_element.clear()  # Limpia el contenido del input
input_element.send_keys('1')  # Ingresa el nuevo valor
input_element.send_keys('1') 
driver.execute_script("window.scrollBy(0, 100);")

time.sleep(2)

driver.find_element(By.XPATH, "//button[@aria-label='Registrar']").click()
time.sleep(3)

#actualizar proovedor 

driver.find_element(By.XPATH, "//a[@href='/farmreabastecimiento']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class='p-button p-component mr-2 p-button-icon-only p-button-rounded p-button-info']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//div[@id='producto_id']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='Paracetamol']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[@id='proveedor_id']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//li[@aria-label='Distribuidora Condo']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@name='cantidad_reabastecida']").send_keys('2')
time.sleep(1)
driver.find_element(By.XPATH, "//button[@class='p-button p-component p-datepicker-trigger p-button-icon-only']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//td[@class='p-datepicker-today']").click()
time.sleep(1)
input_element = driver.find_element(By.XPATH, "//input[@name='costo_total']")
input_element.clear()  # Limpia el contenido del input
input_element.send_keys('1')  # Ingresa el nuevo valor
input_element.send_keys('1') 
time.sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Guardar']").click()
time.sleep(3)