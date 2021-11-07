"""Przeanalizuj wynik wykonania ciągu następujacych operacji:

Q.enqueue(4)
Q.enqueue(1)
Q.enqueue(3)
Q.dequeue()
Q.enqueue(8)
Q.dequeue()
Q.enqueue(4)
Q.enqueue(5)
Q.dequeue()
Q.enqueue(2)
Q.enqueue(1)

na początkowej pustej kolejce Q zaimplementowanej:

• za pomocą podanej na wykładzie listy cyklicznej
(zakładamy, że początkowo pusta tablica ma 6 miejsc).
• za pomocą listy dowiązanej
(podanie takiej pełnej implementacji jest też zadaniem na laboratorium)."""


class ListaCykliczna:
    """lista nigdy się nie kończy, elementy są nadpisywane,
    zmienany jest indeks początku listy"""
    def __init__(self, n):  # inicjalizacja -> zlozonosc O(n)
        self.items = n * [None]
        self.size = n
        self.head = 0
        self.tail = 0

    def is_empty(self):  # zlozonosc O(1)
        """sprawdzenie czy kolejka jest pusta"""
        return self.head == self.tail

    def is_full(self):
        """sprawdzenie czy kolejka jest pelna"""
        return (self.tail + 1) % self.size == self.head

    def enqueue(self, item):  # zlozonosc O(1)
        """wstawienie elementu"""
        if self.is_full():
            raise Exception("Kolejka jest pelna")
        self.items[self.tail] = item
        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):  # zlozonosc O(1)
        """usuniecie elementu"""
        if self.is_empty():
            raise Exception("Kolejka jest pusta")
        x = self.items[self.head]
        if self.head == self.size - 1:
            self.head = 0
        else:
            self.head += 1
        return x

    def first(self):  # zlozonosc O(1)
        """zwrocenie pierwszego elementu z kolejki FIFO"""
        return self.items[self.head]


print('Lista cykliczna:')
k1 = ListaCykliczna(6)
print(k1.items)
k1.enqueue(4)
print(k1.items)
k1.enqueue(1)
print(k1.items)
k1.dequeue()  # dequeue 4
print(k1.first())
k1.enqueue(8)
print(k1.items)
k1.dequeue()  # dequeue 1
print(k1.items)
k1.enqueue(4)
print(k1.items)
k1.enqueue(5)
print(k1.items)
k1.dequeue()  # dequeue 3
print(k1.items)
k1.enqueue(2)
print(k1.items)
k1.enqueue(1)
print(k1.items)

print('PIERWSZY ELEMENT:', k1.first())



class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.previous = None


class ListaDowiazana:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def lprint(self):
        """Zlozonosc O(n) dla wyswietlenia wszystkich node'ow"""
        current = self.head
        while current is not None:
            print(current.item)
            current = current.next

    def enqueue(self, item):
        """Zlozonosc O(1)"""
        tail = self.tail
        self.tail = Node(item)

        if self.is_empty():
            self.head = self.tail
        else:
            tail.next = self.tail
            self.tail.previous = tail
        self._size += 1

    def dequeue(self):
        """Zlozonosc O(1)"""
        x = self.head.item

        if self.is_empty():
            raise Exception('Kolejka jest pusta')
        self.head = self.head.next
        self._size -= 1
        return x


k2 = ListaDowiazana()
k2.enqueue(4)
k2.enqueue(1)
k2.enqueue(3)
k2.dequeue()  # dequeue 4
k2.enqueue(8)
k2.dequeue()  # dequeue 1
k2.enqueue(4)
k2.enqueue(5)
k2.dequeue()  # dequeue 3
k2.enqueue(2)
k2.enqueue(1)
print('\nLista dowiazana:')
k2.lprint()
