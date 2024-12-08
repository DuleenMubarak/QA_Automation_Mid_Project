from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import pytest
import time
from create_contact_function import generate_random_contact
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class TestContactsList():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        #self.driver=webdriver.Chrome()
        # options = webdriver.FirefoxOptions()
        # self.driver = webdriver.Remote(
        # command_executor="http://localhost:4444/wd/hub",options=options)

    def teardown_method(self, method):
        self.driver.quit()
  
  #adding a new contact
    def test_add_new_contact(self):
        contact=generate_random_contact()
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
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
        assert self.driver.find_element(By.XPATH, "//h1[contains(.,\'Contact List\')]").text == "Contact List"


    #editing an existing contact

    def test_edit_existing_contact(self):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//table[@id=\'myTable\']/tr/td[2]").click()
        self.driver.find_element(By.ID, "edit-contact").click()
        time.sleep(1)
        ActionChains(self.driver).double_click(self.driver.find_element(By.ID, "firstName")).perform()
        self.driver.find_element(By.ID, "firstName").send_keys("edited")
        ActionChains(self.driver).double_click(self.driver.find_element(By.ID, "lastName")).perform()
        self.driver.find_element(By.ID, "lastName").send_keys("edited")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "return").click()
        time.sleep(3)
        assert "edited edited" in self.driver.find_element(By.ID, "myTable").text  
    
#deleting an existing account

    def test_delete_existing_contact(self):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//table[@id=\'myTable\']/tr/td[2]").click()
        time.sleep(3)
        element = self.driver.find_element(By.ID, "phone").text
        #self.driver.find_element(By.CSS_SELECTOR, ".contactTableBodyRow:nth-child(3) > td:nth-child(2)").click()
        self.driver.find_element(By.ID, "delete").click()
        time.sleep(3)
        assert self.driver.switch_to.alert.text == "Are you sure you want to delete this contact?"
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        assert element not in self.driver.find_element(By.ID, "myTable").text

        #@adding empty input contact

    def test_adding_empty_input_contact(self):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "add-contact").click()
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        error=self.driver.find_element(By.ID, "error").text
        assert  "Contact validation failed" in error

        #adding a contact with filling the required fields only

    def test_required_fields_only(self):
        contact=generate_random_contact()
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "add-contact").click()
        self.driver.find_element(By.ID, "firstName").send_keys(contact["first_name"])
        self.driver.find_element(By.ID, "lastName").send_keys(contact["last_name"])
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        assert self.driver.find_element(By.XPATH, "//h1[contains(.,\'Contact List\')]").text == "Contact List"

#adding a contact with a missing required field

    def test_missing_required_fields(self):
        contact=generate_random_contact()
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "add-contact").click()
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
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        error=self.driver.find_element(By.ID, "error").text
        assert  "Contact validation failed" in error

        #adding a contact with invalid email format
    def test_invalid_email(self):
        contact=generate_random_contact()
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "add-contact").click()
        self.driver.find_element(By.ID, "firstName").send_keys(contact["first_name"])
        self.driver.find_element(By.ID, "lastName").send_keys(contact["last_name"])
        self.driver.find_element(By.ID, "birthdate").send_keys(contact["birthday"])
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj")
        self.driver.find_element(By.ID, "phone").send_keys(contact["phone"])
        self.driver.find_element(By.ID, "street1").send_keys(contact["street_address_1"])
        self.driver.find_element(By.ID, "street2").send_keys(contact["street_address_2"])
        self.driver.find_element(By.ID, "city").send_keys(contact["city"])
        self.driver.find_element(By.ID, "stateProvince").send_keys(contact["state"])
        self.driver.find_element(By.ID, "postalCode").send_keys(contact["postal_code"])
        self.driver.find_element(By.ID, "country").send_keys(contact["country"])
        time.sleep(3)
        self.driver.find_element(By.ID, "submit").click()
        error=self.driver.find_element(By.ID, "error").text
        assert  "Contact validation failed" in error

#localization

    def test_localization_arabic(self):
        contact=generate_random_contact()
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "add-contact").click()
        self.driver.find_element(By.ID, "firstName").send_keys("احمد")
        self.driver.find_element(By.ID, "lastName").send_keys("محمد")
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
        assert self.driver.find_element(By.XPATH, "//h1[contains(.,\'Contact List\')]").text == "Contact List"


