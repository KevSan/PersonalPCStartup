from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import cred_retrieval

user_name, password = cred_retrieval.retrieve_username_and_password('keys_path', 'keys.secrets', 'google')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com/")

time.sleep(5)

driver.find_element_by_id("gb_70").click()

time.sleep(5)

user_name_field = driver.find_element_by_xpath('//*[@id="identifierId"]')
user_name_field.send_keys(user_name)

time.sleep(2)

driver.find_element_by_id('identifierNext').click()

password_field = driver.find_element_by_id('')
password_field.send_keys(password)

# TODO create this to be a class that gets reused by each site
time.sleep(5)
driver.find_element_by_id('noAcctSubmit').send_keys("\n")
# opens a new tab
#driver.execute_script("window.open('https://www.capitalone.com/');")
