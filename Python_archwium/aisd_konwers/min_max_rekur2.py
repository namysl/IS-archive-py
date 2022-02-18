"""Zaproponuj i zapisz (w pseudokodzie) rekurencyjny algorytm oparty na
metodzie „dziel i zwyciężaj”, realizujący problem wyznaczenia elementu minimalnego w
danej tablicy n-elementowej. Napisz program w języku Python realizujacy Twój algorytm.
Znajdź rekurencję opisującą złożoność tego algorytmu."""


A = [3, 5, 7, 9, 1, 3, 10, 11, 0]


def minimum_rekur(lista, left, right):
    """T(n) = O(1) + 2T(n/2) -> T(n) = O(n)"""
    if left == right:  # jednoelementowa lista; porownanie O(1)
        return lista[left]

    middle = (left + right) // 2  # wyznaczanie srodka O(1)
    left_side = minimum_rekur(lista, left, middle)  # T(n/2) <- pracuje na polowie listy
    right_side = minimum_rekur(lista, middle+1, right)

    if left_side < right_side:  # O(1)
        return left_side
    else:
        return right_side


print(minimum_rekur(A, 0, len(A)-1))


def maximum(numbers):
    """Find the maximum value in the list 'numbers'."""
    if len(numbers) == 1:
        return numbers[0]
    mid = len(numbers) / 2
    leftmax = maximum(numbers[0:mid])
    rightmax = maximum(numbers[mid:len(numbers)])
    if leftmax > rightmax:
        return leftmax
    else:
        return rightmax
