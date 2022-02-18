# coding: utf-8
# Prosta implementacja kolejki FIFO jako Abstrakcyjnej Struktury Danych (ADT-Abstract Data Type)
# kolejka oparta jest na liscie w jezyku Python (pierwsza wersja).
# Ta implementacja nie jest optymalna, gdyz operacja enqueue() ma zlozonosc liniowa
# PROSZE TEGO NIGDY NIE STOSOWAC!!!
# materialy do wykladu AiSD, Michal Baczynski

class Queue:
    def __init__(self):				# zlozonosc O(1)
        self._QList = []
    def size(self):					# zlozonosc O(1)
        return len(self._QList)
    def isEmpty(self):				# zlozonosc O(1)
        return self._QList == []
    def enqueue(self, item):			# zlozonosc O(n), gdzie n oznacza liczbe elementow w kolejce
        self._QList.insert(0,item)
    def dequeue(self):					# zlozonosc O(1)
        assert not self.isEmpty(), "operacja dequeue - kolejka jest pusta!!!"
        self._QList.pop()
    def first(self):					# zlozonosc O(1)
        assert not self.isEmpty(), "operacja first - kolejka jest pusta!!!"
        return self._QList[len(self._QList)-1]

print("Kolejka FIFO - pierwsza implementacja oparta na liscie Python (ale prosze jej nigdy nie stosowac!!!)")
a=Queue()
a.enqueue("a")
a.enqueue("b")
a.enqueue("c")
a.enqueue("d")
print(a.first())
print(a.first())
a.dequeue()
print(a.first())
a.dequeue()
a.enqueue("e")
print(a.first())
a.dequeue()
print(a.first())

#Program powinien wypisac
# a a b c d
