from unittest import TestCase

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep as slep

class TestCheckboxDemo(TestCase):
    def setUp(self):
        self.url = 'https://demo.seleniumeasy.com/basic-checkbox-demo.html'
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        slep(3)
        try:
            close_popup_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[2]/a')
            close_popup_button.click()
        except NoSuchElementException:
            pass
        self.option_1 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/label/input')
        self.option_2 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]/label/input')
        self.option_3 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[3]/label/input')
        self.option_4 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[4]/label/input')
        self.check_all = self.driver.find_element(By.ID, 'check1')

    def test_single_checkbox(self):
        checkbox = self.driver.find_element(By.ID, 'isAgeSelected')
        checkbox.click()
        success_message = self.driver.find_element(By.ID, 'txtAge')
        success_message.value_of_css_property('display')
        self.assertEqual('block', success_message.value_of_css_property('display'))

    def test_multiple_checkbox_select_button(self):
        self.check_all.click()
        self.assertTrue(self.option_1.is_selected())
        self.assertTrue(self.option_2.is_selected())
        self.assertTrue(self.option_3.is_selected())
        self.assertTrue(self.option_4.is_selected())

    def test_multiple_checkbox_rename_button(self):
        self.check_all.click()
        self.assertEqual('Uncheck All', self.check_all.get_attribute('value'))

    def test_multiple_checkbox_uncheck_change(self):
        self.option_1.click()
        self.option_2.click()
        self.option_3.click()
        self.option_4.click()
        self.option_1.click()
        self.assertEqual('Check All', self.check_all.get_attribute('value'))

    def tearDown(self) -> None:
        self.driver.quit()
        print('good job')
