from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes

def rc4_encrypt(key, plaintext):
    cipher = ARC4.new(key)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return ciphertext

def rc4_decrypt(key, ciphertext):
    cipher = ARC4.new(key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('utf-8')

if __name__ == "__main__":
    key = get_random_bytes(16)  # You can change the key size as needed
    plaintext = "This is a secret message."
    
    #encrypt the message
    ciphertext = rc4_encrypt(key, plaintext)
    print("Ciphertext:", ciphertext.hex())

    #decrypt the message
    decrypted_text = rc4_decrypt(key, ciphertext)
    print("Decrypted Text:", decrypted_text)