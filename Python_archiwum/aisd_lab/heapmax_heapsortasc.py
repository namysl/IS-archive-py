class Heap:  # maksimum
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

    def heapsort(self, new_list):
        """Sortowanie przez kopcowanie
        Zł. obl. przypadka pesymistycznego/średniego: O(n log n)
        niestabilny
        """
        self.build_heap(new_list)  # buduje kopiec z podanej listy
        size = self.heapsize
        # print(self.heaplist)

        while size > 1:
            # zamiana pierwszy (maksimum) z ostatnim:
            self.heaplist[1], self.heaplist[size] = self.heaplist[size], self.heaplist[1]
            size -= 1  # ostatni element jest juz posortowany, ograniczamy size do tych nieposortowanych
            self.fix_down(1, size)  # naprawa kopca (od pierwszego elementu do ostatniego nieposortowanego)

        return self.heaplist[1:]


k1 = Heap()
k1.insert(1)
k1.insert(2)
k1.insert(3)
k1.insert(4)
k1.insert(8)
k1.insert(6)

print(k1.heaplist)
print(k1.print_list())

"""
     8
   /  \
  4    6
 / \   /
1  3  2

"""

print('~~~~~~')
k2 = Heap()
print('pali')
k2.build_heap([6,12,8,5,45,7,20,1])
print(k2.print_list())

print('~~~~~~')
k3 = Heap()
print(k3.heapsort([16, 13, 1, 12, 2, 3, 5, 6]))
