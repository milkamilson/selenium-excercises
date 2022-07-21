from unittest import TestCase

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep as slep


class TestRadioButtons(TestCase):
    def setUp(self):
        self.url = 'https://demo.seleniumeasy.com/basic-radiobutton-demo.html'
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        slep(3)
        try:
            close_popup_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[2]/a')
            close_popup_button.click()
        except NoSuchElementException:
            pass
        self.radio_button_male = self.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[1]/div['
                                                                    '2]/label[1]/input')
        self.radio_button_female = self.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[1]/div['
                                                                      '2]/label[2]/input')
        self.check_button = self.driver.find_element(By.ID, 'buttoncheck')
        self.output_message = self.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[1]/div[2]/p[3]')

    def test_radio_button_check_male(self):
        self.radio_button_male.click()

        self.assertTrue(not self.radio_button_female.is_selected())
        self.check_button.click()
        self.assertEqual('Radio button \'Male\' is checked', self.output_message.text)

    def test_radio_button_check_female(self):
        self.radio_button_female.click()

        self.assertTrue(not self.radio_button_male.is_selected())
        self.check_button.click()
        self.assertEqual('Radio button \'Female\' is checked', self.output_message.text)

    def test_radio_button_check_none(self):
        self.assertTrue(not self.radio_button_male.is_selected())
        self.assertTrue(not self.radio_button_female.is_selected())
        self.check_button.click()
        self.assertEqual('Radio button is Not checked', self.output_message.text)

    def tearDown(self) -> None:
        self.driver.quit()
        print('good job')

