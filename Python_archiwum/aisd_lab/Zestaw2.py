"""
pytanie 1:
Jaka jest roznica miedzy selection sort i insertion sort?

Selection sort zbudowany jest z podwójnej pętli, w pierwszej
zawsze szuka minimum listy, w drugiej porównuje wartości z
minimum i ustawia je na swoich miejscach, następnie powtarza,
aż do posortowania całej listy.
Insertion sort natomiast porównuje kolejne wartości listy, aby
umieścić element w odpowiednim miejscu, aż przesortuje całą listę.

Jeśli przyjrzymy się średniemu lub pesymistycznemu przypadkowi,
to insertion sort wykonuje n^2 zamian elementów, jak i n^2 porównań,
natomiast selection sort wykona n^2 porównań, ale tylko n zamian -
przenoszone będzie tylko aktualne minimum.

Ponadto selection sort nie jest stabilny, w przeciwieństwie do
insertion sort.


pytanie 2:
Co daje nam zastosowanie wartownika?

Dzięki wartownikowi można użyć prostszej pętli, w której nie ma
warunku jej zakończenia (np. dopóki i <= len(lista)), dzięki czemu
unikamy dodatkowych porównań w pętli.

W przypadku pythona, jeśli indeks poszukiwanej wartości będzie wynosić
len(lista)+1, oznacza to, że elementu nie było w liście i trafiliśmy
na wartownika.

Alternatywnie można po pętli dodać dodatkowy warunek, który porównuje
indeks z długością listy i następnie zwraca czy natrafiliśmy na poszukiwany
element, czy na wartownika (wówczas może zwracać np. None).
"""

import random

nowalista1 = []
for _ in range(0, 100):
    nowalista1.append(random.randint(-10000, 10000))


# zad. 1
def insertion_sort_asc(tab):
    """Sortowanie przez wstawianie,
    zlozonosc n^2 w przypadku srednim i pesymistycznym,
    O(n) w przypadku optymistycznym"""
    n = len(tab)

    for i in range(1, n):
        k = i - 1
        key = tab[i]
        while k >= 0 and key < tab[k]:
            tab[k+1] = tab[k]
            k -= 1
        tab[k+1] = key
    return tab


print('insertion asc:', insertion_sort_asc(nowalista1))


# zad. 3
def insertion_sort_desc(tab):
    n = len(tab)

    for i in range(1, n):
        k = i - 1
        key = tab[i]
        while k >= 0 and key > tab[k]:
            tab[k+1] = tab[k]
            k -= 1
        tab[k+1] = key
    return tab


print('insertion desc:', insertion_sort_desc(nowalista1))


# zad. 4
def insertion_sort(L, order='ascending'):
    if order == 'ascending':
        print('asc')
        return insertion_sort_asc(L)
    elif order == 'descending':
        print('desc')
        return insertion_sort_desc(L)
    else:
        print('Invalid input in order')


nowalista2 = []
for _ in range(0, 100):
    nowalista2.append(random.randint(-10000, 10000))

print(insertion_sort(nowalista2, 'descending'))


# zad. 5
def selection_sort_asc(L):
    """Sortowanie przez wybieranie,
    zlozonosc n^2 w kazdym z przypadkow
    """
    n = len(L)

    for i in range(n):
        minimum = i
        for j in range(i + 1, n):
            if L[minimum] > L[j]:
                minimum = j
        L[i], L[minimum] = L[minimum], L[i]
    return L


def selection_sort_desc(L):
    n = len(L)
    for i in range(n):
        maksimum = i
        for j in range(i + 1, n):
            if L[maksimum] < L[j]:
                maksimum = j
        L[i], L[maksimum] = L[maksimum], L[i]
    return L


# zad. 6
def sort(L, method='insertion', order='ascending'):
    if method == 'insertion':
        if order == 'ascending':
            print('insertion asc')
            return insertion_sort_asc(L)
        elif order == 'descending':
            print('insertion desc')
            return insertion_sort_desc(L)
        else:
            print('Invalid input in order')
    elif method == 'selection':
        if order == 'ascending':
            print('selection asc')
            return selection_sort_asc(L)
        elif order == 'descending':
            print('selection desc')
            return selection_sort_desc(L)
        else:
            print('Invalid input in order')
    else:
        print('Invalid input in method')


nowalista3 = [2, 3, -1, 5, 1, 0, 4, 6]
# print(sort(nowalista3, 'insertion', 'descending'))
print(sort(nowalista3, 'selection', 'descending'))


# zad. 7
def liniowe(lista, szukany_el):
    """Zwraca indeks, jesli szukany element
     znajduje sie w liscie
     """
    n = len(lista)
    for i in range(n):
        if lista[i] == szukany_el:
            return i  # zwraca indeks
    return None


def liniowe_while(lista, szukany_el):
    n = len(lista)
    i = 0
    while i < n:
        if lista[i] == szukany_el:
            return i
        i += 1
    return None


def liniowe_wartownik(lista, szukany_el):
    """Wartownik dodany na koniec listy
    zapewnia, że """
    n = len(lista)
    i = 0
    lista.append(szukany_el)

    while lista[i] != szukany_el:
        i += 1

    if i < n:
        return i
    else:
        return None

nowalista4 = [1, 2, 3, 4, 5, 6, 7]

print('liniowe for:', liniowe(nowalista4, 8))
print('liniowe while:', liniowe_while(nowalista4, 5))
print('liniowe wartownik:', liniowe_wartownik(nowalista4, 6))
