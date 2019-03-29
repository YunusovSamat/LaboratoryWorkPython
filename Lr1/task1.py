plaintext = input("Введите строку: ")


def encrypt_caesar(plain):
    s = ""
    for i in plain:
        num = ord(i)
        if ((num >= 60) and (num <= 87)) or ((num >= 97) and (num <= 119)):
            s += chr(num + 3)
        elif ((num > 87) and (num <= 90)) or ((num > 119) and (num <= 121)):
            s += chr(num - 23)
        else:
            s += chr(num)
    return s


def decrypt_caesar(cipher):
    s = ""
    for i in cipher:
        num = ord(i)
        if ((num >= 68) and (num <= 90)) or ((num >= 100) and (num <= 121)):
            s += chr(num - 3)
        elif ((num >= 65) and (num < 68)) or ((num >= 97) and (num < 100)):
            s += chr(num + 23)
        else:
            s += chr(num)
    return s


ec = encrypt_caesar(plaintext)

print("Шифровка:", plaintext, "=>", ec)
print("Расшифровка:", encrypt_caesar(plaintext), "=>", decrypt_caesar(ec))
