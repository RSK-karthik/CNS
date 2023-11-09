from pycipher import Playfair

plaintext = "Instruments"
subkey=input("Enter key Capitals:")
key=subkey
charset = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
for i in charset:
    if i not in subkey:
        key+=(i)

        
print("Plain text:",plaintext)
cipher = Playfair(key)
encrypted_text = cipher.encipher(plaintext)
print("Encrypted:", encrypted_text)

decrypted_text = cipher.decipher(encrypted_text)
print("Decrypted:",decrypted_text)
