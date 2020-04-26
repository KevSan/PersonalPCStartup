from cryptography.fernet import Fernet
import json

key = Fernet.generate_key()

cipher_suite = Fernet(key)
user_name = cipher_suite.encrypt(b"")
td_pwd = cipher_suite.encrypt((b""))

print("This is the key: ", key)
print("This is how the password is hidden: ", user_name)
unciphered_username = (cipher_suite.decrypt(user_name))
unciphered_pwd = (cipher_suite.decrypt(td_pwd))
print("This is the password after unlocking it with the key: ", unciphered_username)
print("This is the password after unlocking it with the key: ", unciphered_pwd)

dict = {"td_username": user_name,
        "td_pwd": td_pwd}

with open('keys.secrets', 'wb') as file_object:
    file_object.write(bytes(str(dict), encoding='utf8'))

with open('keys.secrets', 'rb') as file_object:
    for line in file_object:
        dict = line

print(dict)

