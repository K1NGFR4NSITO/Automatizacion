

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración automática del WebDriver
driver = webdriver.Chrome()

# Maximizar la ventana del navegador
driver.maximize_window()

# Abrir url en el navegador
driver.get('https://www.multicine.com.bo/register')
time.sleep(5)


driver.find_element(By.XPATH, "//div[text()= ' LA PAZ ']").click()
driver.find_element(By.XPATH, "//span[text()= 'Aceptar']").click()
time.sleep(5)

driver.get('https://www.multicine.com.bo/register')
time.sleep(2)
# Acciones para interactuar con el navegador
driver.find_element(By.XPATH, "//input[@name= 'firstname' ]").send_keys("Jorge")
driver.find_element(By.XPATH, "//input[@name= 'lastname' ]").send_keys("Lima")
driver.find_element(By.XPATH, "//input[@name= 'address' ]").send_keys("jorgelima@gmail.com")
time.sleep(5)



driver.find_element(By.XPATH, "//ion-select[@name='mySelect']").click()
driver.find_element(By.XPATH, "//div[@class= 'alert-radio-group sc-ion-alert-md']").click()
driver.find_element(By.XPATH, "//button[@id= 'alert-input-8-3']//div[@class='alert-radio-icon sc-ion-alert-md']").click()
driver.find_element(By.XPATH, "//button[@class= 'alert-button ion-focusable ion-activatable sc-ion-alert-md']").click()
time.sleep(2)

# Acciones para interactuar con el navegador

driver.find_element(By.XPATH, "//input[@name= 'reg_passwd__' ]").send_keys("Gato1234")
time.sleep(5)
#driver.find_element(By.XPATH, "LOCATORS").click()

driver.find_element(By.XPATH, "//select[@id='day']").click()

driver.find_element(By.XPATH, "//select[@name= 'birthday_day' ]//option[text() = '17']").click()
driver.find_element(By.XPATH, "//select[@name= 'birthday_month' ]//option[text() = 'ago']").click()
driver.find_element(By.XPATH, "//select[@name= 'birthday_year' ]//option[text() = '2002']").click()

driver.find_element(By.XPATH, "//label[text() = 'Hombre']//input[@id = 'sex']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//button[@name= 'websubmit' ]").click
time.sleep(3)
driver.quit()


print("Prueba visual completada")
