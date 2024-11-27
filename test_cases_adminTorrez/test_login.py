from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
 
class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000/auth/login')
        time.sleep(5)
        
    def teardown_method(self):
        self.driver.quit()
        #esto es para el inicio de sesion, logout y volver a iniciar sesion
        # esperando el mensaje de error de correo y contraseña incorrectos
    print("prueba visual completada")
    def test_Inputs_Login_Correctos_Y_Mensaje_Error(self):
        self.driver.find_element(By.XPATH,"//input[@inputid='email1']").send_keys("chorizo@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@inputid='password1']").send_keys("qweQWE123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component w-full p-3 text-xl bg-orange-400']").click()
        time.sleep(2)
        #logout para hacer el test erroneo
        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component ml-3 p-button-danger']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@inputid='email1']").send_keys("crizo@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@inputid='password1']").send_keys("qweQWE123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component w-full p-3 text-xl bg-orange-400']").click()
        time.sleep(2)
        #funciona
        #para imprimir el error de contraseña o correo incorrectos
    def test_Inputs__Login_Verificacion(self):
        #email @ y contraseña sin Mayus
        self.driver.find_element(By.XPATH,"//input[@inputid='email1']").send_keys("chorizogmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component w-full p-3 text-xl bg-orange-400']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@inputid='password1']").send_keys("qweqweq123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component w-full p-3 text-xl bg-orange-400']").click()
        time.sleep(2)
        
    def test_Inputs__Login_Verificacion_2(self):
        #email sin . y contraseña sin 123
        self.driver.find_element(By.XPATH,"//input[@inputid='email1']").send_keys("chorizo@gmailcom")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='p-button p-component w-full p-3 text-xl bg-orange-400']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@inputid='password1']").send_keys("qweqweqqweqwe")
        time.sleep(2)
        #actual = self.driver.find_element(By.XPATH, "//div[@class='p-toast-detail']").text
        #print("+++++++++",actual)
        #esperado = "inexistente"
        #assert actual == esperado