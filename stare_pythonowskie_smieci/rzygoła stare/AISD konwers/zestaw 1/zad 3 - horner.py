# zad. 3
def horner(lista, c):
    """Ilosc operacji:

    n operacji mnozenia, n operacji dodawania,
    gdzie n jest stopniem wielomianu"""

    wynik = lista[0]
    for i in range(1, len(lista)):
        wynik = c * wynik + lista[i]
    return wynik


lista1 = [2, 3, -7, -2]
print('wielomian:', horner(lista1, 1))
