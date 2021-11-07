import random


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


class BazaDanychAB():

    """Obiekt BazaDanychAB opisuje wlasnosci baz danych.

    Parameters
    ----------
    None

    Attributes
    ----------
    db: tu przechowuje liste

    Examples
    --------
    >>> bd = BazaDanychAB()
    >>> bd.dodaj_studenta(student1)
    [student1]
    >>> bd.student(321654)
    (321654, 'Iksinski', 'Matematyka', 3, 2)
    """

    def __init__(self):
        self.db = []

    def __repr__(self):
        return "instancja klasy " + __class__.__name__

    def __str__(self):
        return str(self.db)

    def get_db(self):
        return self.db

    def set_db(self, *args):
        self.db = [*args]

    def dodaj_studenta(self, instancja_Student):
        """Dodaje studenta do bazy wzgledem jego
        numeru albumu w kolejnosci rosnacej"""

        if len(self.db) == 0:  # pusta baza
            self.db.append(instancja_Student)
            return self.db
        else:  # lista ma co najmniej jeden element
            i = 0
            for element in self.db:
                if instancja_Student.album > self.db[-1].album:  # najwiekszy numer albumu
                    self.db.append(instancja_Student)
                    return self.db
                elif instancja_Student.album < self.db[0].album:  # najmniejszy numer albumu
                    self.db.insert(0, instancja_Student)
                    return self.db
                # numer albumu gdzies posrodku
                elif self.db[i].album < instancja_Student.album and instancja_Student.album < self.db[i+1].album:
                    self.db.insert(i+1, instancja_Student)
                    return self.db
                i += 1

    def _student_idx(self, nr_album):
        """Wyszukuje i zwraca indeks w liscie pod ktorym znajduje sie
        student o podanym numerze albumu. Jesli nie ma takiego
        numeru, zwraca None"""
        # iteracyjne wyszukiwanie binarne
        low = 0
        high = len(self.db) - 1
        mid = 0

        while low <= high:
            mid = (high + low) // 2
            if self.db[mid].album < nr_album:
                low = mid + 1
            elif self.db[mid].album > nr_album:
                high = mid - 1
            else:
                return mid
        return None

    def student(self, album):
        """Wyszukuje i zwraca informacje o studencie
        posiadającym podany numer albumu"""
        wynik = BazaDanychAB._student_idx(self, album)  # indeks albumu
        dane = print(self.db[wynik])
        return dane

    def usun_studenta(self, album):
        """Wyszukuje i usuwa rekord ze studentem o podanym
        numerze albumu. Jesli nie ma takiego numeru albumu, zwraca None"""
        wynik = BazaDanychAB._student_idx(self, album)  # indeks
        if wynik is None:
            return None
        else:
            self.db.pop(wynik)

    def lista_albumow(self):
        """Zwraca liste numerow albumow studentow w bazie"""
        albumy = []
        i = 0
        for element in self.db:
            albumy.append(self.db[i].album)
            i += 1
        return albumy

    def generuj_studenta(self, ilu):
        """Funkcja pomocnicza, generuje instancje studentow
        i dodaje do bazy metoda dodaj_studenta

        ilu: liczba generowanych instancji"""
        for x in range(0, ilu):
            var = Student(album=random.randint(111111, 999999),
                nazwisko=str(x), kierunek=str(x+x),
                rok=random.randint(1, 5), grupa=random.randint(1, 3))
            BazaDanychAB.dodaj_studenta(self, var)


# basics
Cobol = Student(album=956123, nazwisko='Cobol',
        kierunek='Informatyka Stosowana', rok=2, grupa=3)
Fortran = Student(album=654321, nazwisko='Fortran',
        kierunek='Informatyka Stosowana', rok=1, grupa=4)
Asembler = Student(album=123456, nazwisko='Asembler',
        kierunek='Informatyka Stosowana', rok=3, grupa=1)

ins = BazaDanychAB()
ins.dodaj_studenta(Asembler)
ins.dodaj_studenta(Cobol)
ins.dodaj_studenta(Fortran)
ins.usun_studenta(654321)

# testy dla 100 studentow z funkcja generuj_studenta()
ins.generuj_studenta(100)
print(ins.get_db())
