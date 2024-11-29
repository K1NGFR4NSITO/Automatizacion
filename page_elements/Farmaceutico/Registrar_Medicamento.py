from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from applitools.selenium import Eyes, Target
import time
 
class TestAtt:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000')
        time.sleep(5)
       
    def teardown_method(self):
        self.driver.quit()
        time.sleep(5)
    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")
 
    def test_verify_imei(self):
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@href='/auth/register']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        time.sleep(5)
        actual = self.driver.find_element(By.XPATH, "//div[@class = 'alert note note-warning']//strong").text
        print("++++++++",actual)
        esperado = "Usted no puede realizar mas consultas que las realizadas"
        assert actual == esperado