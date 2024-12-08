from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class TestButtonsFuncionality():

    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        # self.driver=webdriver.Chrome()
        # options = webdriver.FirefoxOptions()
        # self.driver = webdriver.Remote(
        # command_executor="http://localhost:4444/wd/hub",options=options)
        

    def teardown_method(self, method):
        self.driver.quit()
  
    #testing the submit button in log in page
    
    def test_submit_button_login_page(self):

        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.find_element(By.ID, "submit").click()
        assert self.driver.find_elements(By.ID, "error")


    #testing the sign up button in log in page
    def test_sign_up_button_login_page(self):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.set_window_size(1158, 640)
        self.driver.find_element(By.ID, "signup").click()
        assert self.driver.find_elements(By.XPATH, "//p[contains(.,\'Sign up to begin adding your contacts!\')]")

    #testing the log out button in contacts list page
    def test_log_out_button_contacts_page(self):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[contains(.,\'Logout\')]").click()
        time.sleep(2)
        assert self.driver.find_elements(By.CSS_SELECTOR, ".main-content > p:nth-child(1)")

    #testing add a new contact button
    def test_add_a_new_contact_button(self):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "add-contact").click()
        assert self.driver.find_elements(By.XPATH, "//h1[contains(.,\'Add Contact\')]")

    #testing the submit button in add a new contact page
    def test_submit_button_in_new_contact_page(self):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "add-contact").click()
        self.driver.find_element(By.ID, "submit").click()
        assert self.driver.find_element(By.ID, "error")

    #testing the cancel button in add a new contact page
    def test_cancel_button_in_new_contact_page(self):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "add-contact").click()
        self.driver.find_element(By.ID, "cancel").click()
        assert self.driver.find_elements(By.ID, "add-contact")

    
    #testing the edit button in the contact page
    def test_edit_button_in_contact_page(self):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//table[@id=\'myTable\']/tr/td[2]").click()
        self.driver.find_element(By.ID, "edit-contact").click()
        assert self.driver.find_elements(By.XPATH, "//h1[contains(.,\'Edit Contact\')]")
    
    #testing the delete button in the contact page
    def test_delete_button_in_contact_page(self):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//table[@id=\'myTable\']/tr/td[2]").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "delete").click()
        time.sleep(2)
        assert self.driver.switch_to.alert.text == "Are you sure you want to delete this contact?"
    





