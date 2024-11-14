from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

import base64
import os




def load_key(file_path = './Keylogger/key.key'):
    file_path = './Keylogger/key.key'
    with open(file_path, 'rb') as key_file:
        encoded_key = key_file.read()
    key = base64.b64decode(encoded_key)
    return key

def encrypt_aes_gcm(text, key):
    data = text.encode()
    nonce = os.urandom(12)
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    tag = encryptor.tag
    result_str = nonce + ciphertext + tag 
    return result_str

def decrypt_aes_gcm(encrypted_data, key):
    nonce = encrypted_data[:12]
    ciphertext = encrypted_data[12:-16]
    tag = encrypted_data[-16:]
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    data = decryptor.update(ciphertext) + decryptor.finalize()
    return data.decode()