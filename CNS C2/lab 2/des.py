#pip install pyDes
from pyDes import des, PAD_PKCS5
import binascii

# Key for encryption and decryption (8 bytes)
key = b'12345678'

# Data to be encrypted
data = b'This is a secret'

# Create a DES object with the specified key and mode
cipher = des(key, PAD_PKCS5, IV=b'\0\0\0\0\0\0\0\0')

# Encrypt the data
encrypted_data = cipher.encrypt(data)

# Decrypt the data
decrypted_data = cipher.decrypt(encrypted_data)

# Print the results
print("Original data:", data)
print("Encrypted data (hex):", binascii.hexlify(encrypted_data))
print("Decrypted data:", decrypted_data.decode('utf-8'))
