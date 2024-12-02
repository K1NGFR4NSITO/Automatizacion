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
       self.driver.find_element(By.XPATH, "//span[@id='telefono_proveedor']").click()
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



        
        