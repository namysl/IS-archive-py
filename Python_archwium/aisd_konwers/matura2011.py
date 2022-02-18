# zad.1
def sklej(n):  # rekurencyjnie
    if n == 1:
        return 0
    elif n % 2 == 0:
        return n - 1 + 2 * sklej(n//2)
    else:
        return n - 1 + sklej((n-1)//2) + sklej((n+1)//2)

#print(sklej(7))

def sklej_iteracyjnie(n):
    assert n > 0

    s = [0 for _ in range(n+1)]
    i = 2
    while i <= n:
        if i == 0:
            s[i] = 0
        if i % 2 == 0:
            s[i] = i - 1 + 2 * s[i//2]
        else:
            s[i] = i - 1 + s[(i-1)//2] + s[(i+1)//2]
        i += 1
    print(s)
    return s[-1]


print(sklej_iteracyjnie(6))



def sklej_iteracyjnie2(n):
    assert n > 0
    s = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        if i % 2 == 0:
            s[i] = i - 1 + 2 * s[i//2]
        else:
            s[i] = i - 1 + s[(i-1)//2] + s[(i+1)//2]
    # print(s)
    return s[-1]

#print(sklej_iteracyjnie(6))


# zad.2
def potega(n, a):
    p = 1
    b = a
    while n > 0:
        # print('p', p, 'b', b, 'n', n)
        if n % 2 != 0:
            p = p * b
        b = b * b
        n = n // 2
    return p, b, n


#print(potega(2, 2))