from cryptography.fernet import Fernet
import base64
import os

def generate_Key():
    return Fernet.generate_key()

def encrypt_File(backup_path,key):
    with open(backup_path,'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    encrypted_path = backup_path + ".enc"
    with open(encrypted_path,'wb') as file:
        file.write(encrypted_data)
    
    #remove original unencrypted file#
    os.remove(backup_path)
    return encrypted_path