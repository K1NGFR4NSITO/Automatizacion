from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
class TestFarmacia:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000/auth/login')
        time.sleep(5)
 
    def teardown_method(self):
        self.driver.quit()
    def test_Registrar_Nueva_Categoria(self):
        self.driver.find_element(By.XPATH,"//input[@inputid='email1']").send_keys("chorizo@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@inputid='password1']").send_keys("qweQWE123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component w-full p-3 text-xl bg-orange-400']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='nombre']").send_keys("Medicamentos")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//textarea[@id='descripcion']").send_keys("Categoría para medicamentos genéricos")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'bg-orange-500')]/span[contains(text(), 'Registrar')]").click()
        time.sleep(2)

    def test_Limpiar_Formulario(self):
        self.driver.find_element(By.XPATH, "//input[@id='nombre']").send_keys("Temporal")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//textarea[@id='descripcion']").send_keys("Descripción temporal")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'p-button-outlined')]/span[contains(text(), 'Limpiar')]").click()
        time.sleep(2)
    def test_Registrar_Nuevo_Producto(self):
        self.driver.find_element(By.XPATH, "//input[@id='nombre_medicamento']").send_keys("Paracetamol")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[text()='Proveedores']/following-sibling::div[contains(@class, 'p-dropdown')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//li[normalize-space(text())='Proveedor XYZ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[text()='Categoria Productos']/following-sibling::div[contains(@class, 'p-dropdown')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//li[normalize-space(text())='Analgésicos']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[@id='precio']//input").send_keys("10.50")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[@id='cantidad']//input").send_keys("100")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[@id='fecha_caducidad']//input").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//td[contains(@class, 'p-datepicker-today')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'bg-orange-500')]/span[contains(text(), 'Registrar')]").click()
        time.sleep(2)
    def test_Limpiar_Formulario(self):
        self.driver.find_element(By.XPATH, "//input[@id='nombre_medicamento']").send_keys("Temporal")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[text()='Proveedores']/following-sibling::div[contains(@class, 'p-dropdown')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//li[normalize-space(text())='Proveedor Temporal']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[text()='Categoria Productos']/following-sibling::div[contains(@class, 'p-dropdown')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//li[normalize-space(text()='Temporal']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'p-button-outlined')]/span[contains(text(), 'Limpiar')]").click()
        time.sleep(2)
    def test_busqueda_producto(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Buscar producto...']").send_keys("Paracetamol")
        time.sleep(2)
        resultados = self.driver.find_elements(By.XPATH, "//td[contains(text(), 'Paracetamol')]")
        assert len(resultados) > 0, "El producto no fue encontrado."
    def test_editar_nombre_producto(self):
        self.driver.find_element(By.XPATH, "//td[contains(text(), 'Paracetamol')]").click()
        time.sleep(2)
        nombre_input = self.driver.find_element(By.XPATH, "//input[@id='nombre_medicamento']")
        nombre_input.clear()
        nombre_input.send_keys("Paracetamol 500mg")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'Guardar')]]").click()
        time.sleep(2)
    def test_eliminar_producto(self):
        self.driver.find_element(By.XPATH, "//td[contains(text(), 'Paracetamol')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//td[contains(text(), 'Paracetamol')]/following-sibling::td//span[contains(@class, 'pi-times')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'Si')]]").click()
        time.sleep(2)
    def test_cancelar_eliminar_producto(self):
        self.driver.find_element(By.XPATH, "//td[contains(text(), 'Paracetamol')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//td[contains(text(), 'Paracetamol')]/following-sibling::td//span[contains(@class, 'pi-times')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'No')]]").click()
        time.sleep(2)
    def test_buscar_producto_metformina(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Buscar producto...']").send_keys("Metformina")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//td[contains(text(), 'Metformina')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'Habilitar Productos')]]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'Si')]]").click()
        time.sleep(2)
    def test_cancelar_habilitar_producto_metformina(self):

        self.driver.find_element(By.XPATH, "//input[@placeholder='Buscar producto...']").send_keys("Metformina")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//td[contains(text(), 'Metformina')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'Habilitar Productos')]]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'No')]]").click()
        time.sleep(2)
    def test_verificar_sin_productos_inactivos(self):
    # Intentar buscar "Metformina" en la tabla después de habilitarla
       self.driver.find_element(By.XPATH, "//input[@placeholder='Buscar producto...']").send_keys("Metformina")
       time.sleep(2)

    # Verificar mensaje de "No se encontraron productos disponibles"
       self.driver.find_element(By.XPATH, "//td[contains(text(), 'No se encontraron productos disponibles.')]")
       time.sleep(2)
    def test_registrar_proveedor_correctamente(self):
       self.driver.find_element(By.XPATH, "//input[@id='nombre_proveedor']").send_keys("Proveedor ABC")
       time.sleep(1)
       self.driver.find_element(By.XPATH, "//input[@id='representante']").send_keys("Juan Pérez")
       time.sleep(1)
       self.driver.find_element(By.XPATH, "//input[@id='telefono']").send_keys("12345678")
       time.sleep(1)
       self.driver.find_element(By.XPATH, "//textarea[@id='descripcion']").send_keys("Proveedor confiable de productos farmacéuticos.")
       time.sleep(1)
       self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'Registrar')]]").click()
       time.sleep(2)
    def test_registrar_proveedor_sin_datos(self):
    # Dejar todos los campos vacíos y hacer clic en "Registrar"
       self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'Registrar')]]").click()
       time.sleep(2)
    def test_registrar_proveedor_con_datos_parciales(self):
       self.driver.find_element(By.XPATH, "//input[@id='nombre_proveedor']").send_keys("Proveedor Incompleto")
       time.sleep(1)
       self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'Registrar')]]").click()
       time.sleep(2)
    def test_limpiar_formulario_proveedor(self):
       self.driver.find_element(By.XPATH, "//input[@id='nombre_proveedor']").send_keys("Proveedor Temporal")
       time.sleep(1)
       self.driver.find_element(By.XPATH, "//input[@id='representante']").send_keys("Carlos Méndez")
       time.sleep(1)
       self.driver.find_element(By.XPATH, "//input[@id='telefono']").send_keys("87654321")
       time.sleep(1)
       self.driver.find_element(By.XPATH, "//textarea[@id='descripcion']").send_keys("Descripción temporal.")
       time.sleep(1)
       self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'Limpiar')]]").click()
       time.sleep(2)
    def test_buscar_proveedor(self):
       self.driver.find_element(By.XPATH, "//input[@placeholder='Buscar nombre...']").send_keys("Farcomed")
       time.sleep(2)
       self.driver.find_element(By.XPATH, "//td[contains(text(), 'Farcomed')]").click()
       time.sleep(2)
    def test_editar_proveedor_completamente(self):
       self.driver.find_element(By.XPATH, "//input[@placeholder='Buscar nombre...']").send_keys("Farcomed")
       time.sleep(2)
       self.driver.find_element(By.XPATH, "//td[contains(text(), 'Farcomed')]/following-sibling::td//span[contains(@class, 'pi-pencil')]").click()
       time.sleep(2)
       self.driver.find_element(By.XPATH, "//input[@id='nombre_proveedor']").clear()
       self.driver.find_element(By.XPATH, "//input[@id='nombre_proveedor']").send_keys("Farcomed Internacional")
       time.sleep(1)
       self.driver.find_element(By.XPATH, "//input[@id='representante']").clear()
       self.driver.find_element(By.XPATH, "//input[@id='representante']").send_keys("Juan Pérez")
       time.sleep(1)
       self.driver.find_element(By.XPATH, "//span[@id='telefono_proveedor']").click()  # Clic para activar
       self.driver.find_element(By.XPATH, "//span[@id='telefono_proveedor']/input").clear()
       self.driver.find_element(By.XPATH, "//span[@id='telefono_proveedor']/input").send_keys("987654321")
       time.sleep(1)
       self.driver.find_element(By.XPATH, "//textarea[@id='descripcion_proveedor']").clear()
       self.driver.find_element(By.XPATH, "//textarea[@id='descripcion_proveedor']").send_keys("Proveedor confiable especializado en productos médicos.")
       time.sleep(1)
       self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'Guardar')]]").click()
       time.sleep(2)
    def test_eliminar_proveedor(self):
       self.driver.find_element(By.XPATH, "//input[@placeholder='Buscar nombre...']").send_keys("Farcomed")
       time.sleep(2)
       self.driver.find_element(By.XPATH, "//td[contains(text(), 'Farcomed')]/following-sibling::td//span[contains(@class, 'pi-times')]").click()
       time.sleep(2)
       self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'Si')]]").click()
       time.sleep(2)
    def test_cancelar_eliminar_proveedor(self):
       self.driver.find_element(By.XPATH, "//input[@placeholder='Buscar nombre...']").send_keys("Farcomed")
       time.sleep(2)
       self.driver.find_element(By.XPATH, "//td[contains(text(), 'Farcomed')]/following-sibling::td//span[contains(@class, 'pi-times')]").click()
       time.sleep(2)
       self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'No')]]").click()
       time.sleep(2)
    def test_buscar_proveedor(self):
       self.driver.find_element(By.XPATH, "//input[@placeholder='Buscar nombre...']").send_keys("Farcomed")
       time.sleep(2)
       self.driver.find_element(By.XPATH, "//td[contains(text(), 'Farcomed')]").click()
       time.sleep(2)
    def test_reactivar_proveedor_especifico(self):
       self.driver.find_element(By.XPATH, "//input[@placeholder='Buscar nombre...']").send_keys("Farcomed")
       time.sleep(2)
       self.driver.find_element(By.XPATH, "//td[contains(text(), 'Farcomed')]/following-sibling::td//span[contains(@class, 'pi-undo')]").click()
       time.sleep(2)
       self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'Si')]]").click()
       time.sleep(2)
    def test_cancelar_reactivar_proveedor(self):
       self.driver.find_element(By.XPATH, "//input[@placeholder='Buscar nombre...']").send_keys("Farcomed")
       time.sleep(2)
       self.driver.find_element(By.XPATH, "//td[contains(text(), 'Farcomed')]/following-sibling::td//span[contains(@class, 'pi-undo')]").click()
       time.sleep(2)
       self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'No')]]").click()
       time.sleep(2)
    def test_reactivar_todos_los_proveedores(self):
       self.driver.find_element(By.XPATH, "//th//div[contains(@class, 'p-checkbox-box')]").click()
       time.sleep(2)
       self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'Reactivar productos')]]").click()
       time.sleep(2)
       self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'Si')]]").click()
       time.sleep(2)
    def test_cancelar_reactivar_todos(self):
       self.driver.find_element(By.XPATH, "//th//div[contains(@class, 'p-checkbox-box')]").click()
       time.sleep(2)
       self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'Reactivar productos')]]").click()
       time.sleep(2)
       self.driver.find_element(By.XPATH, "//button[span[contains(text(), 'No')]]").click()
       time.sleep(2)






       









    
