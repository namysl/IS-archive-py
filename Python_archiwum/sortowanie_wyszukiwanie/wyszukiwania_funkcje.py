def liniowe(lista, szukany_el):
    """Zwraca indeks, jesli szukany element znajduje sie w liscie"""
    for i in range(len(lista)):
        if lista[i] == szukany_el:
            return 'indeks: {}'.format(i)
    return False


def binarne_rekur(lista, szukany_el):
    """Musza byc posortowane"""
    srodek = len(lista) // 2
    lewa = lista[:srodek]
    prawa = lista[srodek + 1:]

    if len(lista) != 0:
        if szukany_el == lista[srodek]:
            return True

        elif szukany_el > lista[srodek]:
            return binarne_rekur(prawa, szukany_el)

        elif szukany_el < lista[srodek]:
            return binarne_rekur(lewa, szukany_el)
    else:
        return False  # nie znaleziono podanego elementu'


def binary_search_recursive(array, element, start, end):
    """Wskazuje indeks"""
    if start > end:
        return False

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid - 1)
    else:
        return binary_search_recursive(array, element, mid + 1, end)


def binarne_iter(lista, szukany_el):
    low = 0
    high = len(lista) - 1

    while low <= high:
        mid = (high + low) // 2

        if lista[mid] < szukany_el:
            low = mid + 1
        elif lista[mid] > szukany_el:
            high = mid - 1
        else:
            return mid
    return False


def liniowe_wartownik(lista, szukany_el):
    """Szukana wartosc umieszczana jest na koncu listy jako wartownik"""
    lista = lista[:]

    lista.append(szukany_el)
    indeks = 0

    while True:
        if lista[indeks] != szukany_el:
            indeks += 1
        else:
            if indeks != len(lista) - 1:
                return ('znaleziono poszukiwany element, indeks w liscie: {}'
                        .format(indeks))
            else:
                return False  # nie znaleziono poszukiwanego elementu'


LL = [3, 11, 15, 33, 45, 60, 90, 111, 133, 656, 890, 999, 1000]
print(binarne_iter(LL, 111))
print(binary_search_recursive(LL, 111, 0, len(LL) - 1))

aList = [1, 3, 5, 6, 8, 9, 10, 12, 34, 56, 78, 456]


def binary_search(arr, item, low=0, high=None):
    if high is None:
        high = len(arr)
    mid = low + (high - low) // 2

    if high - low + 1 <= 0 or mid == high:
        return False
    else:
        guess = arr[mid]
        if guess == item:
            return mid
        if item < guess:
            return binary_search(arr, item, low, mid)
        else:
            return binary_search(arr, item, (mid + 1), high)


print(binary_search(aList, 34))
