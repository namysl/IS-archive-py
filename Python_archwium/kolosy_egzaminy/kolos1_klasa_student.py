import random


class Student:
    """Obiekt Student opisuje wlasnosci studentow.

    Parameters
    ----------
    imie: str
        trzyma imie studenta
    nazwisko: str
        trzyma nazwisko studenta
    pesel: int
        trzyma pesel studenta
    plec: str
        trzyma plec studenta
    album: int
        trzyma numer albumu studenta

    Attributes
    ----------
    imie: przechowuje informacje o parametrze imie
    nazwisko: przechowuje informacje o parametrze nazwisko
    pesel: przechowuje informacje o parametrze pesel
    plec: przechowuje informacje o parametrze plec
    album: tu przechowuje informacje o parametrze nr_albumu

    Examples
    --------
    >>> student1 = Student('Iksinski', 'Igrek', 93101106435, 'M', 999111)"""
    def __init__(self, imie, nazwisko, pesel, plec, kierunek, album=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.plec = plec
        self.kierunek = kierunek
        if album is None:
            album = random.randint(202000, 202010)
        self.album = album

    def get_imie(self):
        return self.imie

    def get_nazwisko(self):
        return self.nazwisko

    def get_pesel(self):
        return self.pesel

    def get_plec(self):
        return self.plec

    def get_kierunek(self):
        return self.kierunek

    def get_album(self):
        return self.album

    def set_imie(self, new):
        self.imie = new

    def set_nazwisko(self, new):
        self.nazwisko = new

    def set_pesel(self, new):
        self.pesel = new

    def set_plec(self, new):
        self.plec = new

    def set_kierunek(self, new):
        self.kierunek = new

    def set_album(self, new):
        self.album = new

    def __repr__(self):
        return "instancja klasy" + __class__.__name__

    def __str__(self):
        info = self.nazwisko, self.imie, self.pesel
        return str(info)


class Stypendysta(Student):
    """Obiekt Stypendysta opisuje wlasnosci stypendystow.

    Parameters
    ----------
    imie: str
        trzyma imie studenta
    nazwisko: str
        trzyma nazwisko studenta
    pesel: int
        trzyma pesel studenta
    plec: str
        trzyma plec studenta
    album: int
        trzyma numer albumu studenta
    kwota: int/float
        trzyma kwote stypendium studenta

    Attributes
    ----------
    imie: przechowuje informacje o parametrze imie
    nazwisko: przechowuje informacje o parametrze nazwisko
    pesel: przechowuje informacje o parametrze pesel
    plec: przechowuje informacje o parametrze plec
    album: tu przechowuje informacje o parametrze nr_albumu

    Examples
    --------
    >>> stypendysta1 = Stypendysta('Iksinski', 'Igrek', 93101106435, 'M', 999111, 216.20)"""
    def __init__(self, imie, nazwisko, pesel, plec, kierunek, album, kwota):
        super().__init__(imie, nazwisko, pesel, plec, kierunek, album)
        self.kwota = kwota

    def get_kwota(self):
        return self.kwota

    def set_kwota(self, new):
        self.kwota = new

    def __repr__(self):
        return "instancja klasy" + __class__.__name__

    def __str__(self):
        info = self.nazwisko, self.imie, self.pesel, self.kwota
        return str(info)


stypendysta1 = Stypendysta('krt', 'albns', 931009, 'K', 'infostos', 292, 30.80)
student1 = Student('Abc', 'Zet', 92111142435, 'K', 'matma')
print(student1.album)
