# Ewa Namysł, gr.6

"""
Funkcja, która wyznacza najwieksza liczbe palindromiczna
powstala jako iloczyn liczb czterocyfrowych, zwracajaca
krotke zawierajaca liczby oraz wynik ich mnozenia.
"""

ilucyfr = 4

def najpali(ilucyfr):

    gora = 0
    for a in range(1, ilucyfr + 1):
        gora = (gora * 10) + 9
    dol = int((gora + 1) / 10)

    maks = 0

    for b in range(gora, dol - 1, -1):
        for c in range(b, dol - 1, -1):

            iloczyn = c * b
            if (iloczyn < maks):
                break

            liczba = iloczyn
            wspak = 0

            while (liczba > 0):
                wspak = (liczba % 10) + (wspak * 10)
                liczba = int(liczba / 10)

            if (iloczyn == wspak and iloczyn > maks):
                maks = iloczyn
                krotka = (maks, b, c)

    return krotka


print("Najwiekszy palindrom liczbowy stworzony z", ilucyfr, "cyfrowych liczb:")
print(najpali(ilucyfr))
