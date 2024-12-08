import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from create_contact_function import generate_random_contact
from selenium.webdriver.firefox.options import Options as FirefoxOptions



class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    #self.driver = webdriver.Chrome()
    # options = webdriver.FirefoxOptions()
    # self.driver = webdriver.Remote( 
    # command_executor="http://localhost:4444/wd/hub",options=options)


  def teardown_method(self, method):
        self.driver.quit()
      
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



