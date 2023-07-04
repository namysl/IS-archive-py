def insertion_sort(lista):
    """Sortowanie przez wstawianie"""
    n = len(lista)

    for i in range(1, n):
        klucz = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > klucz:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = klucz
    return lista


def merge_sort_recur(lista):
    """Sortowanie przez scalanie - rekurencyjne"""

    if len(lista) > 1:
        m = len(lista) // 2
        left = lista[:m]
        right = lista[m:]

        merge_sort_recur(left)
        merge_sort_recur(right)

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
    return lista

print(merge_sort_recur([12, 13, 9, 5, 11, 8, 7, 4, 10]))

def bubble_sort(lista):
    """Sortowanie bąbelkowe"""
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def quicksort(lista):
    """Sortowanie szybkie"""

    smaller = []
    pivot_temp = []
    bigger = []

    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        for element in lista:
            if element < pivot:
                smaller.append(element)
            elif element > pivot:
                bigger.append(element)
            else:
                pivot_temp.append(element)

        left = quicksort(smaller)
        right = quicksort(bigger)

        wynik = left + pivot_temp + right
        return wynik


def counting_sort(lista):
    """Sortowanie przez zliczanie"""
    n = len(lista)
    gora = max(lista)

    temp = [0] * (gora + 1)

    for i in lista:
        temp[i] += 1

    for i in range(1, gora + 1):
        temp[i] += temp[i - 1]

    wynik = [0] * n
    i = n - 1

    while i >= 0:
        wynik[temp[lista[i]] - 1] = lista[i]
        temp[lista[i]] -= 1
        i -= 1

    return wynik


def insertion_sentinel(lista):
    """Sortowanie przez wstawianie z wartownikiem"""
    lista[0] = -1
    for i in range(2, len(lista)):
        klucz = lista[i]
        j = i - 1
        while lista[j] > klucz:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = klucz
    return lista


jakaslista = [9, 8, 7, 4, 5, 6, 3, 2, 1]
#print(insertion_sort(jakaslista))
print('*'*10)
#print(merge_sort(jakaslista))
print('*'*10)
#print(bubble_sort(jakaslista))
print('*'*10)
#print(quicksort(jakaslista))
print('*'*10)
#print(counting_sort(jakaslista))
print('*'*10)
#print(insertion_sentinel(jakaslista))
print('*'*10)


# MERGE SORT v2
def _mergeit(lista1, lista2):
    """Funkcja pomocnicza sortowania przez scalanie"""
    len_lista1 = len(lista1)
    len_lista2 = len(lista2)
    i1 = 0
    i2 = 0
    lista = []

    for i in range(len_lista1 + len_lista2):
        if i1 == len_lista1:
            lista.append(lista2[i2])
            i2 += 1
        elif i2 == len_lista2:
            lista.append(lista1[i1])
            i1 += 1
        elif lista1[i1] < lista2[i2]:
            lista.append(lista1[i1])
            i1 += 1
        else:
            lista.append(lista2[i2])
            i2 += 1

    return lista


def _merge_new_list(lista):
    """Funkcja pomocnicza sortowania przez scalanie"""
    len_lista = len(lista)

    if len_lista == 0 or len_lista == 1:
        return lista

    len_lista = len_lista // 2

    nowa_lista = _mergeit(_merge_new_list(lista[:len_lista]),
                          _merge_new_list(lista[len_lista:]))

    return nowa_lista


def mergesort(lista):
    """Sortowanie przez scalanie - v2"""
    return _merge_new_list(lista)


print(mergesort(jakaslista))

newlist = [2312, 8, 4141, 222, 411, 12, 1, 12]

print(mergesort(newlist))
