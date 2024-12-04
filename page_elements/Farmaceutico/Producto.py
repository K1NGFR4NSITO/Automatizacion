from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from applitools.selenium import Eyes, Target
import time
driver = webdriver.Chrome()
driver.maximize_window()

#//li[@class="active-menuitem"]
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

#print('La fecha de hoy es:'+solucion)//span[text()="Nuevo producto"]Gestion de Productos
driver.get('http://localhost:3000/farmproductos/nuevoProducto')

time.sleep(2)
#Registrando medicamento

driver.find_element(By.XPATH, "//input[@id='nombre_medicamento']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='nombre_medicamento']").send_keys('Tonico')
time.sleep(2)
driver.find_element(By.XPATH, "//div[@id='proveedor_id']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//li[@aria-label='Distribuidora Condo']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@id='categoria_id']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//li[@aria-label='Analgésicos']").click()
time.sleep(1)
input_element = driver.find_element(By.XPATH, "//input[@name='precio']")
input_element.clear()  # Limpia el contenido del input
input_element.send_keys('1')  # Ingresa el nuevo valor
input_element.send_keys('1') 
time.sleep(1)
driver.find_element(By.XPATH, "//button[@class='p-button p-component p-datepicker-trigger p-button-icon-only']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[@tabindex='0']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@name='cantidad']").send_keys('2')
driver.find_element(By.XPATH, "//button[@aria-label='Registrar']").click()
time.sleep(2)
####


#Pasando a modificar producto

driver.find_element(By.XPATH, "//a[@href='/farmproductos']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@type='search']").send_keys('Tonico')
time.sleep(4) 
driver.find_element(By.XPATH, "//button[@class='p-button p-component mr-2 p-button-icon-only p-button-rounded p-button-info']").click()
time.sleep(2)
#Modificando medicamento
###

driver.find_element(By.XPATH, "//input[@id='nombre_medicamento']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='nombre_medicamento']").send_keys('Tonico1')
time.sleep(2)
driver.find_element(By.XPATH, "//div[@id='proveedor_id']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//li[@aria-label='Distribuidora Condo']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@id='categoria_id']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//li[@aria-label='Analgésicos']").click()
time.sleep(1)
input_element = driver.find_element(By.XPATH, "//input[@name='precio']")
input_element.clear()  # Limpia el contenido del input
input_element.send_keys('1')  # Ingresa el nuevo valor
input_element.send_keys('1') 
time.sleep(1)
driver.find_element(By.XPATH, "//button[@class='p-button p-component p-datepicker-trigger p-button-icon-only']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[@class='p-datepicker-next-icon pi pi-chevron-right']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[text()='26']").click()
driver.find_element(By.XPATH, "//input[@name='cantidad']").send_keys('2')
time.sleep(1)
driver.find_element(By.XPATH, "//button[@aria-label='Guardar']").click()
time.sleep(2)

