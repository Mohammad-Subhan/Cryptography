from encrypt_CC import Encrypt
from decrypt_CC import Decrypt

text = input("Enter Text : ")

while True:
    digit = True
    key = input("Enter Key : ")

    for c in key:
        if not c.isdigit():
            digit = False
            break

    if not digit:
        print("Invalid Key. Enter only digits")
    else:
        break

key = int(key)

print("What do you want to do : ")
print("1. Encrypt\n2. Decrypt")
while True:
    choice = input("Enter: ")

    if choice == '1':
        encrypted = Encrypt(text, key)
        print(f"Encrypted Text: {encrypted}")
        break
    elif choice == '2':
        decrypted = Decrypt(text, key)
        print(f"Encrypted Text: {decrypted}")
        break
    else:
        print(f"Invalid Input")
