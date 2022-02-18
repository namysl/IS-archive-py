class ListaLiczb:
    def __init__(self, lista):
        assert isinstance(lista, (list, tuple)), "argument musi byc obiektem sekwencyjnym"

        for el in lista:
            assert isinstance(el, (float, int)), "tylko float lub int"

        # self.lista = lista
        self.lista = [el for el in lista]

    def bubble(self):
        n = len(self.lista)

        for i in range(n):
            for j in range(0, n - i - 1):
                if self.lista[j] > self.lista[j + 1]:
                    self.lista[j], self.lista[j + 1] = self.lista[j + 1], self.lista[j]
        return self.lista

    def merge(self):
        """Dziala tylko z self.lista = lista"""
        if len(self.lista) > 1:
            m = len(self.lista) // 2
            left = self.lista[:m]
            right = self.lista[m:]

            leftsorter = ListaLiczb(left)
            leftsorter.merge()
            rightsorter = ListaLiczb(right)
            rightsorter.merge()

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    self.lista[k] = left[i]
                    i += 1
                else:
                    self.lista[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                self.lista[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                self.lista[k] = right[j]
                j += 1
                k += 1

        return self.lista

    def _mergeit(self, lista1, lista2):
        len_lista1 = len(lista1)
        len_lista2 = len(lista2)
        i1 = 0
        i2 = 0
        lista = []

        for i in range(len_lista1 + len_lista2):
            if i1 == len_lista1:
                lista.append(lista2[i2])
                i2 += 1
            elif i2 == len_lista2:
                lista.append(lista1[i1])
                i1 += 1
            elif lista1[i1] < lista2[i2]:
                lista.append(lista1[i1])
                i1 += 1
            else:
                lista.append(lista2[i2])
                i2 += 1

        return lista

    def _merge_new_list(self, lista):
        len_lista = len(lista)

        if len_lista == 0 or len_lista == 1:
            return lista

        len_lista = len_lista // 2

        nowa_lista = self._mergeit(self._merge_new_list(lista[:len_lista]),
                                          self._merge_new_list(lista[len_lista:]))

        return nowa_lista

    def mergesort(self):
        lista = self.lista
        return self._merge_new_list(lista)

    def wybor(self, metoda="bubble"):
        if metoda == "bubble":
            return self.bubble()
        elif metoda == "merge":
            return self.mergesort()
        else:
            print("Blad lub brak danej metody")

    def get_lista(self):
        return self.lista

    def set_lista(self, nowalista):
        assert isinstance(nowalista, (list, tuple)), "Tylko list lub tuple"
        for el in self.lista:
            assert isinstance(el, (float, int)), "Tylko float lub int"
        self.lista = nowalista

    def add_element(self, liczba):
        assert isinstance(liczba, (float, int)), "Tylko float lub int"
        self.lista.append(liczba)

    def get_sorted(self):
        return self.bubble()


l1 = ListaLiczb((1, 2, 5, 3))
l1.add_element(2)
l1.get_lista()
print(l1.mergesort())

l2 = ListaLiczb([2, 16, 11, 77, 1, 2, 10, 5])
print(l2.wybor('merge'))

l3 = ListaLiczb((60, 70, 2, 666, 11, 9, 16, 2000, 21, 1))
print(l3.mergesort())
