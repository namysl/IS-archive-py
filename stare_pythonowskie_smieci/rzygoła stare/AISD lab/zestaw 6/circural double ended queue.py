class Queue3:
    def __init__(self, n):  # zlozonosc O(n)
        self.items = n * [None]
        self.size = n
        self.head = 0
        self.tail = 0
        self.empty = True
        self.full = False

    def add_end(self, item):  # zlozonosc O(1)
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

    def add_start(self, item):
        if self.full:
            raise Exception('pelna')
        else:
            self.items[self.head] = item
            self.empty = False

        if self.head == self.size - 1:
            self.head = 0
        else:
            self.head += 1

        if self.head == self.tail:
            self.full = True

    def del_first(self):  # zlozonosc O(1)
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

    def del_last(self):
        if self.empty:
            raise Exception('kolejka pusta')
        else:
            x = self.items[self.tail]
            self.full = False

        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail += 1

        if self.head == self.tail:
            self.empty = True
        return x

fifo_tabc = Queue3(5)
fifo_tabc.add_start(1)
fifo_tabc.add_end(3)
print(fifo_tabc.items)