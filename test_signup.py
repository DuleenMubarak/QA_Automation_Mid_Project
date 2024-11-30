import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from create_contact_function import generate_random_contact


class TestSignup():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()
#signing up with valid details   
    def test_valid_details_sign_up(self):
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
#signing up with short password
    def test_short_password_sing_in(self):
        contact=generate_random_contact()
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "signup").click()
        self.driver.find_element(By.ID, "firstName").send_keys(contact["first_name"])
        self.driver.find_element(By.ID, "lastName").send_keys(contact["last_name"])
        self.driver.find_element(By.ID, "email").send_keys(contact["email"])
        self.driver.find_element(By.ID, "password").send_keys("djdjdj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        assert self.driver.find_element(By.ID, "error")

#signing up with invalid password chars
    @pytest.mark.xfail
    def test_invalid_chars_in_password_sing_up(self):
        contact=generate_random_contact()
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "signup").click()
        self.driver.find_element(By.ID, "firstName").send_keys(contact["first_name"])
        self.driver.find_element(By.ID, "lastName").send_keys(contact["last_name"])
        self.driver.find_element(By.ID, "email").send_keys(contact["email"])
        self.driver.find_element(By.ID, "password").send_keys("djdjאאj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        assert self.driver.find_element(By.ID, "error")

#signing up with invalid username
    @pytest.mark.xfail
    def test_invalid_chars_in_username_sing_up(self):
        contact=generate_random_contact()
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "signup").click()
        self.driver.find_element(By.ID, "firstName").send_keys("Saeed!")
        self.driver.find_element(By.ID, "lastName").send_keys(contact["last_name"])
        self.driver.find_element(By.ID, "email").send_keys(contact["email"])
        self.driver.find_element(By.ID, "password").send_keys("djdjdjdj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        assert self.driver.find_element(By.ID, "error")

#testing username length limitation in sign up  

    def test_long_username_sing_up(self):
        contact=generate_random_contact()
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "signup").click()
        self.driver.find_element(By.ID, "firstName").send_keys("SaeedSaadAhmadMahmoud")
        self.driver.find_element(By.ID, "lastName").send_keys(contact["last_name"])
        self.driver.find_element(By.ID, "email").send_keys(contact["email"])
        self.driver.find_element(By.ID, "password").send_keys("djdjdjdj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        assert self.driver.find_element(By.ID, "error")
    
    #signing up with registered email
    def test_sign_up_with_registered_email(self):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.find_element(By.ID, "signup").click()
        self.driver.find_element(By.ID, "firstName").send_keys("sjsj")
        self.driver.find_element(By.ID, "lastName").send_keys("sjsj")
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "submit").click()
        assert self.driver.find_element(By.ID, "error")