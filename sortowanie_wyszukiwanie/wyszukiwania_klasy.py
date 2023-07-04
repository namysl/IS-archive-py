class Wyszukiwania:
    def __init__(self, lista):
        assert isinstance(lista, (list, tuple)), 'argument musi byc lista lub krotka'
        for element in lista:
            assert isinstance(element, (int, float)), 'elementy musza byc typu float lub int'

        self.lista = lista

    def liniowe(self, szukany_el):
        """Zwraca indeks, jesli szukany element znajduje sie w liscie,
        w przeciwnym wypadku zwraca False
        """
        for i in range(len(self.lista)):
            if self.lista[i] == szukany_el:
                return i
        return False

    def binarne_iter(self, szukany_el):
        """ITERACYJNE wyszukiwanie binarne
        Zwraca indeks, jesli szukany element znajduje sie w liscie,
        w przeciwnym wypadku zwraca False.
        Lista musi byc posortowana
        """
        low = 0
        high = len(self.lista) - 1

        while low <= high:
            mid = (high + low) // 2

            if self.lista[mid] < szukany_el:
                low = mid + 1
            elif self.lista[mid] > szukany_el:
                high = mid - 1
            else:
                return mid
        return False

    def binarne_rekur(self, item, low=0, high=None):
        """REKURENCYJNE wyszukiwanie binarne
        Zwraca indeks, jesli szukany element znajduje sie w liscie,
        w przeciwnym wypadku zwraca False.
        Lista musi byc posortowana
        """
        if high is None:
            high = len(self.lista)
        mid = low + (high - low) // 2

        if high - low + 1 <= 0 or mid == high:
            return False
        else:
            guess = self.lista[mid]
            if guess == item:
                return mid
            if item < guess:
                return self.binarne_rekur(item, low, mid)
            else:
                return self.binarne_rekur(item, (mid + 1), high)


jakaslista = Wyszukiwania([1, 2, 4, 6, 98])
print(jakaslista.liniowe(2))
print(jakaslista.binarne_iter(2))
print(jakaslista.binarne_rekur(2))
