# zad. 1
def odwroc(A):
    """Metoda odwrocenia listy z zajec"""
    if len(A) <= 1:
        return A
    else:
        return odwroc(A[1:]) + [A[0]]


def odwroc2(lista, el=0):
    """Inna metoda niz przedstawiona na zajeciach"""
    if len(lista) < 2:
        return lista
    else:
        if el != len(lista):
            lista.insert(el, lista[-1])
            del lista[-1]
            odwroc2(lista, el+1)
        return lista


lista1 = [1, 22, 333, 4444, 55555, 666666]
#print(odwroc(lista1))
print(odwroc2(lista1))


# zad 2
def nwd(a, b):
    q = a // b
    reszta = a - b * q

    if reszta == 0:
        return b
    else:
        return nwd(b, reszta)


print('NWD:', nwd(282, 78))


# zad. 3
def piramida(liczba):
    if liczba > 0:
        print('*' * liczba)
        piramida(liczba - 1)


piramida(5)


# zad. 4
def na_binarny(liczba):
    assert isinstance(liczba, int)

    if liczba > 0:
        return (liczba % 2 + 10 * na_binarny(liczba // 2))
    else:
        return 0


print('na binarny:', na_binarny(8))


# zad. 5
def f_ackermanna(m, n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return f_ackermanna(m-1, 1)
    elif m > 0 and n > 0:
        return f_ackermanna(m-1, f_ackermanna(m, n-1))


print('funkcja Ackermanna:', f_ackermanna(3, 2))


# zad. 6
def sigma1(n):
    if n == 1:
        return n
    return 1/n + sigma1(n - 1)


print('1/i:', sigma1(10))


def sigma2(n):
    if n == 1:
        return n
    return 1 / (n ** 2) + sigma2(n - 1)


print('1/i^2:', sigma2(10))


def sigma3(n):
    if n == 1:
        return n
    return n + sigma3(n - 1)


print('i:', sigma3(10))


def sigma4(n):
    if n == 1:
        return 2 ** n
    return 2 ** n + sigma4(n - 1)


print('2^i:', sigma4(10))


# zad. 7
def merge_sort(lista):
    """Sortowanie przez scalanie - rekurencyjne"""

    if len(lista) > 1:
        n = len(lista) // 2
        left = lista[:n]
        right = lista[n:]
        print('left', left)
        print('right', right)
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1
    print(lista)
    return lista


lista5 = [7, 2, 1, 4, 9, 10]

#print(merge_sort(lista5))
