from encrypt_PF import Encrypt
from decrypt_PF import Decrypt
from keymatrix import KeyMatrix
from pairs import Pairs

text = input("Enter Text : ")

key = input("Enter Key : ")

print("What do you want to do : ")
print("1. Encrypt\n2. Decrypt")

key_matrix = KeyMatrix(key)
pairs = Pairs(text)

while True:
    choice = input("Enter: ")

    if choice == '1':
        encrypted = Encrypt(text, pairs, key_matrix)
        print(f"Encrypted Text: {encrypted}")
        break
    elif choice == '2':
        decrypted = Decrypt(text, pairs, key_matrix)
        print(f"Encrypted Text: {decrypted}")
        break
    else:
        print(f"Invalid Input")
