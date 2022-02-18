class Pojazd:
    """Abstrakcyjna klasa do opisu Pojazdow"""

    def __str__(self):
        raise NotImplementedError("Funkcja __str__ nie jest zaimplementowana")
    def __repr__(self):
        raise NotImplementedError("Funkcja __repr__ nie jest zaimplementowana")
    
    def get_wypornosc(self):
        return NotImplementedError("Funkcja get_wypornosc nie jest zaimplementowana")
    def get_pojemnosc(self):
        raise NotImplementedError("Funkcja get_pojemnosc nie jest zaimplementowana")
    def get_ENI(self):
        raise NotImplementedError("Funkcja get_ENI nie jest zaimplementowana")
    def get_marka(self):
        raise NotImplementedError("Funkcja get_marka nie jest zaimplementowana")
    def get_model(self):
        raise NotImplementedError("Funkcja get_model nie jest zaimplementowana")
    def get_moc(self):
        raise NotImplementedError("Funkcja get_moc nie jest zaimplementowana")
    def get_rok_produkcji(self):
        raise NotImplementedError("Funkcja get_rok_produkcji nie jest zaimplementowana")
    def get_VIN(self):
        raise NotImplementedError("Funkcja get_VIN nie jest zaimplementowana")

    def set_wypornosc(self):
        raise NotImplementedError("Funkcja set_wypornosc nie jest zaimplementowana")
    def set_pojemnosc(self):
        raise NotImplementedError("Funkcja set_pojemnosc nie jest zaimplementowana")
    def set_ENI(self):
        raise NotImplementedError("Funkcja set_ENI nie jest zaimplementowana")
    def set_marka(self):
        raise NotImplementedError("Funkcja set_marka nie jest zaimplementowana")
    def set_model(self):
        raise NotImplementedError("Funkcja set_model nie jest zaimplementowana")
    def set_moc(self):
        raise NotImplementedError("Funkcja set_moc nie jest zaimplementowana")
    def set_rok_produkcji(self):
        raise NotImplementedError("Funkcja set_rok_produkcji nie jest zaimplementowana")
    def set_VIN(self):
        raise NotImplementedError("Funkcja set_VIN nie jest zaimplementowana")
  

class Statek(Pojazd):
    """
    Obiekt Statek opisuje wlasnosci statkow.
    
    Statki to srodki transportu zdolne do pokonywania odleglosci
    przemieszczajac sie po powierzchni wody.
 
    Parameters
    ----------
    wypornosc: int or float
        trzyma wypornosc statku
    pojemnosc: int or float
        trzyma pojemnosc statku
    ENI: int
        trzyma europejski numer identyfikacyjny statku
        
    Attributes
    ----------
    wypornosc: tu przechowujemy informacje o parametrze wypornosc
    pojemnosc: tu przechowujemy informacje o parametrze pojemnosc
    ENI: tu przechowujemy informacje o parametrze ENI
    
    Examples
    --------
    >>> statek1 = Statek(200, 545.39, 4242141)
    """
    def __init__(self, wypornosc, pojemnosc, ENI):
        self.wypornosc = wypornosc
        self.pojemnosc = pojemnosc
        self.ENI = ENI

    def __str__(self):
        opis = "Wypornosc: " + str(self.wypornosc) + "\n" + \
        "Pojemnosc: " + str(self.pojemnosc) + "\n" + \
        "ENI: " + str(self.ENI)
        return opis
    
    def __repr__(self):
        return "instancja klasy " + self.__class__.__name__
    
    def get_wypornosc(self):
        return self.wypornosc
    def get_pojemnosc(self):
        return self.pojemnosc
    def get_ENI(self):
        return self.ENI

    def set_wypornosc(self, wypornosc):
        self.wypornosc = wypornosc
    def set_pojemnosc(self, pojemnosc):
        self.pojemnosc = pojemnosc
    def set_ENI(self, ENI):
        self.ENI = ENI

class Samochod(Pojazd):
    """
    Obiekt Samochod opisuje wlasnosci samochodow.
    
    Samochody to srodki transportu zdolne do pokonywania odleglosci
    przemieszczajac sie po ziemi przy pomocy silnikow spalinowych lub elektrycznych.
 
    Parameters
    ----------
    marka: str
        trzyma markę samochodu
    model: str
        trzyma model samochodu
    moc: int or float
        trzyma moc samochodu
    rok_produkcji: int
        trzyma rok produkcji samochodu
    VIN: str
        trzyma numer identyfikacyjny pojazdu samochodu

    Attributes
    ----------
    marka: tu przechowujemy informacje o parametrze marka
    model: tu przechowujemy informacje o parametrze model
    moc: tu przechowujemy informacje o parametrze moc
    rok_produkcji: tu przechowujemy informacje o parametrze rok_produkcji
    VIN: tu przechowujemy informacje o parametrze VIN

    
    Examples
    --------
    >>> samochod1 = Samochod("Peugeot", "107", 499.00, 2009, "VF3140989SN")
    >>> samochod1.get_marka()
    'Peugeot'
    """
    def __init__(self, marka, model, moc, rok_produkcji, VIN):
        self.marka = marka
        self.model = model
        self.moc = moc
        self.rok_produkcji = rok_produkcji
        self.VIN = VIN

    def __str__(self):
        opis = "Marka: " + str(self.marka) + "\n" + \
        "Model: " + str(self.model) + "\n" + \
        "Moc: " + str(self.moc) + "\n" + \
        "Rok produkcji: " + str(self.rok_produkcji) + "\n" + \
        "VIN: " + str(self.VIN)
        return opis

    def __repr__(self):
        return "instancja klasy " + self.__class__.__name__

    def get_marka(self):
        return self.marka
    def get_model(self):
        return self.model
    def get_moc(self):
        return self.moc
    def get_rok_produkcji(self):
        return self.rok_produkcji
    def get_VIN(self):
        return self.VIN

    def set_marka(self, marka):
        self.marka = marka
    def set_model(self, model):
        self.model = model
    def set_moc(self, moc):
        self.moc = moc
    def set_rok_produkcji(self, rok_produkcji):
        self.rok_produkcji = rok_produkcji
    def set_VIN(self, VIN):
        self.VIN = VIN
        
class Amfibia(Statek, Samochod):
    """
    Obiekt Amfibia opisuje wlasnosci amfibii.
    
    Amfibie to srodki transportu zdolne do pokonywania odleglosci
    przemieszczajac sie zarowno po ladzie, jak i w wodzie.
 
    Parameters
    ----------
    wypornosc: int or float
        trzyma wypornosc amfibii
    pojemnosc: int or float
        trzyma pojemnosc amfibii
    ENI: int
        trzyma europejski numer identyfikacyjny amfibii
    marka: str
        trzyma markę amfibii
    model: str
        trzyma model amfibii
    moc: int or float
        trzyma moc amfibii
    rok_produkcji: int
        trzyma rok produkcji amfibii
    VIN: str
        trzyma numer identyfikacyjny pojazdu amfibii
        
    Attributes
    ----------
    wypornosc: tu przechowujemy informacje o parametrze wypornosc
    pojemnosc: tu przechowujemy informacje o parametrze pojemnosc
    ENI: tu przechowujemy informacje o parametrze ENI
    marka: tu przechowujemy informacje o parametrze marka
    model: tu przechowujemy informacje o parametrze model
    moc: tu przechowujemy informacje o parametrze moc
    rok_produkcji: tu przechowujemy informacje o parametrze rok_produkcji
    VIN: tu przechowujemy informacje o parametrze VIN
    
    Examples
    --------
    >>> amfibia1 = Amfibia(345, 199.9, 2321421, "Ford", "XO", 1040, 1993, "KL435345")
    """
    def __init__(self, wypornosc, pojemnosc, ENI, marka, model, moc, rok_produkcji, VIN):
        Statek.__init__(self, wypornosc, pojemnosc, ENI)
        Samochod.__init__(self, marka, model, moc, rok_produkcji, VIN)

    def __str__(self):
        opis = "Wypornosc: " + str(self.wypornosc) + "\n" + \
        "Pojemnosc: " + str(self.pojemnosc) + "\n" + \
        "ENI: " + str(self.ENI) + "\n" + \
        "Marka: " + str(self.marka) + "\n" + \
        "Model: " + str(self.model) + "\n" + \
        "Moc: " + str(self.moc) + "\n" + \
        "Rok produkcji: " + str(self.rok_produkcji) + "\n" + \
        "VIN: " + str(self.VIN)
        return opis


statek1 = Statek(200, 545.39, 4242141)
statek2 = Statek(300, 5324, 24142)
statek3 = Statek(323, 222, 424992)

samochod1 = Samochod("Peugeot", "107", 499.00, 2009, "VF3140989SN")
samochod2 = Samochod("Toyota", "Civic", 1050, 2017, "KS233132SS")
samochod3 = Samochod("Toyota", "Yaris", 799, 2015, "SE324324P")

amfibia1 = Amfibia(345, 199.9, 2321421, "Ford", "XO", 1040, 1993, "KL435345")
amfibia2 = Amfibia(321, 276.9, 657567654, "Lada", "Proj", 3154, 1964, "KR3242321SO")
amfibia3 = Amfibia(121, 788, 2321421, "Jeep", "S32", 999, 1989, "TS2433242A")

# testy
print("INSTANCJE STATEK:\n", \
statek1.get_wypornosc(), \
statek2.get_pojemnosc(), \
statek3.get_ENI() )

statek1.set_wypornosc(111)
statek1.set_pojemnosc(222)
statek1.set_ENI(333)
print(statek1)

print("\nINSTANCJE SAMOCHODU:")
print(samochod1,'\n\n', samochod2,'\n\n', samochod3)

print("\nINSTANCJE AMFIBII:")
print(amfibia1, '\n\n', amfibia2, '\n\n', amfibia3)
