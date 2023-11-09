import os
import pyaes

# Generate a random 128-bit (16-byte) AES key
key = os.urandom(16)

# Create an AES cipher object
aes = pyaes.AESModeOfOperationCTR(key)

# Plaintext to encrypt
plaintext = "hello world"

# Encrypt the plaintext
cipherText = aes.encrypt(plaintext.encode('utf-8'))  # Encode plaintext as bytes

# Decrypt the ciphertext
decrypted = aes.decrypt(cipherText).decode('utf-8')  # Decode the decrypted bytes to string

print("Original plaintext:", plaintext)
print("Encrypted ciphertext:", repr(cipherText))
print("Decrypted plaintext:", decrypted)