from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import time
from create_contact_function import generate_random_contact
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class TestContactPage():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        #self.driver=webdriver.Chrome()
        # options = webdriver.FirefoxOptions()
        # self.driver = webdriver.Remote(
        # command_executor="http://localhost:4444/wd/hub",options=options)

    def teardown_method(self, method):
        self.driver.quit()
        
    #testing adding a new contact and checking if all expected fields are visible and populated correctly

    def test_fields_visability_in_contact_page(self):
        contact=generate_random_contact()
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "add-contact").click()
        self.driver.find_element(By.ID, "firstName").send_keys("Zaki")
        self.driver.find_element(By.ID, "lastName").send_keys("Jason")
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
        self.driver.find_element(By.XPATH, "//td[contains(.,\'Zaki Jason\')]").click()
        time.sleep(2)
        assert self.driver.find_element(By.ID, "firstName").text == "Zaki"
        assert self.driver.find_element(By.ID, "lastName").text == "Jason"
        assert self.driver.find_element(By.ID, "birthdate").text == contact["birthday"]
        assert self.driver.find_element(By.ID, "email").text == contact["email"]
        assert self.driver.find_element(By.ID, "phone").text == contact["phone"]
        assert self.driver.find_element(By.ID, "street1").text == contact["street_address_1"]
        assert self.driver.find_element(By.ID, "street2").text == contact["street_address_2"]
        assert self.driver.find_element(By.ID, "city").text == contact["city"]
        assert self.driver.find_element(By.ID, "stateProvince").text == contact["state"]
        assert self.driver.find_element(By.ID, "postalCode").text == contact["postal_code"]
        assert self.driver.find_element(By.ID, "country").text == contact["country"]

    #testing the back button
    def test_back_button(self):
         def test_delete_button_in_contact_page(self):
            self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
            self.driver.maximize_window()
            self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
            self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
            self.driver.find_element(By.ID, "submit").click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//table[@id=\'myTable\']/tr/td[2]").click()
            self.driver.find_element(By.ID, "return").click()
            assert self.driver.find_elements(By.XPATH, "//h1[contains(.,\'Contact List\')]")