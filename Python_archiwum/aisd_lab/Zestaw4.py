# zad. 1 A)
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


"""jakis_stack = Stack()
print(jakis_stack.is_empty())
jakis_stack.push(12)
jakis_stack.push(1)
jakis_stack.push(6)
jakis_stack.push(2)
print(jakis_stack.is_empty())
print(jakis_stack.peak())
jakis_stack.pop()
print(jakis_stack.size())
print(jakis_stack.peak())
print(jakis_stack)

print('*'*10)"""


# zad. 1 B)
class Stack2:
    """Nowe elementy sa zapisywane na poczatku listy,
    wszystkie elementy sa wowczas przesuwane ze swojej pozycji,
    zlozonosc O(n)"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if self.is_empty() is False:
            del self.items[0]
        else:
            print('Pusty stos')

    def peak(self):
        if self.is_empty() is False:
            return self.items[0]
        else:
            print('Pusty stos')

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


"""jakis_stack2 = Stack2()
print(jakis_stack2.is_empty())
jakis_stack2.push(12)
jakis_stack2.push(1)
jakis_stack2.push(6)
jakis_stack2.push(2)
print(jakis_stack2.is_empty())
print(jakis_stack2.peak())
jakis_stack2.pop()
print(jakis_stack2.size())
print(jakis_stack2.peak())
print(jakis_stack2)"""


# zad. 2
def sprawdz_nawiasy(string):
    """Zwraca prawde dla prawidlowo zamknietych nawiasow,
    falsz dla blednie zamknietych nawiasow"""
    stos_naw = Stack()

    for nawias in string:
        if nawias == '(':
            stos_naw.push(nawias)
            # print('dodaje (')
        elif nawias == ')':
            if stos_naw.is_empty() is False:
                stos_naw.pop()
                # print('odejmuje )')
            else:
                stos_naw.push(')')
                break

    print('stan wyjsciowy stosu:', stos_naw)
    if stos_naw.is_empty():
        return True
    else:
        return False


#print(sprawdz_nawiasy('(()()())'))  # True
#print(sprawdz_nawiasy('((()('))  # False


# zad. 3
def get_key(my_dict, val):
    """Funkcja pomocnicza dla sprawdz_nawiasy_dict"""
    for key, value in my_dict.items():
        if val == value:
            return key


def sprawdz_nawiasy_dict(string):
    """Sprawdza poprawnosc uzytych nawiasow typu (, [, <, {"""
    slownik = {'(': ')', '[': ']', '{': '}', '<': '>'}
    stos = Stack()

    for nawias in string:
        if nawias in slownik.keys():
            # print('dodaje:', nawias)
            stos.push(nawias)
        elif nawias in slownik.values():
            if stos.is_empty() is False:
                if stos.peak() == get_key(slownik, nawias):
                    # print('odejmuje:', stos.peak())
                    stos.pop()
            elif stos.is_empty() is True:
                # print('dodaje blad:', nawias)
                stos.push(nawias)
                break

    # print('stan wyjsciowy stosu:', stos)
    if stos.is_empty():
        return True
    else:
        return False


#print(sprawdz_nawiasy_dict('[()()()]'))  # True
#print(sprawdz_nawiasy_dict('(()('))  # False
#print(sprawdz_nawiasy_dict('([)]'))  # False
#print(sprawdz_nawiasy_dict('()[]<>{}'))  # True
#print(sprawdz_nawiasy_dict('([(){}])'))  # True
#print(sprawdz_nawiasy_dict('([(){}]>'))  # False
#print(sprawdz_nawiasy_dict('([{<>}])'))  # True


# zad. 4
def wskaz_blad(string):
    """Wskazuje gdzie zostal popelniony blad w nawiasach"""
    slownik = {'(': ')', '[': ']', '{': '}', '<': '>'}
    stos = Stack()

    indeks_bledu = 0

    for nawias in string:
        if nawias in slownik.keys():
            stos.push(nawias)
        elif nawias in slownik.values():
            if stos.is_empty() is False:
                if stos.peak() == get_key(slownik, nawias):
                    stos.pop()
            elif stos.is_empty() is True:
                stos.push(nawias)
                indeks_bledu += 1
                break
        indeks_bledu += 1

    if stos.is_empty():
        return True
    else:
        print('blad na pozycji', indeks_bledu)
        return False


#print(wskaz_blad('((()'))


# zad. 5
def infix_postfix(wyrazenie_infix):
    """Konwertuje wyrazenie infiksowe na postinfiksowe"""
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


#wyrazenie1 = '( 2 + 3 ) * 5'
#print(infix_postfix(wyrazenie1))


# zad. 6
def operacja(operator, op1, op2):
    """Funkcja pomocnicza dla oblicz_postfix"""
    if operator == "+":
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == "*":
        return op1 * op2
    elif operator == "/":
        return op1 / op2


def oblicz_postfix(wyrazenie_postfix):
    """Oblicza wartosc wyrazenia postfiksowego"""
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


def check_convert_calculate(wyrazenie):
    """Sprawdza poprawnosc nawiasow w wyrazeniu infiksowym,
    nastepnie konwertuje na postfiksowe i zwraca jego wartosc
    """
    if sprawdz_nawiasy_dict(wyrazenie):
        if infix_postfix(wyrazenie):
            return oblicz_postfix(infix_postfix(wyrazenie))
        else:
            print('Błąd przy zamianie na postfix')
    else:
        print('Błąd w nawiasach')


#wyr1 = '( 20 + 3 ) * 4'
#print(check_convert_calculate(wyr1))


# zad. 7
def konwerter_stos(liczba, system):
    """Konwerter liczb decymalnych
    na system binarny, ósemkowy lub heksadecymalny
    """
    assert isinstance(liczba, int)
    stos = Stack()

    if system == 2:
        while liczba > 0:
            stos.push(liczba % 2)
            liczba = liczba // 2

    if system == 8:
        while liczba > 0:
            stos.push(liczba % 8)
            liczba = liczba // 8

    if system == 16:
        while liczba != 0:
            reszta = liczba % 16
            if reszta < 10:
                stos.push(reszta)
            else:
                wieksze_od_9 = chr(reszta + 55)
                stos.push(wieksze_od_9)
            liczba = liczba // 16

    wynik = ""
    while stos.is_empty() is False:
        wynik += str(stos.peak())
        stos.pop()

    return wynik


#print(konwerter_stos(111, 2))
#print(konwerter_stos(111, 8))
#print(konwerter_stos(111, 16))
