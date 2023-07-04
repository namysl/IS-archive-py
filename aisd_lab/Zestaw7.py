# zad. 1
class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def show(self):
        if self.is_empty():
            return Exception('pusta lista')

        string = str(self.head.item)
        nastepny = self.head.next
        while nastepny is not None:
            string += ' -> ' + str(nastepny.item)
            nastepny = nastepny.next
        return string

    def add_first(self, item):
        new = Node(item)
        if self.is_empty():
            self.tail = new
            self.head = self.tail
        else:
            self.head.previous = new
            new.next = self.head
            self.head = new
        self._size += 1

    def add_end(self, item):
        tail = self.tail
        self.tail = Node(item)
        if self.is_empty():
            self.head = self.tail
        else:
            tail.next = self.tail
            self.tail.previous = tail
        self._size += 1

    def del_first(self):
        if self.is_empty():
            raise ValueError("Lista")
        val = self.head.item
        self.head = self.head.next
        self._size -= 1
        if self.is_empty():
            self.tail = None
        return val

    def del_end(self):
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

    def size(self):
        return self._size

    def __add__(self, other):
        """Dodaje dwie liczby z dwoch list dowiazanych,
        carry trzyma przeniesienie jedynki w przypadku gdy suma > 9

        Jesli listy maja rozna dlugosc, dodaje brakujaca liczbe zer
        na koniec linked listy"""

        if self.size() < other.size():
            length = other.size() - self.size()
            for _ in range(length):
                self.add_end(0)
        elif self.size() > other.size():
            length = self.size() - other.size()
            for _ in range(length):
                other.add_end(0)

        # print('show self: ', self.show())
        # print('show other:', other.show())

        result = LinkedList()
        carry = 0
        while not self.is_empty() and not other.is_empty():
            first = self.del_first()
            second = other.del_first()
            suma = first + second + carry

            if suma >= 10:
                carry = 1
                suma = suma % 10
                result.add_end(suma)
            else:
                carry = 0
                result.add_end(suma)

        # print('CARRY:', carry)
        if carry != 0:  # jesli w ostatnim dodawaniu wynikiem byla liczba >9
            result.add_end(carry)

        return result


# print('342 + 465 = 807')
# LL = LinkedList()
# LL.add_first(3)
# LL.add_first(4)
# LL.add_first(2)
# print(LL.show())
#
# inna = LinkedList()
# inna.add_first(4)
# inna.add_first(6)
# inna.add_first(5)
# print(inna.show(), '\n')
#
# print((LL + inna).show(), '\n\n')
#
# print('przypadek list o roznej dlugosci:')
# LL2 = LinkedList()
# LL2.add_first(1)
# LL2.add_first(2)
# LL2.add_first(3)
# print(LL2.show())
#
# inna2 = LinkedList()
# inna2.add_first(1)
# inna2.add_first(2)
# inna2.add_first(3)
# inna2.add_first(4)
# inna2.add_first(5)
# inna2.add_first(6)
# print(inna2.show(), '\n')
#
# print((LL2 + inna2).show(), '\n\n')
#
# print('713 + 307 = 1020')
# LL3 = LinkedList()
# LL3.add_first(3)
# LL3.add_first(1)
# LL3.add_first(7)
# print(LL3.show())
#
# inna3 = LinkedList()
# inna3.add_first(7)
# inna3.add_first(0)
# inna3.add_first(3)
# print(inna3.show(), '\n')
#
# print((LL3 + inna3).show(), '\n\n')


# zad. 2
class StackMin:
    def __init__(self):
        self.stos = []
        self.minimum = []

    def push(self, x):
        self.stos.append(x)

        if len(self.minimum) == 0:
            # jesli lista minimum jest pusta, dodaje do niej element
            self.minimum.append(x)
        else:
            # jesli x jest mniejsze od ostatniego elementu listy minimum, dodaje go na koniec
            if x < self.minimum[-1]:
                self.minimum.append(x)

    def pop(self):
        if len(self.stos) != 0:
            if self.top() == self.minimum[-1]:
                # jesli szczyt znajduje sie w liscie minimum na ostatnim miejscu,
                self.minimum.pop()  # to go usuwa z listy i ze stosu
            self.stos.pop()
        else:
            raise Exception('pusty stos')

    def top(self):
        if len(self.stos) != 0:
            return self.stos[-1]
        else:
            raise Exception('pusty stos')

    def get_min(self):
        return self.minimum[-1]  # zwraca ostatni element listy minimum


# stos1 = StackMin()
#
# stos1.push(18)
# stos1.push(23)
# stos1.push(9)
# stos1.push(0)
# print(stos1.stos)
# print(stos1.get_min())
#
# stos1.pop()  # usuwa 0
# print(stos1.stos)
# print(stos1.get_min())
#
# stos1.push(101)
# stos1.push(13)
# stos1.push(33)
# stos1.push(67)
# stos1.push(1)
# stos1.push(11)
# stos1.pop()
#
# print(stos1.stos)
# print(stos1.get_min())


# zad. 3 + 4
class Node2:
    def __init__(self, item=None):
        self.item = item
        self.next = None


class LinkedList2:
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
        new = Node2(item)
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
        self._size += 1

    def del_first(self):
        val = self.head.item

        if self.is_empty():
            raise Exception('pusta lista')

        self.head = self.head.next
        self._size -= 1

        return val

    def odwroc(self):
        """Odwraca elementy w liscie dowiazanej"""
        previous = None
        current = self.head

        while current is not None:
            nextnode = current.next
            current.next = previous
            previous = current
            current = nextnode
        self.head = previous

    def sortuj(self):
        """Sortowanie przez wstawianie"""
        head = self.head
        current = head

        while current.next is not None:
            if current.item < current.next.item:
                current = current.next
            else:
                nextnode = current.next
                current.next = nextnode.next

                if head.item > nextnode.item:
                    nextnode.next = head
                    self.head = nextnode
                    head = self.head
                else:
                    temphead = head
                    while nextnode.item > temphead.next.item:
                        temphead = temphead.next
                    nextnode.next = temphead.next
                    temphead.next = nextnode


# print('odwroc:')
# link2 = LinkedList2()
# link2.add_end(1)
# link2.add_end(2)
# link2.add_end(4)
# link2.add_end(8)
# link2.add_end(16)
# link2.add_end(32)
#
# print(link2.show_all())
# link2.odwroc()
# print(link2.show_all())
#
# print('sortuj:')
# link3 = LinkedList2()
# link3.add_end(3)
# link3.add_end(1)
# link3.add_end(2)
# link3.add_end(4)
# print(link3.show_all())
#
# link3.sortuj()
# print(link3.show_all())


# zad. 5
"""class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        if self.is_empty():
            raise Exception('kolejka pusta')
        else:
            return len(self.items)

    def peak(self):
        if self.is_empty():
            raise Exception('kolejka pusta')
        else:
            return self.items[-1]


def odkoduj(tekst):
    q_litery = Queue()
    q_liczby = Queue()
    odkodowane = ''

    for znak in tekst:
        if znak.isdigit():
            q_liczby.enqueue(znak)

        elif znak == '[':
            q_litery.enqueue(znak)

        elif znak == ']':
            string = ''
            while not q_litery.is_empty():
                if q_litery.peak() == '[':
                    q_litery.dequeue()
                else:
                    string += q_litery.dequeue()
            liczba = int(q_liczby.dequeue())
            wynik = liczba * string
            odkodowane += wynik

        else:  # litery
            q_litery.enqueue(znak)

    while not q_litery.is_empty():
        odkodowane += q_litery.dequeue()

    return odkodowane#, q_liczby.items, q_litery.items


print(odkoduj('3[a]2[bc]'))  # aaabcbc
print(odkoduj('3[a2[c]]'))  # accaccacc -> ?
print(odkoduj('2[abc]3[cd]ef'))  # abcabccdcdcdef"""


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
        if not self.is_empty():
            self.items.pop()
        else:
            return Exception('pusty stos')

    def peak(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return Exception('pusty stos')

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def odkoduj(tekst):
    liczby = Stack()
    litery = Stack()
    string = ''

    for znak in tekst:
        if znak.isdigit():
            liczby.push(int(znak))

        elif znak == ']':
            temp = ''
            liczba = 0

            if not liczby.is_empty():
                liczba = liczby.peak()
                liczby.pop()

            while not litery.is_empty() and litery.peak() != '[':
                temp = litery.peak() + temp
                litery.pop()

            if not litery.is_empty() and litery.peak() == '[':
                litery.pop()

            for _ in range(liczba):
                string = string + temp
                #print(string)

            for i in range(len(string)):
                litery.push(string[i])
                #print(litery.items)

            string = ''

        elif znak == '[':
            litery.push(znak)

        else:  # litery
            litery.push(znak)

    while not litery.is_empty():
        string = litery.peak() + string
        litery.pop()

    return string


# print(odkoduj('3[a]2[bc]'))
# print(odkoduj('3[a2[c]]'))
# print(odkoduj('2[abc]3[cd]ef'))
