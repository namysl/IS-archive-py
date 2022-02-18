# 1.Stwórz klasę LinkedList. Jaka jest złożoność dodawania elementu na koniec listy.
class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None


class LinkedList1:
    """Zlozonosc liniowa"""
    def __init__(self):
        self.head = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def show_all(self):
        current = self.head
        while current is not None:
            print(current.item)
            current = current.next

    def add_end(self, item):  # O(n), uzywa petli
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self._size += 1

    def del_first(self):
        val = self.head.item

        if self.is_empty():
            raise Exception('pusta lista')

        self.head = self.head.next
        self._size -= 1

        return val


print('LinkedList1 O(n)')
link1 = LinkedList1()
link1.add_end(1)
link1.add_end(2)
link1.add_end(4)
link1.add_end(8)
link1.add_end(16)
print('len:', link1.size())
link1.del_first()
print('len:', link1.size())

print('\nshow_all:'), link1.show_all()

print('~~~~~~')


# 2. Stwórz klasę LinkedList, w której dodawanie elementu na koniec listy będzie
# miało złożoność O(1).
class LinkedList2:
    """
    show_all() -> zlozonosc O(n)
    add_end()  -> zlozonosc O(1)"""
    def __init__(self):
        self.head = None
        self.tail = None  # dodany ogon
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def show_all(self):
        if self.is_empty():
            return Exception('pusta lista')

        string = str(self.head.item)
        nastepny = self.head.next
        while nastepny is not None:
            string += ' -> ' + str(nastepny.item)
            nastepny = nastepny.next
        return string

    def add_start(self, item):  # O(1); wstawia na poczatek
        new = Node(item)
        new.next = self.head
        self.head = new
        self._size += 1

    def add_end(self, item):  # O(1) dodawanie elementu na koniec
        tail = self.tail
        self.tail = Node(item)

        if self.is_empty():
            self.head = self.tail
        else:
            tail.next = self.tail
        self._size += 1

    def del_first(self):
        val = self.head.item

        if self.is_empty():
            raise Exception('pusta lista')

        self.head = self.head.next
        self._size -= 1

        return val


print('LinkedList2 O(1)')
link2 = LinkedList2()
link2.add_end(1)
link2.add_end(2)
link2.add_end(4)
link2.add_end(8)
link2.add_end(16)
link2.add_start(32)
print('len:', link2.size())

link2.del_first()  # usuwa 32
print('len:', link2.size())

link2.show_all()

print('~~~~~~')


# 3. Stwórz klasę LinkedList dwukierunkową,
# taką dla której wszystkie operacje dodawania i usuwania miały złożoność O(1).

class Node2:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def show_all(self):
        if self.is_empty():
            return Exception('pusta lista')

        string = str(self.head.item)
        nastepny = self.head.next
        while nastepny is not None:
            string += ' -> ' + str(nastepny.item)
            nastepny = nastepny.next
        return string

    def add_start(self, item):
        new = Node(item)
        new.next = self.head
        self.head = new
        self._size += 1

    def add_end(self, item):
        tail = self.tail
        self.tail = Node2(item)
        if self.is_empty():
            self.head = self.tail
        else:
            tail.next = self.tail
            self.tail.previous = tail
        self._size += 1

    def del_first(self):
        if self.is_empty():
            raise Exception('LL pusta')

        val = self.head.item
        self.head = self.head.next
        self._size -= 1
        return val

    def del_last(self):
        if self.is_empty():
            raise Exception('pusta')

        val = self.tail.item
        self._size -= 1

        if self.is_empty():
            self.tail = Node()
            self.head = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        return val


print('DoublyLinkedList')
link3 = DoublyLinkedList()
link3.add_end(1)
link3.add_end(2)
link3.add_end(4)
link3.add_end(8)
link3.add_end(16)
print('len:', link3.size())
print(link3.show_all())
link3.del_last()
link3.del_last()
link3.del_last()
link3.del_first()
link3.del_first()
print('len:', link3.size())

print('~~~~~~')


# 4. Stwórz klasę OrderedList (dziedziczącą z LinkedList).
class OrderedList(LinkedList2):
    def sort(self):
        for i in range(self.size()-1):
            # pierwszy element:
            current = self.head
            next_link = current.next
            previous = None

            while next_link is not None:
                if current.item > next_link.item:
                    if previous is None:
                        previous = current.next
                        next_link = next_link.next
                        previous.next = current
                        current.next = next_link
                        self.head = previous
                    else:
                        temp = next_link
                        next_link = next_link.next
                        previous.next = current.next
                        previous = temp
                        temp.next = current
                        current.next = next_link
                else:  # przypadek <=, wskazanie na kolejny
                    previous = current
                    current = current.next
                    next_link = next_link.next
            i += 1


print('OrderedList')
ord1 = OrderedList()
ord1.add_end(3)
ord1.add_end(4)
ord1.add_end(1)
ord1.add_end(2)
ord1.sort()
print(ord1.show_all())

print('~~~~~~')


# 5. Zaimplementuj stos używając LinkedList.
class Node3:
    def __init__(self, item=None):
        self.item = item
        self.next = None


class StackLL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def show_all(self):
        iternode = self.head
        if self.is_empty():
            return Exception('stos pusty')
        else:
            while iternode is not None:
                print(iternode.item, "->", end=" ")
                iternode = iternode.next
            return

    def push(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            newnode = Node(item)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.is_empty():
            return Exception('stos pusty')
        else:
            del_val = self.head
            self.head = self.head.next
            del_val.next = None
            return del_val.item


print('Stack LL')
stos1 = StackLL()
stos1.push(1)
stos1.push(2)
stos1.push(3)
stos1.push(4)
stos1.push(5)
stos1.pop()
stos1.show_all()
print('\n~~~~~~')


# 6. Zaimplementuj kolejkę używając LinkedList.

class Node4:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.previous = None


class QueueLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def show_all(self):
        iternode = self.head
        if self.is_empty():
            return Exception('kolejka pusta')
        else:
            while iternode is not None:
                print(iternode.item, "->", end=" ")
                iternode = iternode.next
            return

    def enqueue(self, item):
        tail = self.tail
        self.tail = Node4(item)
        if self.is_empty():
            self.head = self.tail
        else:
            tail.next = self.tail
            self.tail.previous = tail
        self._size += 1

    def dequeue(self):
        val = self.head.item
        if self.is_empty():
            raise Exception('kolejka pusta')
        self.head = self.head.next
        self._size -= 1

        return val


print('Queue LL')
stos1 = QueueLL()
stos1.enqueue(1)
stos1.enqueue(2)
stos1.enqueue(3)
stos1.enqueue(4)
stos1.enqueue(5)
stos1.dequeue()

stos1.show_all()

print('\n~~~~~~')


# 7. Zaimplementuj kolejkę FIFO jako tablicę cykliczną.
class Queue:
    def __init__(self, n):
        self.items = n * [None]
        self.size = n
        self.head = 0
        self.tail = 0
        self.empty = True
        self.full = False

    def enqueue(self, item):  # zlozonosc O(1)
        if self.full:
            raise Exception('kolejka pelna')
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
            raise Exception('kolejka pusta')
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

    def first(self):
        return self.items[self.head]


print('FIFO tablica cykliczna')
fifo_tabc = Queue(5)
fifo_tabc.enqueue(1)
fifo_tabc.enqueue(2)
fifo_tabc.enqueue(3)
fifo_tabc.enqueue(4)
print(fifo_tabc.items)
fifo_tabc.dequeue()
print('first:', fifo_tabc.first())
fifo_tabc.enqueue(5)
print(fifo_tabc.items)
fifo_tabc.enqueue(6)
print(fifo_tabc.items)
#fifo_tabc.enqueue(7)  # kolejka pelna
fifo_tabc.dequeue()
fifo_tabc.enqueue(7)
print(fifo_tabc.items, 'first:', fifo_tabc.first())
print('~~~~~~')


# 8. Pokaż, jak zaimplementować kolejkę FIFO, używając dwóch stosów. Napisz stosowną klasę.
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

print('FIFO dwa stosy')
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

print('~~~~~~')

# 9. Kolejka dwustronna
# Napisz cztery procedury działające w czasie O(1), służące do wstawiania
# i usuwania elementów z obu końców kolejki przechowywanej:

# (b) liście dowiązanej
print('(b) Lista dowiazana')
# Funkcje kolejki dwustronnej zostaly juz zrealizowane w klasie DoublyLinkedList
# (add_end, add_start, del_last, del_first) z zadania 3 w tym pliku

queue_dll = DoublyLinkedList()
queue_dll.add_end(1)
queue_dll.add_start(2)
queue_dll.add_start(3)
queue_dll.add_end(4)

queue_dll.del_first()
queue_dll.del_last()
print('kolejka', queue_dll.show_all())