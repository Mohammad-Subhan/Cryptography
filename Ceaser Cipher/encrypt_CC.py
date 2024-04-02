def Encrypt(text, key):
    encrypted = ""

    for i in text:
        if i == ' ':
            encrypted += i
        elif i.isdigit():
            encrypted += chr((ord(i) + key - 48) % 9 + 48)
        elif i.isupper():
            encrypted += chr((ord(i) + key - 65) % 26 + 65)
        elif i.islower():
            encrypted += chr((ord(i) + key - 97) % 26 + 97)
        else:
            encrypted += i

    return encrypted
