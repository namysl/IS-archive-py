def nwd(a, b):
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert a > 0 and b > 0

    while b != 0:
        c = a % b
        a = b
        b = c

    return a


print(nwd(24, 4))
print(nwd(71, 7))
