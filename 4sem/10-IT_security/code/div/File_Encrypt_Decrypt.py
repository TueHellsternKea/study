# pip install cryptography
from cryptography.fernet import Fernet

def encrypt(filename, key):
    fernet = Fernet(key)
    
    with open(filename, 'rb') as file:
        original = file.read()
        
    encrypted = fernet.encrypt(original)
    
    with open(filename, 'wb') as enc_file:
        enc_file.write(encrypted)

def decrypt(filename, key):
    fernet = Fernet(key)
    
    with open(filename, 'rb') as enc_file:
        encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)
    
    with open(filename, 'wb') as dec_file:
        dec_file.write(decrypted)

# Generate Key
key = Fernet.generate_key()
filename = input("Enter Your filename: ")
encrypt(filename, key)
decrypt(filename, key)