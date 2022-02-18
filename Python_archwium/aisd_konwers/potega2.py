def potega1(a, n):
    if n == 1:
        return a
    m = n // 2
    return potega1(a, m) * potega1(a, n-m)

print(potega1(2, 8))