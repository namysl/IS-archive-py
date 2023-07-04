def sumuj(lista, s):
    """Sumuje kolejne elementy listy.
    Jesli ich suma jest wieksza od s zwraca sume."""
    suma = 0

    for num in lista:
        if suma + num <= s:
            suma += num
        else:
            return suma


def ogranicz_liste(lista, s):
    """Ogranicza liste, jesli w sumuj suma wyszla
    wieksza od s."""
    j = 0

    for num in lista:
        if sumuj(lista[j:], s) != s:
            j += 1
        else:
            return lista[j:]


def znajdz_podliste(lista, s):
    """Generuje podliste elementow dajacych sume s."""
    elem = []
    suma = 0

    if ogranicz_liste(lista, s) is None:
        print('po sortowaniu')
        return znajdz_podliste(sortuj(lista), s)

    for num in ogranicz_liste(lista, s):
        if suma + num <= s:
            suma += num
            elem.append(num)
    return elem


def sortuj(lista):
    """Sortuje podana liste metoda zliczania."""
    n = len(lista)
    gora = max(lista)

    temp = [0] * (gora + 1)
    for el in lista:
        temp[el] += 1
    for el in range(1, gora + 1):
        temp[el] += temp[el - 1]

    wynik = [0] * n
    i = n - 1

    while i >= 0:
        wynik[temp[lista[i]] - 1] = lista[i]
        temp[lista[i]] -= 1
        i -= 1
    return wynik


def zbadaj(lista, s):
    """Steruje wynikiem koncowym programu.
    Jesli elementy daja s, zwraca ich w podliscie,
    w przeciwnym przypadku zwraca None."""
    if len(znajdz_podliste(lista, s)) != 0:
        return znajdz_podliste(lista, s)
    else:
        return None


lista1 = [1, 4, 20, 3, 10, 5]
s1 = 33

lista2 = [1, 4, 0, 0, 3, 10, 5]
s2 = 7

lista3 = [1, 4, 0, 2, 9]
s3 = 3

print('sumuj', sumuj(lista3, s2))
print('ogranicz_liste', ogranicz_liste(lista3, s3))
print('znajdz_podliste', znajdz_podliste(lista3, s3))
print('sortuj', sortuj(lista3))
print('zbadaj', zbadaj(lista3, s3))
print('~'*10)
print(zbadaj(lista1, s1))
print('*'*10)
print(zbadaj(lista2, s2))
print('*'*10)
print(zbadaj(lista3, s3))
