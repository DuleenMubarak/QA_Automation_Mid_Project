import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from create_contact_function import generate_random_contact

#from selenium.webdriver.chrome.service import Service


class TestLogin():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
    #testing the contacts details data preservation
    def test_data_preservation(self):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        contact = self.driver.find_element(By.XPATH, "//table[@id=\'myTable\']/tr/td[2]").text
        self.driver.find_element(By.ID, "logout").click()
        #self.driver.close()
        time.sleep(2)
        #self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        assert contact in self.driver.find_element(By.XPATH, "//table[@id=\'myTable\']/tr/td[2]").text
    
    #testing saving the user details
    def test_used_details_preservation(self):
        contact=generate_random_contact()
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "signup").click()
        self.driver.find_element(By.ID, "firstName").send_keys(contact["first_name"])
        self.driver.find_element(By.ID, "lastName").send_keys(contact["last_name"])
        self.driver.find_element(By.ID, "email").send_keys(contact["email"])
        self.driver.find_element(By.ID, "password").send_keys("djdjdjdj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        assert self.driver.find_element(By.ID,"logout")
        self.driver.find_element(By.ID, "logout").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "email").send_keys(contact["email"])
        self.driver.find_element(By.ID, "password").send_keys("djdjdjdj")
        self.driver.find_element(By.ID, "submit").click()
        assert self.driver.find_element(By.ID,"logout")
        self.driver.quit()


        
'''
    #a function that closes the current browser session and reopens it, navigating to the mentioned URL
    def close_and_reopen_browser(self,driver, driver_path, url):
        
        # Close the current browser session
        self.driver.quit()
        time.sleep(2)  
        # Reopen the browser and return the new WebDriver instance
        new_driver = webdriver.Chrome(service=Service(driver_path))
        new_driver.maximize_window()
        new_driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        return new_driver
'''