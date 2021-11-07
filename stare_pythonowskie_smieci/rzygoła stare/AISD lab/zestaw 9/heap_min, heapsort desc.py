class Heap:  # minimum
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

        while size > 1 and self.heaplist[size//2] > self.heaplist[size]:  # rodzic > ostatnie dziecko w liscie
            # zamiana miejsc rodzica i dziecka:
            self.heaplist[size//2], self.heaplist[size] = self.heaplist[size], self.heaplist[size//2]
            size = size // 2  # rodzic

    def build_heap(self, new_list):
        """Tworzy kopiec z podanej listy"""
        for element in new_list:
            self.heaplist.append(element)
            self.heapsize += 1
        self._build_heap()  # wywoluje funkcje przygotowujaca argumenty niezbedne dla naprawy kopca

    def _build_heap(self):
        for i in range(self.heapsize // 2, 0, -1):  # od indeksu size//2 do 1
            self.fix_down(i, self.heapsize)  # argumenty dla funkcji fix_down()

    def fix_down(self, i, size):
        """Naprawia porzadek kopca z gory na dol"""
        left = 2 * i  # potomek po lewej (indeks parzysty)
        right = 2 * i + 1  # potomek po prawej (indeks nieparzysty)
        smallest = i  # rodzic

        #print('smallest1:', smallest, 'left:', left, 'right:', right)

        if left <= size and self.heaplist[smallest] > self.heaplist[left]:  # rodzic > dziecko_left
            smallest = left  #
        if right <= size and self.heaplist[smallest] > self.heaplist[right]:  # rodzic > dziecko_right
            smallest = right
        if smallest != i:  # indeks w largest != oryginalny indeks rodzica
            self.heaplist[smallest], self.heaplist[i] = self.heaplist[i], self.heaplist[smallest]  # zamiana miejsc
            #print('smallest2:', largest)
            self.fix_down(smallest, size)  # rekurencyjnie dla podmienionego

    def extract_min(self):
        """Zwraca maksimum, nastepnie zamienia miejscami z ostatnim elementem,
        nastepnie usuwa maksimum z ostatniego indeksu
        """
        minimum = self.heaplist[1]
        self.heaplist[1] = self.heaplist[-1]  # zamiana miejsc minimum i ostatniego elementu
        self.heapsize -= 1
        self.heaplist.pop()  # usuwa min
        self.fix_down(1, self.heapsize)  # naprawia kopiec z gory na dol
        return minimum

    def heapsort(self, new_list):
        """Sortowanie przez kopcowanie
        Zł. obl. przypadka pesymistycznego/średniego: O(n log n)
        niestabilny
        """
        self.build_heap(new_list)  # buduje kopiec z podanej listy
        size = self.heapsize
        # print(self.heaplist)

        while size > 1:
            # zamiana pierwszy (minimum) z ostatnim:
            self.heaplist[1], self.heaplist[size] = self.heaplist[size], self.heaplist[1]
            size -= 1  # ostatni element jest juz posortowany, ograniczamy size do tych nieposortowanych
            self.fix_down(1, size)  # naprawa kopca (od pierwszego elementu do ostatniego nieposortowanego)

        return self.heaplist[1:]


k1 = Heap()
k1.insert(10)
k1.insert(9)
k1.insert(8)
k1.insert(4)
k1.insert(2)
k1.insert(6)

"""
     2
   /  \
  4    6
 / \   /
10  8  9

"""
print(k1.print_list())
print(k1.heaplist)

print('~~~~~~')

k2 = Heap()
k2.build_heap([8, 2, 1, 3, 5, 6])
print(k2.print_list())
print(k2.extract_min())

print('~~~~~~')
k3 = Heap()
print(k3.heapsort([16, 13, 1, 12, 2, 3, 5, 6]))
