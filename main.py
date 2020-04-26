from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

user_name = ""
password = ""
driver = webdriver.Chrome()
driver.get("https://onlinebanking.tdbank.com/#/authentication/login")

user_name_field = driver.find_element_by_id('formElement_0')
user_name_field.send_keys(user_name)

password_field = driver.find_element_by_id('formElement_1')
password_field.send_keys(password)

#TODO create this to be a class that gets reused by each site
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[2]/div[1]/div/div/form/button').send_keys("\n")

# opens a new tab
driver.execute_script("window.open('');")



from cryptography.fernet import Fernet
import os
import ast

def retrieve_username_and_password(env_var, secrets, source):
    key = get_key(env_var)
    cred_bytes = get_credentials(secrets)
    cred_dict_str = cred_bytes.decode("UTF-8")
    cred_dict = ast.literal_eval(cred_dict_str)
    user_name = decrypt_credentials(key, cred_dict[source + '_username'])
    password = decrypt_credentials(key, cred_dict[source + '_pwd'])
    return user_name, password

def get_key(env_var):
    path = os.getenv(env_var) + 'pc_startup.txt'
    with open(path, 'r') as f:
        for line in f:
            key = line
    return key

def get_credentials(secrets):
    with open(secrets, 'rb') as file_object:
        for line in file_object:
            credentials_dict = line
    return credentials_dict

def decrypt_credentials(key_str, ciphered_credential):
    key_byte = bytes(key_str, 'utf-8')
    cipher_suit = Fernet(key_byte)
    deciphered_credential = cipher_suit.decrypt(ciphered_credential)
    return deciphered_credential

username, password = retrieve_username_and_password('keys_path', 'keys.secrets', 'td')
