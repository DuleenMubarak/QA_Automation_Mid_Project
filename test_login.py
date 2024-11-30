import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from create_contact_function import generate_random_contact



class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    #self.driver = webdriver.Chrome()
  

  # test valid user details login
  def test_successful_login(self):
    self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
    self.driver.maximize_window()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
    self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
    self.driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    assert self.driver.find_element(By.ID,"logout")
    
   # testing invalid user login 
  @pytest.mark.xfail
  def test_invalid_user_login(self):
    self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
    self.driver.maximize_window()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("fail@sjsj.com")
    self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
    self.driver.find_element(By.ID, "submit").click()
    time.sleep(2)  
    assert self.driver.find_element(By.ID,"logout")

# testing loging in with valid user and invalid password 
  @pytest.mark.xfail
  def test_invalid_password_login(self):
    self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
    self.driver.maximize_window()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
    self.driver.find_element(By.ID, "password").send_keys("sjsjsjsjfail")
    self.driver.find_element(By.ID, "submit").click()
    time.sleep(2)  
    assert self.driver.find_element(By.ID,"logout") 
   
# testing empty input
  @pytest.mark.xfail  
  def test_empty_input(self):
    self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
    self.driver.maximize_window()
    self.driver.find_element(By.ID, "submit").click()
    time.sleep(2)  
    assert self.driver.find_element(By.ID,"logout")

  #testing logout
  def test_logout(self):
    self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
    self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
    self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
    self.driver.find_element(By.ID, "submit").click()
    time.sleep(3)
    assert self.driver.find_element(By.ID, "logout").text == "Logout"
    self.driver.find_element(By.ID, "logout").click()
    time.sleep(3)
    assert self.driver.find_element(By.CSS_SELECTOR, ".main-content > p:nth-child(1)").text == "Log In:"









"""
#options - selenium Grid
from selenium.webdriver.firefox.options import Options as FirefoxOptions
#from selenium.webdriver.chrome.options import Options as ChromeOptions
options=FirefoxOptions()
options.set_capability("browserVersion","132.0.2")
options.set_capability("platformName","Windows")

driver=webdriver.Remote("http://192.168.1.60:4444/",options=FirefoxOptions())
driver.get("https://google.com")
driver.maximize_window()
time.sleep(5)
print(driver.title)
driver.quit

#@pytest.fixture
def driver():
    #driver=webdriver.Chrome()
    driver=webdriver.Firefox()
    driver.maximize_window()
    yield driver
    #driver.quit()


#print(generate_random_contacts(10))
#@pytest.mark.parametrize("fist_name, last_name, birthday, email, phone, street_address_1, street_address_2,city, state, postal code, country",generate_random_contacts(100))

"""