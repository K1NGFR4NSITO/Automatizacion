from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestVenta:
    def setup_method(self):
        """Configuración inicial: abre el navegador."""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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

    def verificar_ausencia_de_errores(self):
        """Verifica que no existan mensajes de error en la página."""
        errores = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'error')]")
        assert len(errores) == 0, "Se encontraron mensajes de error en la página"

    def test_registrar_venta(self):
        """Prueba para registrar una nueva venta."""
        self.login()  # Reutiliza el método de inicio de sesión
        self.driver.get('http://localhost:3000/farmventas/nuevaVenta')
        time.sleep(2)

        cantidad_vendida = "5"  # Cantidad que vamos a validar
        cliente = "Eduardo Gabriel Arancibia Lopez"  # Cliente seleccionado

        # Seleccionar producto
        self.driver.find_element(By.XPATH, "//div[@aria-label='Seleccione un Producto']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//li[@aria-label='Paracetamol']").click()
        time.sleep(1)

        # Ingresar cantidad vendida
        cantidad_input = self.driver.find_element(By.XPATH, "//input[@name='cantidad_vendida']")
        cantidad_input.clear()
        cantidad_input.send_keys(cantidad_vendida)
        time.sleep(1)

        # Validar que el campo contiene la cantidad ingresada
        actual_cantidad = cantidad_input.get_attribute("value")
        assert cantidad_vendida == actual_cantidad, f"Falla: Se esperaba cantidad '{cantidad_vendida}' pero se obtuvo '{actual_cantidad}'"

        # Seleccionar cliente
        self.driver.find_element(By.XPATH, "//button[@aria-label='Buscar']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, f"//li[text()='{cliente}']").click()
        time.sleep(1)

        # Registrar venta
        self.driver.find_element(By.XPATH, "//button[@aria-label='Registrar']").click()
        time.sleep(3)

        # Verificar ausencia de errores
        self.verificar_ausencia_de_errores()

    def test_actualizar_venta(self):
        """Prueba para actualizar una venta existente."""
        self.login()  # Reutiliza el método de inicio de sesión
        self.driver.get('http://localhost:3000/farmventas')
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component mr-2 p-button-icon-only p-button-rounded p-button-info']").click()
        time.sleep(1)

        # Actualizar la cantidad vendida
        nueva_cantidad = "10"  # Nueva cantidad que vamos a validar
        cantidad_input = self.driver.find_element(By.XPATH, "//input[@name='cantidad_vendida']")
        cantidad_input.clear()
        cantidad_input.send_keys(nueva_cantidad)
        time.sleep(1)

        # Validar que el campo contiene la nueva cantidad ingresada
        actual_cantidad = cantidad_input.get_attribute("value")
        assert nueva_cantidad == actual_cantidad, f"Falla: Se esperaba cantidad '{nueva_cantidad}' pero se obtuvo '{actual_cantidad}'"

        # Guardar cambios
        self.driver.find_element(By.XPATH, "//button[@aria-label='Guardar']").click()
        time.sleep(3)

        # Verificar ausencia de errores
        self.verificar_ausencia_de_errores()
