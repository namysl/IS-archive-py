# -*- coding: utf-8 -*-
# Przykładowy program obliczający wartość wyrażenia (tylko cyfry) zapisanego w postacji postfiksowej
# materialy do wykladu AiSD, Michal Baczynski

import stack_linked_list
#importujemy plik z nasza klasa stos oparta np. na liscie dowiazanej

Stos = stack_linked_list.Stack
# dla ułatienia odwolania się do naszego stosu tworzymy alias

def do_math(operacja, op1, op2):
    """funkcja oblicza wartosc wyrazenia zapisanego w postaci: op1 operacja op2 """
    if operacja == "*":
        return op1 * op2
    elif operacja == "/":
        return op1 / op2
    elif operacja == "+":
        return op1 + op2
    else:
        return op1 - op2

def postfix_eval(postfix_wyrazenie):
    """postfix_wyrazanie jest typu string i zawiera wyrazenie w postaci postiksowej - nie sprawdzamy poprawnosci wyrazenia !!!"""
    stos_operatorow = Stos()                      
    #dekalrujemy nasz stos operatorow
    for element in postfix_wyrazenie:               # przegladam kolejno dane wyrazenie, zatem zlozonosc wynosi O(n), gdzie n jest dlugoscia wyrazenia
        if (element >="0") and (element <="9"):     # co robimy jak trafimy na cyfre
            stos_operatorow.push(int(element))
        elif (element in "+-*/"):                   # co robimy jak trafimy na klasyczna operacje artymetyczna
            operand2 = stos_operatorow.top()    
            stos_operatorow.pop()
            operand1 = stos_operatorow.top()
            stos_operatorow.pop()
            wynik = do_math(element, operand1, operand2)    # zwroc uwage na kolejnosc
            stos_operatorow.push(wynik)
    return stos_operatorow.top()

# poniżej przykładowe wywołania

print(postfix_eval("7 8 + 3 2 + /"))        # wynik to 3
print(postfix_eval("6 4 - 3 2 + *"))        # wynik to 10

