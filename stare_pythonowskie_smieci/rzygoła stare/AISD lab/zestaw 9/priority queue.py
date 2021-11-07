# 2 b)
class PQlista:
    """Kolejka priorytetowa jako lista"""
    def __init__(self):
        self.lista = []
        self.priorytet = []

    def is_empty(self):
        if len(self.lista) == 0:
            return True

    def add_element(self, element, priorytet):  # dodaje do listy krotkę z elementem (wartosc) i jego priorytetem
        """O(1) -> dodaje na koniec"""
        self.lista.append(element)
        self.priorytet.append(priorytet)

    def pop(self):  # usuwa element z najwiekszym priorytetem
        """zlozonosc O(n)?"""
        max_indeks = 0

        for indeks in range(1, len(self.priorytet)):
            if self.priorytet[indeks] > self.priorytet[indeks-1]:
                max_indeks = indeks

        usuwany = self.lista.pop(max_indeks)
        self.priorytet.pop(max_indeks)
        return usuwany


pqlist = PQlista()
pqlist.add_element('lis', 1)
pqlist.add_element('sowa', 2)
pqlist.add_element('kamien', 1)
pqlist.add_element('zajac', 3)
pqlist.add_element('las', 5)
pqlist.add_element('drzewo', 4)

print(pqlist.lista, pqlist.priorytet)
print(pqlist.pop())
print(pqlist.lista, pqlist.priorytet)
print(pqlist.pop())
print(pqlist.lista, pqlist.priorytet)

print('~~~')


# 2 a)
class PQkopiec:
    """Kolejka priorytetowa jako kopiec"""
    def __init__(self):
        self.heaplist = [None]
        self.heapsize = 0

    def print_list(self):
        """Zwraca liste z kopcem (bez pustego indeksu 0)"""
        return self.heaplist[1:]

    def insert(self, item):
        """Wstawia element do kopca, nastepnie naprawia wlasnosc kopca"""
        self.heaplist.append(item)
        self.heapsize += 1
        self.fix_up()  # przywraca w kopcu porzadek po dodaniu elementu na koniec

    def fix_up(self):
        """Naprawia porzadek kopca z dolu do gory"""
        size = self.heapsize

        while size > 1 and self.heaplist[size//2] < self.heaplist[size]:  # rodzic < ostatnie dziecko w liscie
            # zamiana miejsc rodzica i dziecka:
            self.heaplist[size//2], self.heaplist[size] = self.heaplist[size], self.heaplist[size//2]
            size = size // 2  # rodzic

    def fix_down(self, i, size):
        """Naprawia porzadek kopca z gory na dol"""
        left = 2 * i  # potomek po lewej (indeks parzysty)
        right = 2 * i + 1  # potomek po prawej (indeks nieparzysty)
        largest = i  # rodzic

        #print('largest1:', largest, 'left:', left, 'right:', right)

        if left <= size and self.heaplist[largest] < self.heaplist[left]:  # rodzic < dziecko_left
            largest = left  #
        if right <= size and self.heaplist[largest] < self.heaplist[right]:  # rodzic < dziecko_right
            largest = right
        if largest != i:  # indeks w largest != oryginalny indeks rodzica
            self.heaplist[largest], self.heaplist[i] = self.heaplist[i], self.heaplist[largest]  # zamiana miejsc
            #print('largest2:', largest)
            self.fix_down(largest, size)  # rekurencyjnie dla podmienionego

    def extract_max(self):
        """Zwraca maksimum, nastepnie zamienia miejscami z ostatnim elementem,
        nastepnie usuwa maksimum z ostatniego indeksu
        """
        maximum = self.heaplist[1]
        self.heaplist[1] = self.heaplist[-1]  # zamiana miejsc maksimum i ostatniego elementu
        self.heapsize -= 1
        self.heaplist.pop()  # usuwa maks
        self.fix_down(1, self.heapsize)  # naprawia kopiec z gory na dol
        return maximum


pqheap = PQkopiec()
pqheap.insert((10, 'a'))
pqheap.insert((1, 'b'))
pqheap.insert((5, 'c'))
pqheap.insert((11, 'd'))
pqheap.insert((9, 'e'))
pqheap.insert((8, 'f'))
print(pqheap.print_list())

print(pqheap.extract_max())
print(pqheap.print_list())
