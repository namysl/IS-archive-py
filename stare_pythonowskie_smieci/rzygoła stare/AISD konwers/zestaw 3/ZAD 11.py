def potega2(a, n):
    if n == 1:
        return a

    m = n // 2
    p = potega2(a, m)
    p = p * p

    if n % 2 == 1:
        p = p * a
    return p


print(potega2(2, 8))