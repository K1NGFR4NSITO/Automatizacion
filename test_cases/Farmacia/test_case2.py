from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestProveedor:
    def setup_method(self):
        
        # Configuración del driver utilizando Service
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def teardown_method(self):
        
        self.driver.quit()

    def login(self):
        
        self.driver.get('http://localhost:3000')
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0, 100);")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@inputid='email1']").send_keys('fabri@gmail.com')
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@inputid='password1']").send_keys('Fabri123')
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[@class='p-button-label p-c']").click()
        time.sleep(3)

    def test_registrar_proveedor(self):
        
        self.login()
        self.driver.get('http://localhost:3000/farmproveedores/nuevoProveedor')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='nombre_proveedor']").send_keys('AlabinAlabon20')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='representante']").send_keys('a')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='telefono']").send_keys('70567038')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//textarea[@id='descripcion']").send_keys('a')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@aria-label='Registrar']").click()
        
        time.sleep(2)

        
        

    def test_actualizar_proveedor(self):
        
        self.login()
        self.driver.get('http://localhost:3000/farmproveedores')
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//span[text()='Actualizar proveedor']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type='search']").send_keys('AlabinAlabon')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component mr-2 p-button-icon-only p-button-rounded p-button-info']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='nombre_proveedor']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='nombre_proveedor']").send_keys('Proveedor Actualizado')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='representante']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='representante']").send_keys('b')
        time.sleep(2)
        input_element = self.driver.find_element(By.XPATH, "//input[@inputmode='numeric']")
        input_element.clear()
        time.sleep(2)
        input_element.send_keys('70707070')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//textarea[@id='descripcion_proveedor']").clear()
        self.driver.find_element(By.XPATH, "//textarea[@id='descripcion_proveedor']").send_keys('Descripción Actualizada')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@aria-label='Guardar']").click()
        time.sleep(2)


