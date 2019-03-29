import random


def is_prime(n):
    if n < 1:
        return False

    for i in range(2, int(n / 2)):
        if n % i == 0:
            return False

    return True


def gcd(a, b):
    while (a != 0) and (b != 0):
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b


def multiplicative_inverse(a, b, x, y):
    if b == 1:
        x.append(0)
        y.append(1)
        return

    multiplicative_inverse(b, a % b, x, y)
    x.append(y[len(y) - 1])
    y.append(x[len(x) - 2] - (a // b)*y[len(y) - 1])
    d = y[len(y) - 1]
    return d


def generate_key_pair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)

    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    q = []
    w = []
    d = multiplicative_inverse(phi, e, q, w) % phi

    return (e, n), (d, n)


def encrypt_number(m, e, n):
    return (m**e) % n


def decrypt_number(h, d, n):
    return (h**d) % n


a1 = int(input("Введите первое число генерации ключа: "))
b1 = int(input("Введите второе число генерации ключа: "))

key = generate_key_pair(a1, b1)
print("Параметры RSA:", key)

m = int(input("Введите число для зашифравки: "))
h = encrypt_number(m, key[0][0], key[0][1])
print("Зашифрованное число:", h)
print("Расшифрованное число:", decrypt_number(h, key[1][0], key[1][1]))




