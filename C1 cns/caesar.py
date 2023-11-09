text = input("enter text : ")
key = int(input("enter the key : "))

et = ""

for i in text:
    if(i.isalnum()):
        if(i.islower()):
            temp = chr(((ord(i)-ord('a')+key)%26)+ord('a'))
            et+=temp
        if(i.isupper()):
            temp = chr(((ord(i)-ord('A')+key)%26)+ord('A'))
            et+=temp
        if(i.isnumeric()):
            temp = chr(((ord(i)-ord('0')+key)%10)+ord('0'))
            et+=temp 
    else:
        print("error text")
        break 
print("the encrypted text is ",et)

text = ""
for i in et:
    if(i.isalnum()):
        if(i.islower()):
            temp = chr(((ord(i)-ord('a')-key)%26)+ord('a'))
            text+=temp
        if(i.isupper()):
            temp = chr(((ord(i)-ord('A')-key)%26)+ord('A'))
            text+=temp
        if(i.isnumeric()):
            temp = chr(((ord(i)-ord('0')-key)%10)+ord('0'))
            text+=temp 
    else:
        print("error text")
        break 
print("the decrypted text is ",text)



