from cryptography.fernet import Fernet
import os
import ast


# TODO include proper commenting to code base
def retrieve_username_and_password(env_var, secrets, source):
    key = get_key(env_var, source)
    cred_bytes = get_credentials(secrets)
    cred_dict_str = cred_bytes.decode("UTF-8")
    cred_dict = ast.literal_eval(cred_dict_str)
    user_name = decrypt_credentials(key, cred_dict[source + '_username'])
    password = decrypt_credentials(key, cred_dict[source + '_pwd'])
    return user_name, password


def get_key(env_var, source):
    path = os.getenv(env_var) + source + '_key'
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
    return deciphered_credential.decode('utf-8')
