def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def check_key_validity(a, b, m):
    if gcd(a, m) != 1:
        return False
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(m, int):
        return False
    return True


def encrypt(plaintext, a, b, m):
    if not check_key_validity(a, b, m):
        raise ValueError("Nieprawidłowy klucz.")

    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                x = ord(char) - ord('A')
                encrypted = (a * x + b) % m
                ciphertext += chr(encrypted + ord('A'))
            else:
                x = ord(char) - ord('a')
                encrypted = (a * x + b) % m
                ciphertext += chr(encrypted + ord('a'))
        else:
            ciphertext += char

    return ciphertext


def decrypt(ciphertext, a, b, m):
    if not check_key_validity(a, b, m):
        raise ValueError("Nieprawidłowy klucz.")

    inverse = 0
    for i in range(1, m):
        if (a * i) % m == 1:
            inverse = i
            break

    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                y = ord(char) - ord('A')
                decrypted = (inverse * (y - b)) % m
                plaintext += chr(decrypted + ord('A'))
            else:
                y = ord(char) - ord('a')
                decrypted = (inverse * (y - b)) % m
                plaintext += chr(decrypted + ord('a'))
        else:
            plaintext += char

    return plaintext


klucz_a = 5
klucz_b = 8
modulo = 26

wiadomosc = "jakas wiadomosc"
zaszyfrowane = encrypt(wiadomosc, klucz_a, klucz_b, modulo)
odszyfrowane = decrypt(zaszyfrowane, klucz_a, klucz_b, modulo)

print("Wiadomość oryginalna:", wiadomosc)
print("Wiadomość zaszyfrowana:", zaszyfrowane)
print("Wiadomość odszyfrowana:", odszyfrowane)
