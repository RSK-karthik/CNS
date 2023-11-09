def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char >= 'a' and char <= 'z':
            encrypted_message += key[ord(char) - ord('a')]
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, key):
    decrypted_message = ""
    for char in message:
        if char in key:
            decrypted_message += chr(ord('a') + key.index(char))
        else:
            decrypted_message += char
    return decrypted_message

key = input("Enter the substitution key (26 lowercase letters in random order): ")

if len(key) != 26 or not key.islower():
    print("Invalid key format. Please provide 26 lowercase letters.")
    exit(0)

message = input("Enter the message to encrypt: ")

encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
