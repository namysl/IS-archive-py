import math


class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None


class LinkedList2:
    """show_all() -> zlozonosc O(n)
    add_end()  -> zlozonosc O(1)"""
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

    def sortuj(self):
        """Sortowanie babelkowe elementow w liscie dowiazanej"""
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

    def srednia(self):
        """Oblicza srednia elementow w liscie dowiazanej"""
        suma = 0

        current = self.head
        next_link = current.next

        while next_link is not None:
            suma += current.item
            # print('tutaj', current.item)
            current = current.next
            next_link = next_link.next

        suma += current.item
        # print('tutaj2', current.item)

        suma = suma / self.size()
        return suma

    def mediana(self):
        """Oblicza medianę elementów posortowanej listy dowiązanej"""
        self.sortuj()
        #print(self.show_all())

        if self.size() % 2 == 1:
            srodek_iter = 1

            current = self.head
            next_link = current.next
            while next_link is not None and srodek_iter != math.ceil(self.size()/2):
                #print('tutaj', current.item)
                srodek_iter += 1
                current = current.next
                next_link = next_link.next
            return current.item

        if self.size() % 2 == 0:
            srodek_iter = 1

            current = self.head
            next_link = current.next
            while next_link is not None and srodek_iter != self.size()/2:
                #print('tutaj', current.item)
                srodek_iter += 1
                current = current.next
                next_link = next_link.next
            mediana = (current.item + current.next.item) / 2

            return mediana


lista1 = LinkedList2()
lista1.add_end(3)
lista1.add_end(4)
lista1.add_end(1)
lista1.add_end(2)
print(lista1.show_all())
print('srednia:', lista1.srednia())
print('mediana:', lista1.mediana())

print('~~~~')

lista2 = LinkedList2()
lista2.add_end(3)
lista2.add_end(4)
lista2.add_end(5)
lista2.add_end(1)
lista2.add_end(2)
print(lista2.show_all())
print('srednia:', lista2.srednia())
print('mediana:', lista2.mediana())
