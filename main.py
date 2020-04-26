from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import cred_retrieval


driver = webdriver.Chrome()
driver.get("https://onlinebanking.tdbank.com/#/authentication/login")

user_name, password = cred_retrieval.retrieve_username_and_password('keys_path', 'keys.secrets', 'td')

user_name_field = driver.find_element_by_id('formElement_0')
user_name_field.send_keys(user_name)

password_field = driver.find_element_by_id('formElement_1')
password_field.send_keys(password)

# TODO create this to be a class that gets reused by each site
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[2]/div[1]/div/div/form/button').send_keys("\n")
# opens a new tab
driver.execute_script("window.open('https://www.capitalone.com/');")
