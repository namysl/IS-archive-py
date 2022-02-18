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


# zad. 1
def operacja(operator, op1, op2):
    """Funkcja pomocnicza dla Postfix_Eval oraz Infix_nawiasy_Eval"""
    if operator == "+":
        return op1 + op2
    elif operator == '-':
        return op1 - op2
    elif operator == "*":
        return op1 * op2
    elif operator == "/":
        return op1 / op2


def PostfixEval(wyrazenie_postfix):
    """Oblicza wartosc wyrazenia postfiksowego korzystajac ze stosu"""
    wyrazenie_postfix = wyrazenie_postfix.split()
    stos = Stack()
    print(wyrazenie_postfix)
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


wyr1 = '20 10 + 75 45 - *'  # wynik = 900
#print(PostfixEval(wyr1))


# zad. 2
def InfixToPostfix(wyrazenie_infix):
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


wyr2 = '( 20 + 10 ) * ( 75 - 45 )'
#print(InfixToPostfix(wyr2))


# zad. 3
def PostfixToInfix(wyrazenie_postfix):
    """Konwertuje wyrazenie postfiksowe na infiksowe"""
    wyrazenie_postfix = wyrazenie_postfix.split()
    lista = []
    stos = Stack()

    for el in wyrazenie_postfix:
        if el.isalnum():
            stos.push(el)
        elif el in '+-*/':
            oper2 = stos.peak()
            stos.pop()
            # print('oper2:', oper2)
            oper1 = stos.peak()
            stos.pop()
            # print('oper1:', oper1)
            wynik = ('(' + oper1 + el + oper2 + ')')
            # print('wynik:', wynik)
            stos.push(wynik)

    while not stos.is_empty():
        lista += stos.peak()
        stos.pop()

    string_postfix = ''
    for el in lista:
        string_postfix += el
        string_postfix += ' '
    return string_postfix


#print(PostfixToInfix('20 10 + 75 45 - *'))  # ((20 + 10) * (75 - 45))


# zad. 4
def Infix_nawiasy_Eval(wyrazenie_infix):
    """Oblicza wartosc wyrazenia infiksowego na stosie,
    na stos_operatory umieszcza operatory oraz nawias otwierajacy"""

    wyrazenie_infix = wyrazenie_infix.split()
    stos = Stack()
    stos_operatory = Stack()

    for el in wyrazenie_infix:
        if el.isalnum():
            stos.push(el)

        elif el == '(':
            stos_operatory.push(el)

        elif el in '+-*/':
            stos_operatory.push(el)

        elif el == ')':
            while stos_operatory.peak() == '(':
                #print('pętla while, pop:', stos_operatory.peak())
                stos_operatory.pop()

            oper2 = int(stos.peak())
            stos.pop()
            #print('OPER2:', oper2)

            oper1 = stos.peak()
            stos.pop()
            #print('OPER1:', oper1)

            operator = stos_operatory.peak()
            stos_operatory.pop()
            #print('OPERATOR:', operator)

            wynik = operacja(operator, int(oper1), int(oper2))
            #print('wynik:', wynik)
            stos.push(wynik)

    while not stos_operatory.is_empty():
        if stos_operatory.peak() == '(':
            stos_operatory.pop()
        else:
            operator = stos_operatory.peak()
            stos_operatory.pop()

            op2 = stos.peak()
            stos.pop()
            op1 = stos.peak()
            stos.pop()

            wynik = operacja(operator, op1, op2)
            stos.push(wynik)

    return stos.peak()


print(Infix_nawiasy_Eval('( 11 + ( ( 22 + 3 ) * ( 44 - 52 ) ) ) '))  # wynik = 189
#print(Infix_nawiasy_Eval('( ( 2 + 2 ) * ( 4 ) * ( 9 + 1 ) )'))  # wynik = 160
#print(Infix_nawiasy_Eval('( ( 1 * 2 ) + ( 3 * 2 ) - 1 )'))  # wynik = 7
