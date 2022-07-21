from unittest import TestCase

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep as slep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TestSelectDropdownList(TestCase):
    def setUp(self):
        self.url = 'https://demo.seleniumeasy.com/basic-select-dropdown-demo.html'
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        slep(3)
        try:
            close_popup_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[2]/a')
            close_popup_button.click()
        except NoSuchElementException:
            pass

    def test_select_list(self):
        self.dropdown_list = Select(self.driver.find_element(By.ID, 'select-demo'))
        self.output_message = self.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[1]/div[2]/p[2]')
        self.dropdown_list.select_by_value('Wednesday')
        self.assertEqual('Day selected :- Wednesday', self.output_message.text)

    def tearDown(self) -> None:
        self.driver.quit()
        print('good job')


class MultiselectDropdownList(TestCase):
    def setUp(self):
        self.url = 'https://demo.seleniumeasy.com/basic-select-dropdown-demo.html'
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        slep(3)
        try:
            close_popup_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[2]/a')
            close_popup_button.click()
        except NoSuchElementException:
            pass

    def test_multiple_select(self):
        multiselect_list = Select(self.driver.find_element(By.ID, 'multi-select'))
        output_message = self.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/p[2]')
        first_selected_button = self.driver.find_element(By.ID, 'printMe')
        all_selected_button = self.driver.find_element(By.ID, 'printAll')
        multiselect_list.deselect_all()
        california = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/select/option[1]')
        texas = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/select/option[6]')
        ohio = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/select/option[5]')
        ActionChains(self.driver).key_down(Keys.CONTROL).click(california).key_up(Keys.CONTROL).perform()
        ActionChains(self.driver).key_down(Keys.CONTROL).click(texas).key_up(Keys.CONTROL).perform()
        ActionChains(self.driver).key_down(Keys.CONTROL).click(ohio).key_up(Keys.CONTROL).perform()
        first_selected_button.click()
        self.assertEqual('First selected option is : California', output_message.text)
        all_selected_button.click()
        self.assertEqual('Options selected are : California,Texas,Ohio', output_message.text)

    def tearDown(self) -> None:
        self.driver.quit()
        print('good job')

