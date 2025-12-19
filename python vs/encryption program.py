import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)

# print(f"chars: {chars}")
# print(f"keys: {keys}")

#encrypt

text=input("Enter a your message to encrypt: ")
encrypt=""

for letter in text:
    index = chars.index(letter)
    encrypt += keys[index]

print(f"Original message: {text}")
print(f"Encrypted message: {encrypt}")


#decrypt

encrypt=input("Enter a your message to encrypt: ")
text=""

for letter in encrypt:
    index = keys.index(letter)
    text += chars[index]

print(f"Encrypted message: {encrypt}")

print(f"Original message: {text}")
