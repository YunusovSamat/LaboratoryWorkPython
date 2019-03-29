import math


def encrypt_vigenere(plain, k):
    s = ""
    k = k.upper()
    for i in range(len(plain)):
        num_k = ord(k[i]) - 65
        num_plain = ord(plain[i])

        if plain[i].isupper():
            if num_k + num_plain > 90:
                s += chr(num_k + num_plain - 26)
            else:
                s += chr(num_k + num_plain)
        else:
            if num_k + num_plain > 122:
                s += chr(num_k + num_plain - 26)
            else:
                s += chr(num_k + num_plain)
    return s


def decrypt_vigenere(cipher, k):
    s = ""
    k = k.upper()
    for i in range(len(cipher)):
        num_k = ord(k[i]) - 65
        num_cipher = ord(cipher[i])

        if cipher[i].isupper():
            if num_cipher - num_k < 65:
                s += chr(num_cipher - num_k + 26)
            else:
                s += chr(num_cipher - num_k)
        else:
            if num_cipher - num_k < 97:
                s += chr(num_cipher - num_k + 26)
            else:
                s += chr(num_cipher - num_k)

    return s


plaintext = input("Введите текст: ")

while True:
    key = input("Введите ключ: ")
    if key.isalpha():
        break

if len(plaintext) > len(key):
    div = len(plaintext) / len(key)
    key *= math.ceil(div)
    key = key[:len(plaintext)]
elif len(plaintext) < len(key):
    key = key[:len(plaintext)]

print("\nПростой текст:", plaintext)
print("Ключ:", key)
ev = encrypt_vigenere(plaintext, key)
print("Зашифрованный текст:", ev)
print("Расшифрованный текст:", decrypt_vigenere(ev, key))

