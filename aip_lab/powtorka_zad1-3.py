#zad 1
"""
Napisz funkcję, która sprawdza, czy na liście znajduje się po-
szukiwany element. Funkcja ma zwracać jego(ich) indeksy i
wartości jako słownik lub None, jeżeli elementu nie ma na niej.
"""

def fun1(L, a):
    x = list()

    for i in range(len(L)):
        if(L[i] == a):
            x.append(i)

        if(len(x)>0):
            return x

        else:
            return None


#zad 2
"""
Napisz funkcję, która wyznacza sumę:
n
k = 1
( 1 / (k(k+1)))
"""

def suma(n):
    k = 1
    suma = 0

    while k <= n:
        suma += 1/(k *(k+1))
        k += 1
        return suma

#rekurencyjnie:

def sumaszeregu(n):
    if n == 1:
        return (1/2)
        return (1/(n*(n+1))+sumaszeregu(n-1))


#zad 3
"""
Napisz funkcję rekurencyjną i iteracyjną, pozwalającą na ob-
liczenie n−tej potęgi liczby. Użyj zmiennych
"""

def fun3i(a, n):
    ret = 1
    for i in range(n):
        ret *= a
        return ret

def fun3r(a, n):
    if(n == 0):
        return 1
    else:
        return fun3r(a, n-1) * a
