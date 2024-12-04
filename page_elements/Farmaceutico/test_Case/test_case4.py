from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestReabastecimiento:
    def setup_method(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def teardown_method(self):
        """Cierra el navegador después de cada prueba."""
        self.driver.quit()

    def login(self):
        """Inicia sesión en el sistema."""
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

    def test_registrar_reabastecimiento(self):
        """Prueba para registrar un nuevo reabastecimiento."""
        self.login()  # Reutiliza el método de inicio de sesión
        self.driver.get('http://localhost:3000/farmreabastecimiento/nuevoReabaste')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='producto_id']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//li[@aria-label='Paracetamol']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[@id='proveedor_id']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//li[@aria-label='Distribuidora Condo']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='cantidad_reabastecida']").send_keys('2')
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component p-datepicker-trigger p-button-icon-only']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//td[@class='p-datepicker-today']").click()
        time.sleep(1)
        input_element = self.driver.find_element(By.XPATH, "//input[@name='costo_total']")
        input_element.clear()  # Limpia el contenido del input
        input_element.send_keys('11')  # Ingresa el valor
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, 100);")
        self.driver.find_element(By.XPATH, "//button[@aria-label='Registrar']").click()
        time.sleep(3)

       

    def test_actualizar_reabastecimiento(self):
        """Prueba para actualizar un reabastecimiento existente."""
        self.login()  # Reutiliza el método de inicio de sesión
        self.driver.get('http://localhost:3000/farmreabastecimiento')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component mr-2 p-button-icon-only p-button-rounded p-button-info']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[@id='producto_id']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//li[@aria-label='Paracetamol']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[@id='proveedor_id']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//li[@aria-label='Distribuidora Condo']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='cantidad_reabastecida']").clear()
        self.driver.find_element(By.XPATH, "//input[@name='cantidad_reabastecida']").send_keys('3')  # Nueva cantidad
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component p-datepicker-trigger p-button-icon-only']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//td[@class='p-datepicker-today']").click()
        time.sleep(1)
        input_element = self.driver.find_element(By.XPATH, "//input[@name='costo_total']")
        input_element.clear()  # Limpia el contenido del input
        input_element.send_keys('15')  # Nuevo valor
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@aria-label='Guardar']").click()
        time.sleep(3)

       
