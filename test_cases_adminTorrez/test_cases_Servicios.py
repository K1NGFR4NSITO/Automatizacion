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
        self.driver.find_element(By.XPATH, "//i[@class = 'layout-menuitem-icon pi pi-fw pi-user-plus']").click()
        