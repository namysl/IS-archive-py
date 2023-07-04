class Stack:
    """Nowe elementy sa dopisywane na koncu listy,
    elementy juz istniejace w stosie pozostaja na swoim miejscu,
    zlozonosc O(1)
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Zwraca informacje czy stos jest pusty"""
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        """Umieszcza element na szczycie stosu"""
        self.items.append(item)

    def pop(self):
        """Usuwa element ze szczytu stosu"""
        if self.is_empty() is False:
            self.items.pop()
        else:
            print('Pusty stos')

    def peak(self):
        """Zwraca element, ktory jest na szczycie stosu"""
        if self.is_empty() is False:
            return self.items[-1]
        else:
            print('Pusty stos')

    def size(self):
        """Zwraca rozmiar stosu"""
        return len(self.items)

    def __str__(self):
        return str(self.items)


class DwaStosy:
    def __init__(self):
        self.stack_int = Stack()
        self.stack_pusty = Stack()

    def push(self, item):
        self.stack_int.push(item)

    def usun_najmniejszy(self):
        """Usuwa najglebiej polozony element o najmniejszej wartosci,
        zwraca stack_int bez w/w elementu"""
        minimum = self.stack_int.peak()

        while not self.stack_int.is_empty():
            if minimum >= self.stack_int.peak():
                minimum = self.stack_int.peak()
                self.stack_pusty.push(self.stack_int.peak())
                self.stack_int.pop()
            elif minimum < self.stack_int.peak():
                self.stack_pusty.push(self.stack_int.peak())
                self.stack_int.pop()

        while not self.stack_pusty.is_empty():
            if minimum == self.stack_pusty.peak():
                self.stack_pusty.pop()
                minimum = None
            else:
                self.stack_int.push(self.stack_pusty.peak())
                self.stack_pusty.pop()

        return self.stack_int.items  #, self.stack_pusty.items, minimum


jakis_stack = DwaStosy()
jakis_stack.push(1)  # najglebiej ukryty minimalny element
jakis_stack.push(12)
jakis_stack.push(1)
jakis_stack.push(6)
jakis_stack.push(2)
jakis_stack.push(1)

print(jakis_stack.stack_int.items)
print(jakis_stack.usun_najmniejszy())