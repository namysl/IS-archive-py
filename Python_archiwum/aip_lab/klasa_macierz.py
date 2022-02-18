class Macierz:
    """
    Obiekt Macierz opisuje wlasnosci macierzy.
 
    Parameters
    ----------
    lista: list
        trzyma liste zawierajaca dane
        
    Attributes
    ----------
    lista: tu przechowujemy informacje o parametrze lista
    n: tu przechowujemy informacje o parametrze n
    m: tu przechowujemy informacje o parametrze m

    Examples
    ----------
    >>>matrix = Macierz([[1,1,1],[1,1,1]])
    >>>matrix.wymiary()
    (2, 3)
    >>>matrix.mnoz_lczb(2)
    [[2, 2, 2], [2, 2, 2]]
    """
    def __init__(self, lista):
        self.lista = lista[:]
        self.n = len(self.lista) # kolumny
        self.m = len(self.lista[0]) # rzedy

    def __str__(self):
        return str(self.lista)
    
    def __repr__(self):
        return "instancja klasy " + self.__class__.__name__

    def wymiary(self):
        """Zwraca wymiary macierzy (kolumny, rzedy)"""
        return self.n, self.m

    def reorganizuj(self, dane):
        """Funkcja pomocnicza, wyniki dodawania lub mnozenia macierzy reorganizuje
        w liste list (pierwotny wyglad macierzy)"""
        start = 0
        stop = self.m
        gotowa_lista = [] # trzyma zreorganizowane w podlisty dane
        for i in range(self.m - 1): 
           gotowa_lista.append(dane[start:stop]) # dodaje do listy dane odpowiadajace zmiennym start i stop
           start += self.m
           stop += self.m
        return gotowa_lista

    def dodaj_mac(self, macierz):
        """Zwraca wynik dodawania dwoch macierzy"""
        assert self.wymiary() == macierz.wymiary(), \
               "Wymiary macierzy musza byc takie same, aby mozliwe bylo ich dodawanie"
        
        wynik = [] # trzyma wyniki kolejnych sum elementow
        for n in range(self.n): # iteruje po kolmnach
            for m in range(self.m): # iteruje po rzedach
                wynik.append(self.lista[n][m] + macierz.lista[n][m])

        return self.reorganizuj(wynik) # przesyla wynik do funkcji pomocnicznej, aby otrzymac zreorganizowany wynik 

    def mnoz_lczb(self, liczba):
        """Zwraca wynik mnozenia macierzy przez liczbe"""
        
        wynik = [] # trzyma wyniki mnozenia liczb przez kolejne elementy macierzy
        for n in range(self.n): # iteruje po kolumnach
            for m in range(self.m): # po rzedach
                wynik.append(self.lista[n][m] * liczba) 

        return self.reorganizuj(wynik) # reorganizacja wyniku, zwrocenie go

    def mnoz_mac(self, macierz):
        """Zwraca wynik mnozenia dwoch macierzy"""
        assert self.m == macierz.n, "Ilosc elementow kolumny w jednej macierzy musi byc rowna \
        liczbie elementow rzedu w drugiej macierzy, aby mozliwe bylo ich przemnozenie"

        wynik = [[sum(a*b for a, b in zip(self.rzedy, macierz.kolumny)) \
                   for macierz.kolumny in zip(*macierz.lista)] for self.rzedy in self.lista]
        # sumuje przemnozone wartosci z dwoch macierzy (rzad x kolumna), korzystajac z funkcji zip,
        # ktora laczy wartosci z macierzy1 (self) i macierzy2, iterujac kolejno po kolumnach jednej i rzedach drugiej
        # nie potrzeba tu funkcji pomocniczej, wystarczy zagniezdzona lista
        return wynik


mac1 = Macierz([[1,2,3],[4,5,6]])
mac2 = Macierz([[2,3,4],[1,2,3]])
mac3 = Macierz([[2,2],[3,4,5]])         
mac4 = Macierz([[2,3,4],[1,2,3],[1,1,1]])

print(mac1.dodaj_mac(mac2), '\n\n',\
mac2.mnoz_lczb(3), '\n\n',\
mac1.mnoz_mac(mac4), '\n\n')
