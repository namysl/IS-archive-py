class Student():
    """Obiekt Student opisuje wlasnosci studentow.

    Parameters
    ----------
    album: int
        trzyma numer albumu
    nazwisko: str
        trzyma nazwisko studenta
    kierunek: str
        trzyma kierunek
    rok: int
        trzyma rok studiow
    grupa: int
        trzyma numer grupy studenta

    Attributes
    ----------
    album: przechowuje informacje o parametrze album
    nazwisko: przechowuje informacje o parametrze nazwisko
    kierunek: przechowuje informacje o parametrze kierunek
    rok: przechowuje informacje o parametrze rok
    grupa: przechowuje informacje o parametrze grupa

    Examples
    --------
    >>> student1 = Student(321654, 'Iksinski', 'Matematyka', 3, 2)"""

    def __init__(self, album, nazwisko, kierunek, rok, grupa):
        self.album = album
        self.nazwisko = nazwisko
        self.kierunek = kierunek
        self.rok = rok
        self.grupa = grupa

    def __repr__(self):
        return self.nazwisko

    def __str__(self):
        dane = (self.album, self.nazwisko, self.kierunek,
                self.rok, self.grupa)
        return str(dane)

    def get_album(self):
        return self.album

    def get_nazwisko(self):
        return self.nazwisko

    def get_kierunek(self):
        return self.nazwisko

    def get_rok(self):
        return self.rok

    def get_grupa(self):
        return self.grupa

    def set_album(self, album):
        self.album = album

    def set_nazwisko(self, nazwisko):
        self.nazwisko = nazwisko

    def set_kierunek(self, kierunek):
        self.kierunek = kierunek

    def set_rok(self, rok):
        self.rok = rok

    def set_grupa(self, grupa):
        self.grupa = grupa


class BazaDanychLTH():
    """Obiekt BazaDanychAB opisuje wlasnosci baz danych.

    Parameters
    ----------
    m: opisuje ilosc pol bazy danych

    Attributes
    ----------
    db: tu przechowuje liste

    Examples
    --------
    >>> ins = BazaDanychLTH(9)
    >>> print(ins)
    [[], [], [], [], [], [], [], [], []]
    >>> ins.dodaj_studenta(student1)
    [[], [], [], [student1], [], [], [], [], []]
    >>> bd.student(321654)
    ('Iksinski', 'Matematyka', 3, 2)
    """

    def __init__(self, m):
        self.m = m
        self.db = [[] for _ in range(self.m)]

    def __repr__(self):
        return "instancja klasy " + __class__.__name__

    def __str__(self):
        return str(self.db)

    def get_db(self):
        return self.db

    def get_m(self):
        return self.m
    
    def set_db(self, *args):
        self.db = [*args]

    def set_m(self, m):
        self.m = m

    def hash_album(self, instancja_Student):
        """Funkcja skrotu dla numeru albumu studenta"""
        return instancja_Student.album % self.m

    def dodaj_studenta(self, instancja_Student):
        """Dodaje studenta do bazy przy pomocy funkcji hash_album"""
        #self.db[BazaDanychLTH.hash_album(self, instancja_Student)].append(instancja_Student)
        
        x = self.db[BazaDanychLTH.hash_album(self, instancja_Student)]
        
        if len(x) == 0:  # pusta baza
            x.append(instancja_Student)
            return self.db
        else:  # sublista ma co najmniej jeden element
            i = 0
            for element in x:
                if instancja_Student.album > x[-1].album:  # najwiekszy numer albumu
                    x.append(instancja_Student)
                    return self.db
                elif instancja_Student.album < x[0].album:  # najmniejszy numer albumu
                    x.insert(0, instancja_Student)
                    return self.db
                # numer albumu gdzies posrodku
                elif x[i].album < instancja_Student.album and instancja_Student.album < x[i+1].album:
                    x.insert(i+1, instancja_Student)
                    return self.db
                i += 1
                
    def dane_studenta(self, album):
        """Wyszukuje i wypisuje dane studenta o podanym albumie"""
        treedown = [item for elem in self.db for item in elem]  # rozwiniecie podlist
        # iterac. wysz. bin.
        low = 0
        high = len(treedown) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if treedown[mid].album < album:
                low = mid + 1
            elif treedown[mid].album > album:
                high = mid - 1
            else:
                dane = treedown[mid].nazwisko, treedown[mid].kierunek, \
                treedown[mid].rok, treedown[mid].grupa
                return dane
        return None


# klasa student
Cobol = Student(album=956123, nazwisko='Cobol',
        kierunek='Informatyka Stosowana', rok=2, grupa=3)
Fortran = Student(album=654321, nazwisko='Fortran',
        kierunek='Informatyka Stosowana', rok=1, grupa=4)
Asembler = Student(album=123456, nazwisko='Asembler',
        kierunek='Informatyka Stosowana', rok=3, grupa=1)
Java = Student(album=671388, nazwisko='Java', kierunek='z',
               rok=1, grupa=1)
Go = Student(album=347298, nazwisko='Go', kierunek='x', rok=1, grupa=1)

# bd
bd = BazaDanychLTH(9)
bd.dodaj_studenta(Asembler)
bd.dodaj_studenta(Go)
bd.dodaj_studenta(Java)
bd.dodaj_studenta(Cobol)
bd.dodaj_studenta(Fortran)
