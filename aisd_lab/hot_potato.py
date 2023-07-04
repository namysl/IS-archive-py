class Kolejka:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        """O(n)"""
        self.items.insert(0, item)

    def dequeue(self):
        """O(1)"""
        if self.is_empty() is False:
            self.items.pop()
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


przyklad = Kolejka()
przyklad.enqueue(1)
przyklad.enqueue(2)
przyklad.enqueue(3)
print(przyklad)
przyklad.dequeue()
print(przyklad)


lista = ['a', 'b', 'c', 'd', 'e', 'f']


def goracy_ziemniak(lista_uczestnikow, liczba_przekazan):
    kol = Kolejka()
    for osoba in lista_uczestnikow:
        kol.enqueue(osoba)

    while kol.size() != 1:
        while liczba_przekazan != 0:
            kol.enqueue(kol.peak())
            kol.dequeue()
            liczba_przekazan -= 1
        kol.dequeue()
    print(kol)
    return kol.peak()


print(goracy_ziemniak(lista, 6))
