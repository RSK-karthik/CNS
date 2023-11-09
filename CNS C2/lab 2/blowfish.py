from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes

# Generate a random encryption key (must be 16, 24, or 32 bytes long)
key = get_random_bytes(16)

# Create a Blowfish cipher
cipher = Blowfish.new(key, Blowfish.MODE_ECB)  # ECB mode is used for simplicity; use other modes for better security

# Text to be encrypted (must be a multiple of 8 bytes for ECB mode)
plaintext = b'Hello, Blowfish!'

# Encrypt the text
ciphertext = cipher.encrypt(plaintext)

# Decrypt the text
decrypted_text = cipher.decrypt(ciphertext)

# Print the results
print("Original text:", plaintext.decode())
print("Encrypted text:", ciphertext)
print("Decrypted text:", decrypted_text.decode())
