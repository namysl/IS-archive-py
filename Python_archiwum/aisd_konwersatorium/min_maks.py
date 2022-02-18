# zad. 2
def min_maks_v1(A):
    """Szukanie rownoczesnie minimum i maksimum

    Ilosc operacji:
    minimum: n-1 porownan
    maksimum: n-1 porownan
    w sumie: 2n-2 porownan
    """
    minimum = A[0]
    maksimum = A[0]
    for i in range(len(A)):
        if A[i] < minimum:  # n-1 porownan
            minimum = A[i]
        elif A[i] > maksimum:  # n-1 porownan
            maksimum = A[i]
    return minimum, maksimum


def min_max_v2(A):
    """Wyszukiwanie minimum i maksimum, tworzac pary oraz
    szukajac minimum w miejscach nieparzystych,
    a maksimum w parzystych

    Ilosc operacji:
    dla list parzystych: 1/n + (1/n - 1) * 2 = 3/2n - 2

    dla list nieparzystych: dochodza dwa porownania
    z min i maks, czyli 3/2n - 2 + 2 = 3/2n
    """
    n = len(A)
    for i in range(0, n-1, 2):
        a = A[i]
        b = A[i + 1]
        if a > b:  # 1/n porownan
            A[i] = b
            A[i + 1] = a

    minimum = A[0]
    maksimum = A[1]
    for i in range(0, n-1, 2):
        if minimum > A[i]:  # 1/n-1 porownan
            minimum = A[i]
        elif maksimum < A[i+1]:  # 1/n-1 porownan
            maksimum = A[i+1]

    if n % 2 != 0:
        if minimum > A[-1]:  # 1 porownanie
            minimum = A[-1]
        elif maksimum < A[-1]:  # 1 porownanie
            maksimum = A[-1]

    return minimum, maksimum


l3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(min_max_v2(l3))
