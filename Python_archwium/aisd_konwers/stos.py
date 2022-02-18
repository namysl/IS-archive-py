"""Pokaż, jak można zaimplementować kolejkę FIFO, korzystając z dwóch
stosów (nie stosujemy w implementacji kolejki żadnej tablicy lub listy dowiązanej - tylko
dwa stosy). W swoim rozwiązaniu użyj standardowych operacji na stosie. Swoją odpowiedź
podaj w pseudokodzie oraz w języku Python.
Oszacuj czas działania operacji na takiej kolejce."""


class Stack:
    """Stos o zlozonosci O(1)"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):  # dodaje element na koniec, zlozonosc O(1)
        self.items.append(item)

    def pop(self):
        if not self.is_empty():  # usuwa element z konca, zlozonosc O(1)
            return self.items.pop()
        else:
            raise Exception('Pusty stack')


class FIFO:
    def __init__(self):
        """Zlozonosc O(n)"""
        self.stack1 = Stack()
        self.stack2 = Stack()

    def are_both_empty(self):
        if self.stack1.is_empty() and self.stack2.is_empty():
            return True

    def enqueue(self, item):
        """Zlozonosc O(1), wstawia element na koniec"""
        self.stack1.push(item)

    def dequeue(self):
        """Zlozonosc O(n) w przypadku, kiedy stos2 jest pusty, a stos1 nie;
        przenosi elementy z jednego na drugi za pomoca petli (O(n)), a same operacje
        push i pop maja zlozonosc O(1)"""
        if self.are_both_empty():
            return Exception('Kolejka jest pusta')

        elif not self.stack1.is_empty() and self.stack2.is_empty():
            while not self.stack1.is_empty():  # O(n)
                self.stack2.push(self.stack1.pop())
            self.stack2.pop()

        else:  # O(1)
            self.stack2.pop()


fifooo = FIFO()
fifooo.enqueue(10)
fifooo.enqueue(9)
fifooo.enqueue(8)
fifooo.enqueue(7)

print('s1:', fifooo.stack1.items)
print('s2:', fifooo.stack2.items)

fifooo.dequeue()

print('\ns1 po deq 10:', fifooo.stack1.items)
print('s2 po deq 10:', fifooo.stack2.items)

fifooo.dequeue()

print('\ns1 po deq 9:', fifooo.stack1.items)
print('s2 po deq 9:', fifooo.stack2.items)

fifooo.enqueue(1)

print('\ns1 po enq 1:', fifooo.stack1.items)
print('s2 po enq 1:', fifooo.stack2.items)

fifooo.dequeue()
fifooo.dequeue()

print('\ns1 po deq 7, 8:', fifooo.stack1.items)
print('s2 po deq 7, 8:', fifooo.stack2.items)

fifooo.dequeue()

print('\ns1 po deq 1:', fifooo.stack1.items)
print('s2 po deq 1:', fifooo.stack2.items)
