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
        #self.driver=webdriver.Chrome()
        # options = webdriver.FirefoxOptions()
        # self.driver = webdriver.Remote(
        # command_executor="http://localhost:4444/wd/hub",options=options)


    def teardown_method(self, method):
        self.driver.quit()
    
    #testing the contacts details data preservation
    @pytest.mark.demo
    def test_data_preservation(self):
        #creating new user and new contact 
        user=generate_random_contact()
        contact=generate_random_contact()

        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        
        #signing up
        self.driver.find_element(By.ID, "signup").click()
        self.driver.find_element(By.ID, "firstName").send_keys(user["first_name"])
        self.driver.find_element(By.ID, "lastName").send_keys(user["last_name"])
        self.driver.find_element(By.ID, "email").send_keys(user["email"])
        self.driver.find_element(By.ID, "password").send_keys("djdjdjdj")
        self.driver.find_element(By.ID, "submit").click()
        
        #adding a new contact
        time.sleep(3)
        self.driver.find_element(By.ID, "add-contact").click()
        self.driver.find_element(By.ID, "firstName").send_keys(contact["first_name"])
        self.driver.find_element(By.ID, "lastName").send_keys(contact["last_name"])
        self.driver.find_element(By.ID, "birthdate").send_keys(contact["birthday"])
        self.driver.find_element(By.ID, "email").send_keys(contact["email"])
        self.driver.find_element(By.ID, "phone").send_keys(contact["phone"])
        self.driver.find_element(By.ID, "street1").send_keys(contact["street_address_1"])
        self.driver.find_element(By.ID, "street2").send_keys(contact["street_address_2"])
        self.driver.find_element(By.ID, "city").send_keys(contact["city"])
        self.driver.find_element(By.ID, "stateProvince").send_keys(contact["state"])
        self.driver.find_element(By.ID, "postalCode").send_keys(contact["postal_code"])
        self.driver.find_element(By.ID, "country").send_keys(contact["country"])
        time.sleep(3)
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        
        #remembering the full name
        Res_contact = self.driver.find_element(By.XPATH, "//table[@id=\'myTable\']/tr/td[2]").text
        
        #loging out
        self.driver.find_element(By.ID, "logout").click()
        time.sleep(2)
        
        #closing the browser
        self.driver.close()
        
        #reopening the browser
        time.sleep(2)
        self.driver = webdriver.Firefox()
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        
        #sign in
        self.driver.find_element(By.ID, "email").send_keys(user["email"])
        self.driver.find_element(By.ID, "password").send_keys("djdjdjdj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)

        assert Res_contact in self.driver.find_element(By.XPATH, "//table[@id=\'myTable\']/tr/td[2]").text
    
    #testing saving the user details
    def test_user_details_preservation(self):
        user=generate_random_contact()
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "signup").click()
        self.driver.find_element(By.ID, "firstName").send_keys(user["first_name"])
        self.driver.find_element(By.ID, "lastName").send_keys(user["last_name"])
        self.driver.find_element(By.ID, "email").send_keys(user["email"])
        self.driver.find_element(By.ID, "password").send_keys("djdjdjdj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        assert self.driver.find_element(By.ID,"logout")
        self.driver.find_element(By.ID, "logout").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "email").send_keys(user["email"])
        self.driver.find_element(By.ID, "password").send_keys("djdjdjdj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        assert self.driver.find_element(By.ID,"logout")
        self.driver.quit()


        
