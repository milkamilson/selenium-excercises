from unittest import TestCase

from parameterized import parameterized
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep as slep

NAME_INPUTS = [
    ["first_name"],
    ["last_name"],
]


class TestInputFormDemo(TestCase):
    def setUp(self):
        self.url = 'https://demo.seleniumeasy.com/input-form-demo.html'
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        # slep(3)
        # try:
        #     close_popup_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[2]/a')
        #     close_popup_button.click()
        # except NoSuchElementException:
        #     pass

    def test_no_output_message(self):
        invalid_elements = self.driver.find_elements(By.XPATH, '//*[@data-bv-result="INVALID"]')
        valid_elements = self.driver.find_elements(By.XPATH, '//*[@data-bv-result="VALID"]')
        not_validated_elements = self.driver.find_elements(By.XPATH, '//*[@data-bv-result="NOT_VALIDATED"]')
        self.assertEqual([], invalid_elements)
        self.assertEqual([], valid_elements)
        self.assertNotEqual([], not_validated_elements)

    def get_input(self, name):
        return self.driver.find_element(
            By.XPATH, '//form[@id="contact_form"]/descendant::input[@name="' + name + '"]')

    def get_error_message_for_input(self, name):
        invalid_elements = self.driver.find_elements(
            By.XPATH, '//small[@data-bv-result="INVALID" and @data-bv-for="' + name + '"]')
        self.assertIn(len(invalid_elements), [0, 1])
        return invalid_elements[0].text if len(invalid_elements) > 0 else None

    @parameterized.expand([
        ["first_name"],
        ["last_name"],
    ])
    def test_name_too_short(self, name):
        first_name_box = self.get_input(name)
        first_name_box.send_keys('s')
        message = self.get_error_message_for_input(name)
        self.assertEqual('Please enter more than 2 characters', message)

    @parameterized.expand([
        ["first_name", "Please supply your first name"],
        ["last_name", "Please supply your last name"],
    ])
    def test_name_empty(self, name, expected_message):
        first_name_box = self.get_input(name)
        first_name_box.send_keys('s')
        first_name_box.send_keys(Keys.BACKSPACE)
        message = self.get_error_message_for_input(name)
        self.assertEqual(expected_message, message)

    @parameterized.expand([
        ["first_name"],
        ["last_name"],
    ])
    def test_name_goog(self, name):
        first_name_box = self.get_input(name)
        first_name_box.send_keys('sd')
        message = self.get_error_message_for_input(name)
        self.assertIsNone(message)

    def tearDown(self) -> None:
        self.driver.quit()
        print('goog job')
