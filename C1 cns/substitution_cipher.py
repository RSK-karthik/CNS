import random
d={}
d_={}
def generate_cipher_key():
    global d,d_
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    x = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(alphabet)
    d = dict(zip(x,alphabet))
    d_ = dict(zip(alphabet,x))

generate_cipher_key()
def encrypt(pt,d):
    res= ""
    for item in pt:
        res = res + d[item]
    return res

def decrypt(ct,d_):
    res = ""
    for item in ct:
        res = res + d_[item]
    return res

pt = input("Enter plaintext: ")
ct = encrypt(pt.upper(),d)
print("Encryption: ",ct)
dt = decrypt(ct,d_)
print("Decryption: ",dt)
