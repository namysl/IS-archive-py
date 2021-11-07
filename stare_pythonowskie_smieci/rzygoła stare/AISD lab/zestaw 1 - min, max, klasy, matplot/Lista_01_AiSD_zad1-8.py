lista1 = [1, 2, 1, 2, 1, 3, 5, 0, 0, 0, 0, 1]
lista2 = [23, 12, 53, 1, 23, 1, 8, 1, 53]


# zad. 1
def szukaj_minimum_for(A):
    minimum = A[0]
    for i in range(len(A)):
        if A[i] < minimum:
            minimum = A[i]
    return minimum


print('szukaj_minimum_for:', szukaj_minimum_for(lista2))


# zad. 2
def szukaj_minimum_while(A):
    minimum = A[0]
    i = 0
    while i < len(A):
        if A[i] < minimum:
            minimum = A[i]
        i += 1
    return minimum


print('szukaj_minimum_while:', szukaj_minimum_while(lista2))


# zad. 3
def najmniejszy_indeks_el_min(A):
    minimum = A[0]
    indeks = 0
    for i in range(len(A)):
        if A[i] < minimum:
            minimum = A[i]
            indeks = i
    return indeks


print('najmniejszy_indeks_el_min:', najmniejszy_indeks_el_min(lista2))


# zad. 4
def najwiekszy_indeks_el_min(A):
    minimum = A[0]
    indeks = 0
    for i in range(len(A)):
        if A[i] <= minimum:
            minimum = A[i]
            indeks = i
    return indeks


print('najwiekszy_indeks_el_min:', najwiekszy_indeks_el_min(lista2))


# zad. 5 - maksimum
def szukaj_maksimum_for(A):
    maksimum = A[0]
    for i in range(len(A)):
        if A[i] > maksimum:
            maksimum = A[i]
    return maksimum


print('szukaj_maksimum_for:', szukaj_maksimum_for(lista2))


def szukaj_maksimum_while(A):
    maksimum = A[0]
    i = 0
    while i < len(A):
        if A[i] > maksimum:
            maksimum = A[i]
        i += 1
    return maksimum


print('szukaj_maksimum_while:', szukaj_maksimum_while(lista2))


def najmniejszy_indeks_el_maks(A):
    maksimum = A[0]
    indeks = 0
    for i in range(len(A)):
        if A[i] > maksimum:
            maksimum = A[i]
            indeks = i
    return indeks


print('najmniejszy_indeks_el_maks:', najmniejszy_indeks_el_maks(lista2))


def najwiekszy_indeks_el_maks(A):
    minimum = A[0]
    indeks = 0
    for i in range(len(A)):
        if A[i] >= minimum:
            minimum = A[i]
            indeks = i
    return indeks


print('najwiekszy_indeks_el_maks:', najwiekszy_indeks_el_maks(lista2))


# zad. 6 - minimum i maksimum
def min_maks(A):
    minimum = A[0]
    maksimum = A[0]
    for i in range(len(A)):
        if A[i] < minimum:
            minimum = A[i]
        elif A[i] > maksimum:
            maksimum = A[i]
    return minimum, maksimum


print('min_max:', min_maks(lista2))


# zad. 7
def suma(lista):
    n = len(lista)
    wynik = 0
    for i in range(n):
        wynik += lista[i]
    return wynik


def duze_pi(lista):
    n = len(lista)
    wynik = 1
    for i in range(n):
        wynik *= lista[i]
    return wynik


def srednia(lista):
    n = len(lista)
    wynik = 0
    for i in range(n):
        wynik += lista[i]
    wynik = wynik / n
    return wynik


def srednia_dodatnich(lista):
    n = len(lista)
    copy_n = n
    wynik = 0
    for i in range(n):
        if lista[i] > 0:
            wynik += lista[i]
        else:
            copy_n -= 1
    wynik = wynik / copy_n
    return wynik


lista3 = [x for x in range(1, 11)]
print('suma:', suma(lista3))
print('duze_pi:', duze_pi(lista3))
print('srednia:', srednia(lista3))

lista4 = [1, 3, -1, -8, 2]
print('srednia_dodatnich:', srednia_dodatnich(lista4))  # 6/3


def wielomian(lista, c):
    """f(x) = ax^4 + ax^3 + ax^2 + ax + a"""
    wynik = lista[0]
    for i in range(0, len(lista) - 1):
        wynik = c * wynik + lista[i+1]
    return wynik


lista4 = [2, 3, -7, -2]
print('wielomian:', wielomian(lista4, 1))


# zad. 8
def wyszukiwanie_binarne(A, element):
    """Zwraca indeks pod ktorym znajduje sie poszukiwany element
    lub None, jesli nie ma go w liscie
    """
    n = len(A)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if element == A[mid]:
            return mid
        elif element < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return None


lista5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('wyszukiwanie_binarne, indeks dla 10:', wyszukiwanie_binarne(lista3, 10))
