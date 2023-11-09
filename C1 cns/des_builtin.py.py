from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad

def en(pt,key):
    cipher=DES.new(key,DES.MODE_ECB)
    padded_text=pad(pt,DES.block_size)
    encrypted=cipher.encrypt(padded_text)
    return encrypted

def de(ci,key):
    decipher=DES.new(key,DES.MODE_ECB)
    unpadded=decipher.decrypt(ci)
    decrypted=unpad(unpadded,DES.block_size)
    return decrypted

key=get_random_bytes(8)
pt=b"Ee Sala Cup Namde"
ci=en(pt,key)
print(ci)
print(de(ci,key).decode('utf-8'))

**DES**