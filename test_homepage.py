from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import time

class TestContactPage():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        

    def teardown_method(self, method):
        self.driver.quit()

    #testing the logo
    def test_logo(self):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        elements = self.driver.find_elements(By.XPATH, "//footer/img")

    #testing the table
    def test_table(self):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        assert self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(1)").text == "Name"
        assert self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(2)").text == "Birthdate"
        assert self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(3)").text == "Email"
        assert self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(4)").text == "Phone"
        assert self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(5)").text == "Address"
        assert self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(6)").text == "City, State/Province, Postal Code"
        assert self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(7)").text == "Country"

    #testing the copy rights in the footer
    def test_copy_rights_declaration(self):
        self.driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "email").send_keys("sjsj@sjsj.com")
        self.driver.find_element(By.ID, "password").send_keys("sjsjsjsj")
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(3)
        assert "Created by Kristin Jackvony, Copyright 2021" in self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(1)").text

    