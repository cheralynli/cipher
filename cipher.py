def encrypt(plaintext,keyshift):
    cipher=""
    for i in range(len(keyshift)):
        # get ASCII value, add keyshift ASCII value, mod 26 to cycle back to A-Z
        x=(ord(plaintext[i])+ord(keyshift[i]))%26
        x+=ord('A')
        # append character to cipher
        cipher+=chr(x)
    return cipher

def decrypt(ciphertext,key):
    plaintext=""
    keyshifter=key
    for i in range(len(ciphertext)):
        if i<len(key):
            #get ASCII value of ciphertext and key at i for first len(key) characters
            x=(ord(ciphertext[i])-ord(key[i])+26)%26
            x+=ord('A') 
            plaintext+=chr(x)
            keyshifter=key+chr(x)
        else:
            #get ASCII value of ciphertext and previous plaintext character for rest
            y=(ord(ciphertext[i])-ord(plaintext[i-len(key)])+26)%26
            y+=ord('A')
            plaintext+=chr(y)
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
