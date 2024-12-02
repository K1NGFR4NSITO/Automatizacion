from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


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
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@inputid='password1']").send_keys("Qwerty123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component w-full p-3 text-xl bg-orange-400']").click()
        time.sleep(3)
        # Hacer clic en el enlace "Historia Clinica"
        self.driver.find_element(By.XPATH, "//a[@href='/pacientes/historiaClinica']").click()
        time.sleep(2)  # Ajusta el tiempo de espera según sea necesario
        self.driver.find_element(By.XPATH, "//span[@class='p-button-icon p-c pi pi-chevron-down']").click()
        time.sleep(2)  # Ajusta el tiempo de espera según sea necesario
        self.driver.find_element(By.XPATH, "//li[contains(text(), 'Maria Rodriguez')]").click()
        time.sleep(2)  # Ajusta el tiempo de espera según sea necesario
        # Presionar el botón "Crear historia medica"
        self.driver.find_element(By.XPATH, "//button[@aria-label='Crear historia medica']").click()
        time.sleep(2)  # Ajusta el tiempo de espera según sea necesario
        self.driver.find_element(By.ID, "motivo_consulta").send_keys("dolor")
        time.sleep(2)  # Ajusta el tiempo de espera según sea necesario
        # Ingresar "gripe" en el campo de enfermedad actual
        self.driver.find_element(By.ID, "enfermedad_actual").send_keys("gripe")
        time.sleep(2)  # Ajusta el tiempo de espera según sea necesario
        self.driver.find_element(By.ID, "diagnostico_cie").send_keys("aaaaa")
        time.sleep(2)  
        self.driver.find_element(By.XPATH, "//textarea[@class='p-inputtextarea p-inputtext p-component p-inputtextarea-resizable']").send_keys("aaaaa")
        time.sleep(1)  # Ajusta el tiempo de espera según sea necesario
        self.driver.find_element(By.XPATH, "//textarea[@class='p-inputtextarea p-inputtext p-component p-inputtextarea-resizable']").send_keys("enfermo")
        time.sleep(1)  # Ajusta el tiempo de espera según sea necesario
        self.driver.find_element(By.XPATH, "//textarea[@class='p-inputtextarea p-inputtext p-component p-inputtextarea-resizable']").send_keys("descansito")
        time.sleep(1)  # Ajusta el tiempo de espera según sea necesario
        self.driver.find_element(By.XPATH, "//textarea[@class='p-inputtextarea p-inputtext p-component p-inputtextarea-resizable']").send_keys("ta enfermito")
        time.sleep(1) 
        # Campos con máscaras o restricciones
        masked_input = self.driver.find_element(By.XPATH, "//input[@class='p-inputtext p-component p-inputmask']")
        masked_input.clear()
        masked_input.send_keys("360/00")
        time.sleep(1)

        # Peso
        peso_input = self.driver.find_element(By.ID, "peso")
        self.driver.execute_script("arguments[0].value = '70,00'; arguments[0].dispatchEvent(new Event('input'));", peso_input)
        time.sleep(1)

        # Talla
        talla_input = self.driver.find_element(By.ID, "talla")
        self.driver.execute_script("arguments[0].value = '1,75'; arguments[0].dispatchEvent(new Event('input'));", talla_input)
        time.sleep(1)

        # Temperatura corporal
        temp_input = self.driver.find_element(By.ID, "temperatura_corporal")
        self.driver.execute_script("arguments[0].value = '37,5'; arguments[0].dispatchEvent(new Event('input'));", temp_input)
        time.sleep(1) 

        self.driver.find_element(By.XPATH, "//input[@id='frecuencia_respiratoria']").send_keys("18")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='frecuencia_cardiaca']").send_keys("72")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='saturacion_oxigeno']").send_keys("98")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//textarea[@class='p-inputtextarea p-inputtext p-component p-inputtextarea-resizable']").send_keys("Ta bien")
        time.sleep(1) 
        self.driver.find_element(By.XPATH, "//textarea[@class='p-inputtextarea p-inputtext p-component p-inputtextarea-resizable']").send_keys("Tabien")
        time.sleep(50)  
        # Habilitar el botón utilizando JavaScrip












