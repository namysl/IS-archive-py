# zestaw7
#1

class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.previous = None

class LList:
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

    def show(self):
        if self.isEmpty():
            return Exception('pusta')
        pass

    def add_first(self, item):
        new = Node(item)
        if self.isEmpty():
            self.tail = new
            self.head = self.tail
        else:
            self.head.previous = new
            new.next = self.head
            self.head = new
        self._size += 1

    def add_first222(self, item):
        new = Node(item, self.head)  #??
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.head = new
        self.size += 1

    def add_end(self, item):
        tail = self.tail
        self.tail = Node(item)
        if self.isEmpty():
            self.head = self.tail
        else:
            tail.next = self.tail
            self.tail.previous = tail
        self._size += 1

    def del_first(self):
        if self.isEmpty():
            raise ValueError("Lista")
        item = self.head.item
        self.head = self.head.next
        self._size -= 1
        if self.isEmpty():
            self.tail = None
        return item

    def del_end(self):  # JEST OK TERAZ NAWET DLA 1 ELEMENTU
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

    def __add__(self, a):
        """Dodaje dwie listy"""

        result = LList()
        while not self.isEmpty() and not a.isEmpty():
            first = self.del_first()
            second = a.del_first()
            suma = first + second

            if suma >= 10:
                suma = suma % 10
                result.add_end(suma)
            else:
                result.add_end(suma)

        return result


LL = LList()
LL.add_first(3)
LL.add_first(4)
LL.add_first(2)
LL.lprint()
print('\n')

inna = LList()
inna.add_first(4)
inna.add_first(6)
inna.add_first(5)
inna.lprint()
print('\n')

(LL + inna).lprint()
