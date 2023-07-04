import numpy as np


def macierz_odwrotna(macierz):
    try:
        odwrocona = np.linalg.inv(macierz)
        return odwrocona
    except np.linalg.LinAlgError:
        raise ValueError("Podana macierz jest osobliwa (nieodwracalna).")


A = np.array([[1, 2], [3, 4]])
A_odwrocona = macierz_odwrotna(A)
print("Macierz A:")
print(A)
print("Macierz odwrotna do A:")
print(A_odwrocona)
