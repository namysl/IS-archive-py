# coding: utf-8
# Prosta implementacja stosu jako Abstrakcyjnej Struktury Danych (ADT-Abstract Data Type)
# stos zaimplementowany jako lista dowiazana (linked list)
# materialy do wykladu AiSD, Michal Baczynski

class _StackNode:
    """prywatna klasa wezel"""
    def __init__(self, item):
        self.dane = item
        self.next = None


class Stack:
    """Implementacja stosu za pomoca listy dowiazanej z wykorzystaniem klasy wezel"""
    def __init__(self):
        """iicjalizacja"""
        self._head = None
        self._size = 0

    def isEmpty(self):
        """sprawdzenie czy stos jest pusty"""
        return self._size == 0
        # lub
        # return self.head is None

    def size(self):
        """zwraca rozmiar stosu"""
        return self._size

    def push(self, element):
        """wlozenie elementu na stos"""
        nowy = _StackNode(element)      # tworzymy nowy wezel
        nowy.next = self._head          # podwiazujemy pod niego aktualna glowe (czyli nasz stos)
        self._head = nowy               # glowa staje sie ten nowy wezel
        self._size += 1                 # zwiekszamy rozmiar stosu
        return

    def pop(self):
        """sciagniecie elementu ze stosu"""
        if self.isEmpty():
            print("operacja pop - Stos jest pusty!!!")
            return False              # ewentualnie wywolaj wyjatek np. assert
            # assert not self.isEmpty(), "Stos jest PUSTY!!!"
        self._head = self._head.next    # glowa staje sie nastepny wezel po aktualnej glowei
                                        # w niektorych jezykach programowania trzeba samodzielnie zwolnic pamiec, np. w C++ operacja delete
        self._size -= 1                 # zmniejszamy rozmiar stosu
        return

    def top(self):
        """zwrocenie eleemntu ze szczytu stosu"""
        if self.isEmpty():
            print("operacja top - Stos jest pusty!!!")
            return False                # ewentualnie wywolaj wyjatek
        return self._head.dane          # zwracamy konkretna dane z naszej glowy


def do_math(operacja, op1, op2=None):
    """funkcja oblicza wartosc wyrazenia zapisanego w postaci: op1 operacja op2 """
    if operacja == "*":
        return op1 * op2
    elif operacja == "/":
        return op1 / op2
    elif operacja == "+":
        return op1 + op2
    elif operacja == "-":
        return op1 - op2
    elif operacja == "k":
        return op1 ** 2


def postfix_eval2(postfix_wyrazenie):
    stos_operatorow = Stack()
    licznik = 1
    i = 0
    while i < len(postfix_wyrazenie):
        print('*****')
        print('KTÓRA ITERACJA?', licznik)
        element = postfix_wyrazenie[i]
        if element.isdigit():
            element_next = postfix_wyrazenie[i+1]
            print('0')
            if element_next.isspace():
                print('1')
                print('element:', element)
                stos_operatorow.push(int(element))
            elif element.isdigit() and element_next.isdigit():
                print('2')
                temp = int(element) * 10 + int(element_next)
                print('temp:', temp)
                stos_operatorow.push(int(temp))
                i += 1
        elif element in "+-*/":
            print('3')
            operand2 = stos_operatorow.top()
            stos_operatorow.pop()
            operand1 = stos_operatorow.top()
            stos_operatorow.pop()
            wynik = do_math(element, operand1, operand2)
            print('wynik:', wynik)
            stos_operatorow.push(wynik)
        elif element == "k":
            print('4')
            operand1 = stos_operatorow.top()
            stos_operatorow.pop()
            wynik = do_math(element, operand1)
            print('wynik k:', wynik)
            stos_operatorow.push(wynik)
        licznik += 1
        i += 1
    return stos_operatorow.top(), stos_operatorow.size()


# poniżej przykładowe wywołania
print(postfix_eval2("7 8 + 3 2 + /"))  # wynik to 3
print(postfix_eval2("6 4 - 3 2 + *"))  # wynik to 10
print(postfix_eval2("2 4 6 - k *"))  # wynik = 8
print(postfix_eval2("12 4 6 - k *"))  # 12*(4-6)^2 = 48
print(postfix_eval2("6 2 + 5 k /"))   # 6+2 / 5^2 = 0.32
print(postfix_eval2("10 k 10 k +"))   # 10^2 + 10^2 = 200