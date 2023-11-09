from pycipher import Caesar
plaintext = "Instrument"     
print("Plain text:",plaintext)
shift=3
cipher = Caesar(shift)
encrypted_text = cipher.encipher(plaintext)
print("Encrypted:", encrypted_text)

decrypted_text = cipher.decipher(encrypted_text)
print("Decrypted:",decrypted_text)
