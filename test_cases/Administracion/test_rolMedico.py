from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


import time

class TestLoginnn:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000/auth/login')
        time.sleep(5)
 
    def teardown_method(self):
        self.driver.quit()

    def testLogin(self):
        self.driver.find_element(By.XPATH, "//input[@inputid='email1']").send_keys("javier@gmail.com")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@inputid='password1']").send_keys("Qwerty123")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component w-full p-3 text-xl bg-orange-400']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@href='/pacientes/historiaClinica']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[@class='p-button-icon p-c pi pi-chevron-down']").click()
        time.sleep(1)  
        self.driver.find_element(By.XPATH, "//li[contains(text(), 'Veronica')]").click()
        time.sleep(1) 
        self.driver.find_element(By.XPATH, "//button[@aria-label='Crear historia medica']").click()
        time.sleep(1)  
        self.driver.find_element(By.ID, "motivo_consulta").send_keys("a")
        time.sleep(1) 
        self.driver.find_element(By.ID, "enfermedad_actual").send_keys("a")
        time.sleep(1)  
        self.driver.find_element(By.ID, "diagnostico_cie").send_keys("a")
        time.sleep(1)  
        self.driver.find_element(By.XPATH, "//textarea[@class='p-inputtextarea p-inputtext p-component p-inputtextarea-resizable']").send_keys("a")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//textarea[@class='p-inputtextarea p-inputtext p-component p-inputtextarea-resizable']").send_keys("a")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//textarea[@class='p-inputtextarea p-inputtext p-component p-inputtextarea-resizable']").send_keys("a")
        time.sleep(1)  
        self.driver.find_element(By.XPATH, "//textarea[@class='p-inputtextarea p-inputtext p-component p-inputtextarea-resizable']").send_keys("a")
        time.sleep(1) 
        masked_input = self.driver.find_element(By.XPATH, "//input[@class='p-inputtext p-component p-inputmask']")
        masked_input.send_keys(Keys.HOME)
        masked_input.send_keys("20010")
        time.sleep(1)
        peso_input = self.driver.find_element(By.XPATH, "//input[@class='p-inputtext p-component p-filled p-inputnumber-input']")
        peso_input.send_keys(Keys.HOME)
        peso_input.send_keys("7")
        time.sleep(1)
        talla_input = self.driver.find_element(By.XPATH, "//input[@id='talla' and @aria-valuemax='4']")
        talla_input.send_keys(Keys.HOME)
        talla_input.send_keys("1")
        time.sleep(1)
        temp_input = self.driver.find_element(By.XPATH, "//input[@id='temperatura_corporal' and @aria-valuemax='100']")
        temp_input.send_keys(Keys.HOME)
        temp_input.send_keys("3")
        time.sleep(1) 
        self.driver.find_element(By.XPATH, "//input[@id='frecuencia_respiratoria']").send_keys("10")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='frecuencia_cardiaca']").send_keys("10")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='saturacion_oxigeno']").send_keys("10")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//textarea[@class='p-inputtextarea p-inputtext p-component p-inputtextarea-resizable']").send_keys("a")
        time.sleep(1) 
        self.driver.find_element(By.XPATH, "//textarea[@class='p-inputtextarea p-inputtext p-component p-inputtextarea-resizable']").send_keys("a")
        time.sleep(1)  
        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component p-mt-3 bg-orange-500']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@href='/usuarios/consultaMedica']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Busqueda...']").send_keys("Veronica")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component mr-2 p-button-icon-only p-button-rounded p-button-info']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@aria-label='Cerrar']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[@class='p-button-icon p-c pi pi-times']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[.//span[text()='No']]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component mr-2 p-button-icon-only p-button-rounded p-button-success']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//textarea[@class='p-inputtextarea p-inputtext p-component']").send_keys("El paciente muestra mejoría.")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@placeholder='0.00']").send_keys("7")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[@id='altura']//input").send_keys("1")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//textarea[@id='tratamiento']").send_keys("El paciente debe tomar 2 tabletas diarias de paracetamol")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[text()='Registrar']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component mr-2 p-button-icon-only p-button-rounded p-button-warning']//span[@class='p-button-icon p-c pi pi-book']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@aria-label='Cerrar']//span[@class='p-button-icon p-c p-button-icon-left pi pi-times']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@href='/servicios/listarCategorias']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Medicina General y especialidades')]//following-sibling::div//button[@aria-label='Ver servicios']").click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@href='/servicios/listarCategorias']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Servicios medicos')]//following-sibling::div//button[@aria-label='Ver servicios']").click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@href='/servicios/listarCategorias']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Servicios de diagnostico')]//following-sibling::div//button[@aria-label='Ver servicios']").click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@href='/servicios/listarCategorias']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Diagnosticos de cáncer')]//following-sibling::div//button[@aria-label='Ver servicios']").click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@href='/servicios/listarCategorias']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Servicios de Vanguardia')]//following-sibling::div//button[@aria-label='Ver servicios']").click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@href='/servicios/listarCategorias']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@aria-label='Cerrar Sesion']").click()
        time.sleep(3)
        
























