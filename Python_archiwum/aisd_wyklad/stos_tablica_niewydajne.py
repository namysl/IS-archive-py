# coding: utf-8
# Prosta, ale niewydajna!! implementacja stosu jako Abstrakcyjnej Struktury Danych (ADT-Abstract Data Type)
# stos zaimplementowany jako tablica (lista w j/ Python)
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
        self.items.insert(0,item)
        return
    def pop(self):
        """sciagniecie elementu ze (szczytu) stosu"""
        self.items.pop(0)
        return
    def top(self):
        """zwrocenie elementu ze (szczytu) stosu"""
        return self.items[0]
    def size(self):
        """zwrocenie rozmiaru stosu"""
        return len(self.items)

s=Stack_01()
print("rozmiar", s.size())
s.push(1)
s.push(2)
print("rozmiar", s.size())
print(s.top())
s.pop()
print("rozmiar", s.size())
s.push(3)
print(s.top())
s.pop()
print(s.top())
print("rozmiar", s.size())
