from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = 'http://demo.seleniumeasy.com/basic-first-form-demo.html'

driver = webdriver.Chrome()
driver.get(url)
sleep(3)
try:
    close_popup_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[2]/a')
    close_popup_button.click()
except NoSuchElementException:
    pass

# task 1

user_input = 'message'
msg_box_input = driver.find_element(By.ID, 'user-message')
msg_box_input.clear()
msg_box_input.send_keys(user_input)
button = driver.find_element(By.XPATH, '//*[@id="get-input"]/button')
button.click()
msg_box_output = driver.find_element(By.ID, 'display')
assert msg_box_output.text == user_input, 'task 1 failed - output different than input'


# task 2 - numbers
value_a_box = driver.find_element(By.ID, 'sum1')
value_b_box = driver.find_element(By.ID, 'sum2')
get_total_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')
total_a_b = driver.find_element(By.ID, 'displayvalue')
value_a_box.clear()
value_b_box.clear()
numbers_input_a = 5
numbers_input_b = 7

value_a_box.send_keys(str(numbers_input_a))
value_b_box.send_keys(str(numbers_input_b))
get_total_button.click()
assert total_a_b.text == str(numbers_input_a + numbers_input_b), 'task 2 - numbers failed'



# task 2 - words

value_a_box.clear()
value_b_box.clear()
words_input_a = 'asdfsa'
words_input_b = 'fsdfs'

value_a_box.send_keys(words_input_a)
value_b_box.send_keys(words_input_b)
get_total_button.click()
assert total_a_b.text == 'NaN', 'task 2 - words failed'


driver.close()
print('good job')




