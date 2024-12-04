from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestVenta:
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

    def test_registrar_venta(self):
        
        self.login()  # Reutiliza el método de inicio de sesión
        self.driver.get('http://localhost:3000/farmventas/nuevaVenta')
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//div[@aria-label='Seleccione un Producto']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//li[@aria-label='Paracetamol']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='cantidad_vendida']").send_keys('1')
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@aria-label='Buscar']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//li[text()='Eduardo Gabriel Arancibia Lopez']").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//button[@aria-label='Registrar']").click()
        time.sleep(3)

        

    def test_actualizar_venta(self):
        """Prueba para actualizar una venta existente."""
        self.login()  
        self.driver.get('http://localhost:3000/farmventas')
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component mr-2 p-button-icon-only p-button-rounded p-button-info']").click()
        time.sleep(1)

        # Actualizar la cantidad vendida
        cantidad_input = self.driver.find_element(By.XPATH, "//input[@name='cantidad_vendida']")
        time.sleep(2)
        cantidad_input.send_keys('2')  # Nueva cantidad
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//button[@aria-label='Guardar']").click()
        time.sleep(3)

        
