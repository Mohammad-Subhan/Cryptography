def Decrypt(text, key):
    decrypted = ""

    for i in text:
        if i == ' ':
            decrypted += i
        elif i.isdigit():
            decrypted += chr((ord(i) - key - 48 + 9) % 9 + 48)
        elif i.isupper():
            decrypted += chr((ord(i) - key - 65 + 26) % 26 + 65)
        elif i.islower():
            decrypted += chr((ord(i) - key - 97 + 26) % 26 + 97)
        else:
            decrypted += i

    return decrypted
