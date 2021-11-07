# coding: utf-8
# Prosta implementacja kolejki FIFO jako Abstrakcyjnej Struktury Danych (ADT-Abstract Data Type)
# kolejka oparta jest na liscie w jezyku Python (druga wersja).
# Ta implementacja tez nie jest optymalna, gdyz operacja enqueue() ma zlozonosc liniowa
# PROSZE TEGO NIGDY NIE STOSOWAC!!!
# materialy do wykladu AiSD, Michal Baczynski

class Queue:
    def __init__(self):				# zlozonosc O(1)
        self._QList = []
    def size(self):					# zlozonosc O(1)
        return len(self._QList)
    def isEmpty(self):				# zlozonosc O(1)
        return self._QList == []
    def enqueue(self, item):			# zlozonosc O(1)
        self._QList.append(item)
    def dequeue(self):					# zlozonosc O(n), gdzie n oznacza liczbe elementow w kolejce
        assert not self.isEmpty(), "operacja dequeue - kolejka jest pusta!!!"
        self._QList.pop(0)
    def first(self):					# zlozonosc O(1)
        return self._QList[0]

print("Kolejka FIFO - druga implementacja oparta na liscie Python (ale prosze jej nigdy nie stosowac!!!)")
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
