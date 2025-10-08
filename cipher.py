def encrypt(plaintext,keyshift):
    cipher=""
    for i in range(len(keyshift)):
        x=(ord(plaintext[i])+ord(keyshift[i]))%26
        x+=ord('A')
        cipher+=chr(x)
    return cipher

def decrypt(ciphertext,key):
    plaintext=""
    keyshift=key+ciphertext[0:len(ciphertext)-len(key)]
    for i in range(len(ciphertext)):
        x=(ord(ciphertext[i])-ord(keyshift[i])+26)%26
        x+=ord('A')
        plaintext+=chr(x)
    return plaintext

# ask if user wants to encrypt or decrypt
num= int(input())
if num==1:
    plaintext= input()
    key=input()
    keyshift=key+plaintext[0:len(plaintext)-len(key)] #get key
    print(encrypt(plaintext,keyshift))
elif num==2:
    ciphertext=input()
    key=input()
    print(decrypt(ciphertext,key))
