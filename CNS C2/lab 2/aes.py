# pip install pycryptodome 
from Crypto.Cipher import AES
key = b'C&F)H@McQfTjWnZr'
cipher = AES.new(key, AES.MODE_EAX)
data = "Welcome to copyassignment.com!".encode()
nonce = cipher.nonce
# encrypt the data
ciphertext = cipher.encrypt(data)
print("Cipher text:", ciphertext)
#decryption
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
# decrypt the data
decrypt= cipher.decrypt(ciphertext)
print("Plain text:", decrypt)
