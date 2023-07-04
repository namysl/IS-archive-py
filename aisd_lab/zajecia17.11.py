# bufory cykliczne z wykorzystaniem kolejki:

# 1) Przyklad z wykladu uzupelniony o obsluge bledow - kolejka jest pusta lub pelna

class Queue1:
    def __init__(self, n):  # zlozonosc O(n)
        """inicjalizacja ma wieksza zlozonosc niz wstawianie do kolejki itd."""
        self.items = n * [None]
        self.size = n
        self.head = 0
        self.tail = 0

    def isEmpty(self):  # zlozonosc O(1)
        """sprawdzenie czy kolejka FIFO jest pusta"""
        return self.head == self.tail

    def isFull(self):
        return (self.tail + 1) % self.size == self.head

    def enqueue(self, item):  # zlozonosc O(1)
        """wstawienie elementu do kolejki FIFO"""
        if self.isFull():
            raise Exception("Queue is full")
        self.items[self.tail] = item
        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):  # zlozonosc O(1)
        """usuniecie elementu z kolejki FIFO"""
        if self.isEmpty():
            raise Exception("Queue is Empty")
        x = self.items[self.head]
        if self.head == self.size - 1:
            self.head = 0
        else:
            self.head += 1
        return x

#     def dequeue(self):  # zlozonosc O(1)
#         """usuniecie elementu z kolejki FIFO"""
#         # brak sprawdzenia, czy kolejka nie jest pusta!!!
#         if self.head == self.size - 1:
#             self.head = 0
#         else:
#             self.head += 1

#     def first(self):  # zlozonosc O(1)
#         """zwrocenie pierwszego elementu z kolejki FIFO"""
#         # brak sprawdzenia, czy kolejka nie jest pusta!!!
#         return self.items[self.head]


print('1)')
a = Queue1(3)
a.enqueue(1)
print(a.items)
a.enqueue(1)
print(a.items)
#a.enqueue(1)
#print(a.items)


# 2) Przykład ze zdefiniowaniem rozmiaru tablicy
class Queue2:
    def __init__(self, size):
        self.start = 0
        self.end = 0
        self.n = size + 1
        self.tablica = [None for _ in range(size + 1)]

    def isFull(self):
        return self.zwieksz(self.end) == self.start

    def isEmpty(self):
        return self.end == self.start

    def size(self):
        if self.end >= self.start:
            return self.end - self.start
        else:
            self.n - self.start + self.end

    def enqueue(self, a):
        if self.isFull():
            raise Exception("Queue is full")
        else:
            self.tablica[self.end] = a
            self.end = self.zwieksz(self.end)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is Empty")
        else:
            result = self.tablica[self.start]
            self.start = self.zwieksz(self.start)

            return result

    def zwieksz(self, a):
        return (a + 1) % self.n


print('2)')
b = Queue2(3)
b.enqueue(2)
print(b.tablica)
b.enqueue(2)
print(b.tablica)
#b.enqueue(2)
#print(b.tablica)


# 3) Opcja z flagami: (rozwiązany problem wskaźnika zapisu i odczytu)
class Queue3:
    def __init__(self, n):  # zlozonosc O(n)
        self.items = n * [None]
        self.size = n
        self.head = 0
        self.tail = 0
        self.empty = True
        self.full = False

    def enqueue(self, item):  # zlozonosc O(1)
        if self.full:
            raise Exception('Queue is full')
        else:
            self.items[self.tail] = item
            self.empty = False
        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail += 1

        if self.head == self.tail:
            self.full = True

    def dequeue(self):  # zlozonosc O(1)
        if self.empty:
            raise Exception('Queue is empty')
        else:
            x = self.items[self.head]
            self.full = False

        if self.head == self.size - 1:
            self.head = 0
        else:
            self.head += 1

        if self.head == self.tail:
            self.empty = True
            return x


print('3)')
c = Queue3(3)
print(c.items)
c.enqueue(3)
print(c.items)
c.enqueue(3)
print(c.items)
c.enqueue(3)
print(c.items)


# 4) Opcja z licznikiem
class Queue4:
    def __init__(self, n):  # zlozonosc O(n)
        self.items = n * [None]
        self.size = n
        self._size = 0
        self.head = 0
        self.tail = 0

    def isEmpty(self):
        return self.head == self.tail

    def isFull(self):
        return self._size == self.size

    def enqueue(self, item):  # zlozonosc O(1)
        if self.isFull():
            raise ValueError('Queue is full')
        self.items[self.tail] = item
        self._size += 1

        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):  # zlozonosc O(1)
        if self.isEmpty():
            raise ValueError('Queue is empty')
        self._size -= 1
        if self.head == self.size - 1:
            self.head = 0
        else:
            self.head += 1

    def first(self):
        if self.isEmpty():
            raise ValueError('Queue is empty')
        return self.items[self.head]


print('4)')
d = Queue4(3)
print(d.items)
d.enqueue(4)
print(d.items)
d.enqueue(4)
print(d.items)
d.enqueue(4)
print(d.items)

print('~~~~~~~~~~~~~~~~~~~~')
# Linked List
class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.tail = 0


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, item):  # O(n)
        NewNode = Node(item)
        if self.head.item is None:
            self.head = NewNode
        else:  # jak znalezc ostatni
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = NewNode

    def append2(self, item):  # O(1)
        NewNode = Node(item)
        if self.head.item is None:
            self.head = NewNode
        else:
            pass

    def show_next(self):
        current = self.head
        print(current.item)
        while current.next is not None:
            current = current.next
            print(current.item)

    def dlugosc(self):
        if self.head.item is None:
            return 0

        current = self.head
        i = 1
        while current.next is not None:
            current = current.next
            i += 1
        return i

    def pop(self, element):
        pass


link = LinkedList()
link.append(1)
link.append(2)
link.append(4)
link.append(8)  # złożoność liniowa
print('show_next:', link.show_next())
print('len:', link.dlugosc())  # złożoność liniowa
