import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestFarmacia:
    def setup_method(self):
        # Configuración inicial
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def teardown_method(self):
        # Cerrar el navegador después de cada prueba
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        # Navegar a la página de login
        driver.get('http://localhost:3000')
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 100);")
        time.sleep(1)
        
        # Completar el formulario de login
        driver.find_element(By.XPATH, "//input[@inputid='email1']").send_keys('fabri@gmail.com')
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@inputid='password1']").send_keys('Fabri123')
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[@class='p-button-label p-c']").click()
        time.sleep(3)
    
    def test_registrar_producto(self):
        driver = self.driver
        self.test_login()  # Reutilizamos el login

        # Navegar al formulario de nuevo producto
        driver.get('http://localhost:3000/farmproductos/nuevoProducto')
        time.sleep(2)

        # Completar el formulario de registro
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
        input_element.clear()
        input_element.send_keys('11')  # Precio
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@class='p-button p-component p-datepicker-trigger p-button-icon-only']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[@tabindex='0']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@name='cantidad']").send_keys('2')
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@aria-label='Registrar']").click()
        time.sleep(2)

    def test_modificar_producto(self):
        driver = self.driver
        self.test_login()  # Reutilizamos el login

        # Navegar a la gestión de productos
        driver.get('http://localhost:3000/farmproductos')
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@type='search']").send_keys('Tonico')
        time.sleep(4)
        driver.find_element(By.XPATH, "//button[@class='p-button p-component mr-2 p-button-icon-only p-button-rounded p-button-info']").click()
        time.sleep(2)

        # Modificar el producto
        driver.find_element(By.XPATH, "//input[@id='nombre_medicamento']").clear()
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
        input_element.clear()
        input_element.send_keys('15')  # Nuevo precio
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@class='p-button p-component p-datepicker-trigger p-button-icon-only']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[@class='p-datepicker-next-icon pi pi-chevron-right']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[text()='26']").click()
        driver.find_element(By.XPATH, "//input[@name='cantidad']").clear()
        driver.find_element(By.XPATH, "//input[@name='cantidad']").send_keys('5')
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@aria-label='Guardar']").click()
        time.sleep(2)

# Para ejecutar las pruebas:
# pytest -v nombre_del_archivo.py
