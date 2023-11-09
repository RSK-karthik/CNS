import numpy as np

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").lower()
    if len(plaintext) % 2 != 0:
        plaintext += 'x'
    
    ciphertext = []
    for i in range(0, len(plaintext), 2):
        # Convert pairs of letters to their numerical equivalents (A=0, B=1, ..., Z=25)
        pair = [ord(plaintext[i]) - ord('a'), ord(plaintext[i + 1]) - ord('a')]
        
        # Apply the Hill Cipher encryption
        result = np.dot(key_matrix, pair) % 26
        
        # Convert back to letters
        ciphertext.append(chr(int(result[0]) + ord('a')))
        ciphertext.append(chr(int(result[1]) + ord('a')))
    
    return "".join(ciphertext)

def decrypt(ciphertext, key_matrix):
    plaintext = []
    key_matrix = np.array(key_matrix)
    determinant = key_matrix[0, 0] * key_matrix[1, 1] - key_matrix[0, 1] * key_matrix[1, 0]
    determinant %= 26
    
    mod_inverse_det = mod_inverse(determinant, 26)

    if mod_inverse_det is None:
        raise ValueError("The key matrix is not invertible modulo 26.")
    
    key_matrix[0, 0], key_matrix[1, 1] = key_matrix[1, 1], key_matrix[0, 0]
    key_matrix[0, 1], key_matrix[1, 0] = -key_matrix[0, 1], -key_matrix[1, 0]
    
    key_matrix *= mod_inverse_det
    key_matrix = key_matrix % 26
    
    for i in range(0, len(ciphertext), 2):
        pair = [ord(ciphertext[i]) - ord('a'), ord(ciphertext[i + 1]) - ord('a')]
        
        # Apply the Hill Cipher decryption
        result = np.dot(key_matrix, pair) % 26
        
        # Convert back to letters
        plaintext.append(chr(int(result[0]) + ord('a')))
        plaintext.append(chr(int(result[1]) + ord('a')))
    
    return "".join(plaintext)

# Example usage
key_matrix = [[3, 2], [5, 7]]  # Replace with your 2x2 key matrix
plaintext = "hello"
ciphertext = encrypt(plaintext, key_matrix)
print("Encrypted:", ciphertext)

decrypted_text = decrypt(ciphertext, key_matrix)
print("Decrypted:", decrypted_text)