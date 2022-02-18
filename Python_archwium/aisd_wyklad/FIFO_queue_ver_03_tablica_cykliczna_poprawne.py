# coding: utf-8
# Implementacja kolejki FIFO jako Abstrakcyjnej Struktury Danych (ADT-Abstract Data Type)
# Implementacja oparta na ksiazce Cormen i inni "Wprowadzenie do algorytmow"
# Brak obslugi bledow (przepelnienie oraz niedomiar)
# Prosze to samemu uzupelnic !!!
# Ta implementacja jest generalnie optymalna, gdyz kazda operacja ma zlozonosc O(1), za wyjatkiem inicjalizacji w jezyku Python.
# W innych jezykch programowania (np C++) zlozonosci inicjalizacji tablicy moze byc stala
# materialy do wykladu AiSD, Michal Baczynski

class Queue:
    def __init__(self, n):  # zlozonosc O(n)
        """inicjalizacja"""
        self.items = n * [None]
        self.size = n
        self.head = 0
        self.tail = 0

    def isEmpty(self):  # zlozonosc O(1)
        """sprawdzenie czy kolejka FIFO jest pusta"""
        return self.head == self.tail

    def enqueue(self, item):  # zlozonosc O(1)
        """wstawienie elementu do kolejki FIFO"""
        # brak sprawdzenia, czy kolejka nie jest pelna!!!
        self.items[self.tail] = item
        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):  # zlozonosc O(1)
        """usuniecie elementu z kolejki FIFO"""
        # brak sprawdzenia, czy kolejka nie jest pusta!!!
        if self.head == self.size - 1:
            self.head = 0
        else:
            self.head += 1

    def first(self):  # zlozonosc O(1)
        """zwrocenie pierwszego elementu z kolejki FIFO"""
        # brak sprawdzenia, czy kolejka nie jest pusta!!!
        return self.items[self.head]

"""print("Kolejka FIFO - trzecia implementacja i ja mozna stosowac, ale brak obslugi bledow -- prosze to uzupelnic!")
a = Queue(5)
a.enqueue("a")
a.enqueue("b")
a.enqueue("c")
a.enqueue("d")
print(a.first())
print(a.first())
a.dequeue()
print(a.first())
a.dequeue()
a.enqueue("e")
print(a.first())
a.dequeue()
print(a.first())

#Program powinien wypisac
# a a b c d"""

k1 = Queue(6)
print(k1.items)
k1.enqueue(4)
print(k1.items)
k1.enqueue(1)
print(k1.items)
k1.dequeue() # dequeue 4
print(k1.items)
k1.enqueue(8)
print(k1.items)
k1.dequeue() # dequeue 1
print(k1.items)
k1.enqueue(4)
print(k1.items)
k1.enqueue(5)
print(k1.items)
k1.dequeue() # dequeue 3
print(k1.items)
k1.enqueue(2)
print(k1.items)
k1.enqueue(1)
k1.dequeue()
k1.dequeue()
k1.dequeue()
k1.dequeue()
print(k1.items)

print('PIERWSZY ELEMENT:', k1.first())