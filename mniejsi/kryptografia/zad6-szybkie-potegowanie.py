def szybkie_potegowanie(liczba, n):
    if n == 0:
        return 1

    if n % 2 == 1:
        return liczba * szybkie_potegowanie(liczba, n-1)
    else:
        a = szybkie_potegowanie(liczba, n/2)
    return a**2


print(szybkie_potegowanie(2, 8))
print(szybkie_potegowanie(3, 5))