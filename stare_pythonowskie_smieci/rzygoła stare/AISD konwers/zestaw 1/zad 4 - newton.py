# zad. 4
def HornerNewton(B, X, c):
    """
    B - lista zawierajaca wspolczynniki bk
    X - lista zawierajaca liczby x
    c - dana liczba
    """
    pierwszy_wynik = B[0] * 1
    c_minus_x = 1
    suma = pierwszy_wynik

    for i in range(0, len(B)-1):
        c_minus_x *= (c - X[i])
        wynik = B[i+1] * c_minus_x
        suma += wynik
    return suma


BB = [1, -5, 3, 2]
XX = [0, 1, 2]
cc = -2
# powinien zwrocic -19

print(HornerNewton(BB, XX, cc))
