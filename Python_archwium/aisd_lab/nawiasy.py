# Prosta implementacja stosu jako Abstrakcyjnej Struktury Danych (ADT-Abstract Data Type)
# stos zaimplementowany jako tablica (lista w j. Python)
# brak obslugi bledow (np. kiedy stos jest pusty lub braku pamieci na nowy element)
# materialy do wykladu AiSD, Michal Baczynski

class Stack_01:
    """Implementacja stosu za pomoca listy Pythona, czyli klasycznej tablicy"""
    def __init__(self):
        """inicjalizacja"""
        self.items = []

    def isEmpty(self):
        """sprawdzenie czy stos jest pusty"""
        return self.items == []

    def push(self, item):
        """wlozenie elementu na (szczyt) stos"""
        self.items.append(item)
        return

    def pop(self):
        """sciagniecie elementu ze (szczytu) stosu"""
        self.items.pop()
        return

    def top(self):
        """zwrocenie elementu ze (szczytu) stosu"""
        return self.items[len(self.items)-1]

    def size(self):
        """zwrocenie rozmiaru stosu"""
        return len(self.items)


def get_key(my_dict, val):
    """Funkcja pomocnicza dla nawiasy_spr"""
    for key, value in my_dict.items():
        if val == value:
            return key


stos = Stack_01
def nawiasy_spr(napis):
    """Program sprawdzajacy poprawnosc wyrazen z nawiasami (), [], {}, <>
    rozbudowany z programu z wykladu nr 3, sprawdzajacego poprawnosc
    nawiasow jednego rodzaju"""
    n = len(napis)
    s = stos()
    balanced = True
    i = 0
    slownik = {'(': ')', '[': ']', '{': '}', '<': '>'}

    while i < n and balanced:
        symbol = napis[i]
        if symbol in slownik.keys():
            s.push(symbol)
        elif symbol in slownik.values():
            if s.isEmpty():
                balanced = False
            else:
                if s.top() == get_key(slownik, symbol):
                    s.pop()
        i = i + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


# przyklady

print('1:', nawiasy_spr('((()))'))  # True
print('2:', nawiasy_spr('(()'))  # False
print('3:', nawiasy_spr(')()'))  # False
print('4:', nawiasy_spr('[()()()]'))  # True
print('5:', nawiasy_spr('(()('))  # False
print('6:', nawiasy_spr('([)]'))  # False
print('7:', nawiasy_spr('()[]<>{}'))  # True
print('8:', nawiasy_spr('([(){}])'))  # True
print('9:', nawiasy_spr('([(){}]>'))  # False
print('10:', nawiasy_spr('([{<>}])'))  # True
