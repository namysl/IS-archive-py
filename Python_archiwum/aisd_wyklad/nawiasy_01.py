# -*- coding: utf-8 -*-
# Przykład zastosowania struktury stosów do sprawdzenia poprawności prostego wyrażenia nawiasowego (nawiasy "()")
# materialy do wykladu AiSD, Michal Baczynski

import stos_tablica
# importuje plik z naszą klasa, gdzie jest zaimplementowany stos, np za pomoca tablicy

stos = stos_tablica.Stack_01
# dla ulatienia odwołania się do naszego stosu tworzymy alias

def nawiasy_spr(napis):
    """Program sprawdzajacy poprawnosc prostego wyrazenia nawiasowego zlozonego z '()'"""
    n = len(napis)
    s = stos()
    balanced = True
    i = 0
    while i < n and balanced:
        symbol = napis[i]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        i = i + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

# poniżej przykładowe wywołania

print(nawiasy_spr('((()))'))
print(nawiasy_spr('(()'))
print(nawiasy_spr(')()'))
