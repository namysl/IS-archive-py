import time
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import random


def selection_sort(tab):
    n = len(tab)

    for i in range(n):
        minimum = i
        for j in range(i + 1, n):
            if tab[minimum] > tab[j]:
                minimum = j
        tab[i], tab[minimum] = tab[minimum], tab[i]
    return tab


def generuj_liste(przypadek="sredni"):
    """Generuje liste w zaleznosci od wybranego przypadku"""

    if przypadek == "optymistyczny":
        nowalista = list(range(0, 500))
    elif przypadek == "pesymistyczny":
        nowalista = list(range(0, 500))
        nowalista.reverse()
    elif przypadek == "sredni":
        nowalista = []
        for _ in range(0, 500):
            nowalista.append(random.randint(-10000, 10000))
    return nowalista


def generuj_osie(lista):
    """Mierzy czas i zwraca osie dla wykresow"""
    x = []
    y = []

    for j in range(1, len(lista) + 1):
        for _ in range(0, 10):
            start = time.time()
            selection_sort(lista[0:j])
            end = time.time()
        x.append(j)
        y.append(end - start)
    return x, y


def rysuj_wykres(osie):
    """Indywidualny wykres dla wybranego przypadku"""

    figure(figsize=(16, 10))
    plt.plot(osie[0], osie[1], linewidth=1.0)
    plt.xlabel('list')
    plt.ylabel('time')
    plt.grid(True)
    plt.show()


# wygenerowana_lista = generuj_liste("optymistyczny")
# print(wygenerowana_lista)
# xy = generuj_osie(wygenerowana_lista)
# rysuj_wykres(xy)


def wykres_polaczony():
    """Wykres dla trzech roznych przypadkow"""

    wygenerowana_lista1 = generuj_liste("optymistyczny")
    print(wygenerowana_lista1)
    xy1 = generuj_osie(wygenerowana_lista1)

    wygenerowana_lista2 = generuj_liste("sredni")
    print(wygenerowana_lista2)
    xy2 = generuj_osie(wygenerowana_lista2)

    wygenerowana_lista3 = generuj_liste("pesymistyczny")
    print(wygenerowana_lista3)
    xy3 = generuj_osie(wygenerowana_lista3)

    figure(figsize=(16, 10))
    plt.plot(xy1[0], xy1[1], linewidth=1.0, label='optymistyczny')
    plt.plot(xy2[0], xy2[1], linewidth=1.0, label='średni')
    plt.plot(xy3[0], xy3[1], linewidth=1.0, label='pesymistyczny')
    plt.xlabel('list')
    plt.ylabel('time')
    plt.grid(True)
    plt.legend(prop={"size": 20})
    plt.show()


wykres_polaczony()
