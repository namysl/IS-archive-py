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

    def show(self):
        return str(self.items)


def get_key(my_dict, val):
    """Funkcja pomocnicza dla sprawdz_nawiasy_dict"""
    for key, value in my_dict.items():
        if val == value:
            return key


def sprawdz_nawiasy_dict(string):
    slownik = {'(': ')', '[': ']', '{': '}', '<': '>'}
    stos = Stack()

    for nawias in string:
        if nawias in slownik.keys():
            stos.push(nawias)
        elif nawias in slownik.values():
            if stos.is_empty() is False:
                if stos.peak() == get_key(slownik, nawias):
                    stos.pop()
            elif stos.is_empty() is True:
                stos.push(nawias)
                break

    if stos.is_empty():
        return True
    else:
        return False


def infix_postfix(wyrazenie_infix):
    wyrazenie_infix = wyrazenie_infix.split()
    lista = []
    stos = Stack()

    for el in wyrazenie_infix:
        if el.isdigit():
            lista.append(el)
        elif el == '(':
            stos.push(el)
        elif el == ')':
            while stos.peak() != '(':
                lista.append(stos.peak())
                stos.pop()
            if stos.peak() == '(':
                stos.pop()
        elif el in '+-*/':
            stos.push(el)

    while not stos.is_empty():
        lista += stos.peak()
        stos.pop()

    string_postfix = ''
    for el in lista:
        string_postfix += el
        string_postfix += ' '
    return string_postfix


def operacja(operator, op1, op2):
    if operator == "+":
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == "*":
        return op1 * op2
    elif operator == "/":
        return op1 / op2


def oblicz_postfix2(wyrazenie_postfix):
    wyrazenie_postfix = wyrazenie_postfix.split()
    stos = Stack()

    for el in wyrazenie_postfix:
        if el.isdigit():
            stos.push(int(el))
        elif el in '+-*/':
            op2 = stos.peak()
            stos.pop()
            op1 = stos.peak()
            stos.pop()
            wynik = operacja(el, op1, op2)
            stos.push(wynik)

    return stos.peak()


def wynik_wyrazenia(wyrazenie):
    if sprawdz_nawiasy_dict(wyrazenie):
        if infix_postfix(wyrazenie):
            return oblicz_postfix2(infix_postfix(wyrazenie))
        else:
            print('Błąd przy zamianie na postfix')
    else:
        print('Błąd w nawiasach')


wyr1 = '( 20 + 3 ) * 4'
print(wynik_wyrazenia(wyr1))
