"""Zaproponuj i zapisz (w pseudokodzie) rekurencyjny algorytm oparty na
metodzie „dziel i zwyciężaj”, realizujący problem jednoczesnego wyznaczenia elementu
minimalnego i maksymalnego w danej tablicy n-elementowej.

Znajdz rekurencję opisujacą złożoność tego algorytmu.
Oszacuj złozoność swojego rozwiązania (dla naturalnych potęg 2 dokładnie).

Napisz program w języku Python realizujący Twój algorytm."""


def min_maks_rekur(lista, left, right):
    """Dla
    len(lista) == 1 -> T(n) = 0
    len(lista) == 2 -> T(n) = 1
    len(lista) > 2  -> T(n/2) + T(n/2) + 2
                       T(n) = 2T(n/2) + 2
    """
    if left + 1 >= right:  # porownanie O(1)
        if lista[left] < lista[right]:
            return lista[left], lista[right]
        else:
            return lista[right], lista[left]

    mid = (left + right) // 2

    (left_min, left_maks) = min_maks_rekur(lista, left, mid)  # (n/2)
    (right_min, right_maks) = min_maks_rekur(lista, mid + 1, right)  # (n/2)

    maks_element = left_maks
    min_element = left_min

    if right_maks > maks_element:  # porownanie O(1)
        maks_element = right_maks
    if right_min < min_element:
        min_element = right_min

    return min_element, maks_element


A = [3, 8, 9, 11, 0, 5, 2, 5, 17, 1, 4]
print(min_maks_rekur(A, 0, len(A) - 1))
