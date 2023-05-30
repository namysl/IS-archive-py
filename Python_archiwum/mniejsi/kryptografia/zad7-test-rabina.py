import random


def szybkie_potegowanie(liczba, n):
    if n == 0:
        return 1

    if n % 2 == 1:
        return liczba * szybkie_potegowanie(liczba, n-1)
    else:
        a = szybkie_potegowanie(liczba, n/2)
    return a**2


def test_rabina(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # n-1 jako (2^s) * d, d jest nieparzyste
    s = 0
    d = n - 1
    while d % 2 == 0:
        d = d // 2
        s += 1

    # k iteracji testowania, domyslnie k=5
    for i in range(k):
        a = random.randint(2, n-2)
        x = szybkie_potegowanie(a, d) % n

        if x == 1 or x == n-1:
            continue

        for j in range(s-1):
            x = szybkie_potegowanie(x, 2) % n
            if x == n-1:
                break
        else:
            return False
    return True


lista = [10, 11, 12, 13, 14, 15, 16, 17]

for przyklad in lista:
    if test_rabina(przyklad):
        print(przyklad, "jest prawdopodobnie liczbą pierwszą")
    else:
        print(przyklad, "nie jest liczbą pierwszą")
