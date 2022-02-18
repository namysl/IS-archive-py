class Sortowanie:
    def __init__(self, lista):
        self.lista = lista

    def insertion_sort(self):
        """Sortowanie przez wstawianie"""
        lista = self.lista[:]
        n = len(lista)

        for i in range(1, n):
            klucz = lista[i]
            j = i - 1
            while j >= 0 and lista[j] > klucz:
                lista[j+1] = lista[j]
                j -= 1
            lista[j+1] = klucz
        return lista

    def merge_sort(self):
        """Sortowanie przez scalanie - rekurencyjne"""
        if len(self.lista) > 1:
            m = len(self.lista) // 2
            left = self.lista[:m]
            right = self.lista[m:]

            leftsorter = Sortowanie(left)
            leftsorter.merge_sort()
            rightsorter = Sortowanie(right)
            rightsorter.merge_sort()

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

    def bubble_sort(self):
        """Sortowanie bąbelkowe"""
        copylist = self.lista[:]
        n = len(copylist)

        for i in range(n):
            for j in range(0, n - i - 1):
                if copylist[j] > copylist[j+1]:
                    copylist[j], copylist[j+1] = copylist[j+1], copylist[j]
        return copylist

    def counting_sort(self):
        """Sortowanie przez zliczanie"""
        copylist = self.lista[:]
        n = len(copylist)
        gora = max(copylist)

        temp = [0] * (gora + 1)

        for i in copylist:
            temp[i] += 1

        for i in range(1, gora + 1):
            temp[i] += temp[i - 1]

        wynik = [0] * n
        i = n-1

        while i >= 0:
            wynik[temp[copylist[i]] - 1] = copylist[i]
            temp[copylist[i]] -= 1
            i -= 1

        return wynik

    def insertion_sentinel(self):
        """Sortowanie przez wstawianie z wartownikiem"""
        copylist = self.lista[:]

        copylist[0] = -1
        for i in range(2, len(copylist)):
            klucz = copylist[i]
            j = i - 1
            while copylist[j] > klucz:
                copylist[j + 1] = copylist[j]
                j -= 1
            copylist[j + 1] = klucz
        return copylist

    # MERGE SORT v2
    def _mergeit(self, lista1, lista2):
        """Funkcja pomocnicza sortowania przez scalanie"""
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
        """Funkcja pomocnicza sortowania przez scalanie"""
        len_lista = len(lista)

        if len_lista == 0 or len_lista == 1:
            return lista

        len_lista = len_lista // 2

        nowa_lista = self._mergeit(self._merge_new_list(lista[:len_lista]),
                                   self._merge_new_list(lista[len_lista:]))

        return nowa_lista

    def mergesort(self):
        """Sortowanie przez scalanie - v2"""
        lista = self.lista
        return self._merge_new_list(lista)


jakaslista = Sortowanie([9, 8, 7, 4, 5, 6, 3, 2, 1])

print(jakaslista.insertion_sort())
print('*'*10)
print(jakaslista.merge_sort())
print('*'*10)
print(jakaslista.bubble_sort())
print('*'*10)
print(jakaslista.counting_sort())
print('*'*10)
print(jakaslista.insertion_sentinel())
print('*'*10)
print(jakaslista.mergesort())
