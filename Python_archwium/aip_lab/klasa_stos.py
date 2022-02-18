import collections

class DataStructures(object):
    """
    Obiekt DataStructures opisuje wlasnosci struktur danych.
    
    Struktury danych to sposob przechowywania danych w pamieci komputera.
 
    Parameters
    ----------
    lista: list
        trzyma liste zawierajaca dane
        
    Attributes
    ----------
    lista: tu przechowujemy informacje o parametrze lista

    """
    
    # tworzenie klasy nadrzednej, ktora pomiesci metody wspolne dla stosu i kolejki
    def __init__(self, lista): 
        self.lista = lista[:]

    def __repr__(self):
        return "instancja klasy " + __class__.__name__

    def __str__(self):
        return str(self.lista)

    def check_if_not_empty(self):
        """Sprawdza czy lista danej klasy jest niepusta"""
        if len(self.lista) >= 1: # jesli liczba elementow listy jest wieksza lub rowna 1
            return True # zwraca prawde (lista jest niepusta)
        else: # w innych przypadkach
            return False # zwraca falsz (lista jest pusta)

    def check_len(self):
        """Zwraca dlugosc listy danej klasy"""
        return len(self.lista)
    
    
class Stack(DataStructures):
    """
    Obiekt Stack opisuje wlasnosci stosu.
    
    Stos to abstrakcyjna, liniowa struktura danych, w ktorej wprowadzony
    element umieszczany jest na koncu listy, a usuwany element jest zdejmowany
    z konca listy.
 
    Parameters
    ----------
    lista: list
        trzyma liste zawierajaca dane
        
    Attributes
    ----------
    lista: tu przechowujemy informacje o parametrze lista

    Examples
    ----------
    >>>stack1 = Stack([63, 323, 'sudo', 2.3, 8, 'oneone'])
    >>>stack1.check_if_not_empty()
    True
    >>>stack1.pop()
    >>>stack.check_len()
    5
    """
    def __init__(self, lista):
        DataStructures.__init__(self, lista)

    def push(self, new):
        """Wstawia nowy element na koniec stosu"""
        self.lista.append(new)

    def pop(self):
        """Usuwa element z końca stosu"""
        self.lista.pop()


class Queue(DataStructures):
    """
    Obiekt Queue opisuje wlasnosci kolejki.
    
    Kolejka to abstrakcyjna, liniowa struktura danych, w ktorej wprowadzony
    element umieszczany jest na koncu listy, a usuwany element jest
    zdejmowany z poczatku listy.
 
    Parameters
    ----------
    lista: list
        trzyma liste zawierajaca dane
        
    Attributes
    ----------
    lista: tu przechowujemy informacje o parametrze lista

    Examples
    ----------
    >>>queue1 = Queue(['cd', 2, 'sudo', 3, 222, 1])
    >>>queue1.enqueue('mint')
    >>>queue1.check_len()
    7
    >>>queue1.dequeue()
    >>>print(queue1)
    deque([2, 'sudo', 3, 222, 1, 'mint'])
    """

    # korzysta z modulu collections
    def __init__(self, lista):
        DataStructures.__init__(self, lista)
        self.lista = collections.deque(lista[:])
    
    def enqueue(self, new):
        """Wstawia nowy element na koniec kolejki"""
        self.lista.append(new)

    def dequeue(self):
        """Usuwa element z poczatku kolejki"""
        self.lista.popleft()


s1 = Stack([1, 2, 'etc', 3, 4])
q1 = Queue([6, 7, 8, 9, 'stack', 'word', 76.3, 12, 'q'])
