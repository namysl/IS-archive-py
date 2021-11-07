# a)
def potega_iter(a, n):
    """
    a: potegowana liczba
    n: potega"""

    wynik = 1
    for _ in range(n):
        wynik *= a
    return wynik


print(potega_iter(2, 8))

# b)
def potega_rekur(a, n):

    if n == 0:
        return 1
    else:
        return a * potega_rekur(a, n-1)


print(potega_rekur(2, 8))