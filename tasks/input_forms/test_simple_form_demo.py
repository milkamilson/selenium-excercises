from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from unittest import TestCase


class TestSimpleFormDemo(TestCase):
    def setUp(self):
        self.url = 'http://demo.seleniumeasy.com/basic-first-form-demo.html'
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        sleep(3)
        try:
            close_popup_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[2]/a')
            close_popup_button.click()
        except NoSuchElementException:
            pass
        self.value_a_box = self.driver.find_element(By.ID, 'sum1')
        self.value_b_box = self.driver.find_element(By.ID, 'sum2')
        self.get_total_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')
        self.total_a_b = self.driver.find_element(By.ID, 'displayvalue')

    def test_single_input_field(self):
        user_input = 'message'
        msg_box_input = self.driver.find_element(By.ID, 'user-message')
        msg_box_input.clear()
        msg_box_input.send_keys(user_input)
        button = self.driver.find_element(By.XPATH, '//*[@id="get-input"]/button')
        button.click()
        msg_box_output = self.driver.find_element(By.ID, 'display')
        self.assertEqual(user_input, msg_box_output.text)

    def test_two_input_fields_numbers(self):
        self.value_a_box.clear()
        self.value_b_box.clear()
        numbers_input_a = 5
        numbers_input_b = 7

        self.value_a_box.send_keys(str(numbers_input_a))
        self.value_b_box.send_keys(str(numbers_input_b))
        self.get_total_button.click()
        self.assertEqual(str(numbers_input_a + numbers_input_b), self.total_a_b.text)

    def test_two_input_fields_words(self):
        self.value_a_box.clear()
        self.value_b_box.clear()
        words_input_a = 'asdfsa'
        words_input_b = 'fsdfs'

        self.value_a_box.send_keys(words_input_a)
        self.value_b_box.send_keys(words_input_b)
        self.get_total_button.click()
        self.assertEqual('NaN', self.total_a_b.text)

    def tearDown(self) -> None:
        self.driver.quit()
        print('good job')




