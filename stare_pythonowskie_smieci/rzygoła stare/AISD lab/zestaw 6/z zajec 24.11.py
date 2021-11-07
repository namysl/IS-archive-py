#1 O(n)
class Node():
    def __init__(self, item=None):
        self.item = item
        self.next = None


class LList_oned():  # liniowa zlozonosc
    def __init__(self):
        self.head = None
        self._size = 0

    # self.tail=None

    def isEmpty(self):
        return self._size == 0

    def lprint(self):
        current = self.head
        while current is not None:
            print(current.item)
            current = current.next

    def add_end(self, item):
        NewNode = Node(item)
        if self.isEmpty():
            self.head = NewNode

        else:
            current = self.head

            while current.next is not None:
                current = current.next
            current.next = NewNode
        self._size += 1

    def pop(self):
        x = self.head.item
        if self.isEmpty():
            raise ValueError("Lista jest pusta")
        self.head = self.head.next  # aktualny do następnego
        self._size -= 1
        return x

    def size(self):
        return self._size

"""print('ld1:')
ld1 = LList_oned()
ld1.add_end(3)
ld1.add_end(2)
ld1.add_end(1)

print('print1:')
ld1.lprint()

print('pop:')
print(ld1.pop())
print(ld1.pop())

print('print2:')
ld1.lprint()

print('~~~~~')"""


# O(1) - dodefiniować ogon, wtedy niepotrzebny while
# inkrementacja tylko żeby zwiekszyc rozmiar
class LList_oned2():  # liniowa zlozonosc
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def lprint(self):
        current = self.head
        while current is not None:
            print(current.item)
            current = current.next

    def add_end(self, item):  # O(1) dodawanie elementu na koniec
        tail = self.tail
        self.tail = Node(item)

        if self.isEmpty():
            self.head = self.tail
        else:
            tail.next = self.tail
        self._size += 1

    def pop(self): # usuwa ostatni?
        x = self.tail.item

        if self.isEmpty():
            raise ValueError("Lista jest pusta")

        self.tail = self.tail.next  # aktualny do następnego
        self._size -= 1
        return x

    def size(self):
        return self._size

"""print('ld2:')
ld2 = LList_oned2()
ld2.add_end(3)
ld2.add_end(2)
ld2.add_end(1)
ld2.add_end(0)
ld2.add_end(-1)

ld2.lprint()
print('size', ld2.size())

print('~~~~~')

#print(ld2.pop())
print('tail.next', ld2.tail.next)

print('size', ld2.size())
ld2.lprint()"""


#3
class Node2():
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.previous = None


class LList_oned3():  # liniowa zlozonosc
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def lprint(self):
        current = self.head
        while current is not None:
            print(current.item)
            current = current.next

    def insert(self, item):
        tail = self.tail
        self.tail = Node2(item)
        if self.isEmpty():
            self.head = self.tail
        else:
            tail.next = self.tail
            #self.tail = tail.previous
            self.tail.previous = tail
        self._size += 1

    def pop_start(self):
        x = self.head.item
        if self.isEmpty():
            raise Exception('pusta')
        self.head = self.head.next
        self._size -= 1
        return x

    def pop_end(self):  # JEST OK TERAZ NAWET DLA 1 ELEMENTU
        if self.isEmpty():
            raise Exception('pusta')

        x = self.tail.item
        self._size -= 1

        if self.isEmpty():
            self.tail = Node()
            self.head = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None

        return x

    def size(self):
        return self._size


l3 = LList_oned3()
l3.insert(1)
l3.insert(2)
l3.insert(3)
print('!')
l3.lprint()

l3.pop_end()
l3.pop_end()
l3.pop_end()

print('\n!')
l3.lprint()


# 5. stos:

class Node():
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.previous = None


class STACK_LList():
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def lprint(self):
        current = self.head
        while current is not None:
            print(current.item)
            current = current.next

    def push(self, item):
        tail = self.tail
        self.tail = Node2(item)
        if self.isEmpty():
            self.head = self.tail
        else:
            tail.next = self.tail
            self.tail.previous = tail
        self._size += 1

    def pop(self):
        x = self.head.item
        if self.isEmpty():
            raise Exception('pusta')
        self.head = self.head.next
        self._size -= 1
        return x

# 8 Pokaż, jak zaimplementować kolejkę FIFO, używając dwóch stosów.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty() is False:
            return self.items.pop()
        else:
            print('Pusty stos')

    def peak(self):
        if self.is_empty() is False:
            return self.items[-1]
        else:
            print('Pusty stos')

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

class FIFO():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def isEmpty(self):
        if self.stack1.is_empty() and self.stack2.is_empty():
            return True

    def push(self, item):
        self.stack1.push(item)

    def pop(self):
        if self.stack1.is_empty():
            raise Exception('stack pusty')
        x = self.stack1.pop()
        self.stack2.push(x)
        return x

    def pop2(self): # sprawdzic
        if self.f.isEmpty():
            while not self.s.isEmpty():
                self.f.push(self.s.pop())
        return self.f.pop()

"""fifooo = FIFO()
fifooo.push(3)
fifooo.push(2)
fifooo.push(1)
fifooo.push(0)

print(fifooo.stack1.items)
fifooo.pop()

print('s1', fifooo.stack1.items)
print('s2', fifooo.stack2.items)"""