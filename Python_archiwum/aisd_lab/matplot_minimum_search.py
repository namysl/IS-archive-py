import random
import time
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


def szukaj_minimum(A):
    minimum = A[0]
    for i in range(len(A)):
        if minimum > A[i]:
            minimum = A[i]
    return minimum


def generuj_liste():
    nowalista = []
    for _ in range(0, 1000):
        nowalista.append(random.randint(0, 10000))
    return nowalista


def generuj_osie(lista):
    x = []
    y = []

    for j in range(1, len(lista) + 1):
        czasy = 0
        for _ in range(0, 10):
            start = time.time()
            szukaj_minimum(lista[0:j])
            end = time.time()
            czasy += end - start
        x.append(j)
        y.append(czasy)

    return x, y


def rysuj_wykres(osie):
    figure(figsize=(16, 10))
    plt.plot(osie[0], osie[1], linewidth=1.0)
    plt.xlabel('list')
    plt.ylabel('time')
    plt.grid(True)
    plt.show()


wygenerowana_lista = generuj_liste()
xy = generuj_osie(wygenerowana_lista)
rysuj_wykres(xy)
