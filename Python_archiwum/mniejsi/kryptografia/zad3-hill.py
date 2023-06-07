import numpy as np
import string
import random
from sympy import Matrix


def zaszyfruj(do_zaszyfrowania, klucz, wymiary_macierzy=3):
    do_zaszyfrowania = do_zaszyfrowania.upper()
    alfabet = string.ascii_uppercase
    zaszyfrowane = ""

    for index, i in enumerate(do_zaszyfrowania):
        values = []
        if index % wymiary_macierzy == 0:
            for j in range(0, wymiary_macierzy):
                if index + j < len(do_zaszyfrowania):
                    values.append([alfabet.index(do_zaszyfrowania[index + j])])
                else:
                    values.append([random.randint(0, 25)])
            vector = np.matrix(values)
            vector = klucz * vector
            vector %= 26
            for j in range(0, wymiary_macierzy):
                zaszyfrowane += alfabet[vector.item(j)]

    return zaszyfrowane


def odszyfruj(zaszyfrowane, klucz, wymiary_macierzy=3):
    zaszyfrowane = zaszyfrowane.upper()
    alfabet = string.ascii_uppercase
    odszyfrowane = ""
    klucz = Matrix(klucz).inv_mod(26).tolist()

    for index, i in enumerate(zaszyfrowane):
        values = []
        if index % wymiary_macierzy == 0:
            for j in range(0, wymiary_macierzy):
                values.append([alfabet.index(zaszyfrowane[index + j])])
            vector = np.matrix(values)
            vector = klucz * vector
            vector %= 26
            for j in range(0, wymiary_macierzy):
                odszyfrowane += alfabet[vector.item(j)]

    return odszyfrowane


moj_klucz = np.matrix([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
tekst = "kryptografia"

test_zasz = zaszyfruj(tekst, moj_klucz)
print(test_zasz)

test_odsz = odszyfruj(test_zasz, moj_klucz)
print(test_odsz)
