class StarWarsVehicle(object):
    """
    Obiekt StarWarsVehicle opisuje nam wlasnosci pojazdow z serii StarWars.
    
    Pojazd to srodek transportu.
 
    Parameters
    ----------
    nazwa: str
        trzyma nazwe pojazdu
    v: int or float
        trzyma predkosc pojazdu
    uzbrojenie: str
        trzyma opis uzbrojenia pojazdu
    cmu: int or float
        trzyma wartosc liczbowa uzbrojenia pojazdu
    w: int or float
        trzyma wartosc wytrzymalosci pojazdu
        
    Attributes
    ----------
    nazwa: tu przechowujemy informacje o parametrze nazwa
    v: tu przechowujemy informacje o parametrze v
    uzbrojenie: tu przechowujemy informacje o parametrze uzbrojenie
    cmu: tu przechowujemy informacje o parametrze cmu
    w: tu przechowujemy informacje o parametrze w
    
    Examples
    --------
    >>> p1 = StarWarsVehicle('Nazwa1', 200, 'dwie armatki o mocy 200', 2*200, 555)
    """
    def __init__(self, nazwa, v, uzbrojenie, cmu, w):
        self.nazwa = nazwa
        self.v = v # predkosc
        self.uzbrojenie = uzbrojenie
        self.cmu = cmu # calkowita moc uzbrojenia
        self.w = w # wytrzymalosc

    def __repr__(self):
        return 'instancja klasy ' + self.__class__.__name__

    def szansa(self):
        """Zwraca szanse na wygrana wybranej jednostki"""
        s = 0.2 * self.v + 0.5 * self.cmu + 0.3 * self.w
        return s
    
    def get_nazwa(self):
        return self.nazwa
    def get_v(self):
        return self.v
    def get_uzbrojenie(self):
        return self.uzbrojenie
    def get_cmu(self):
        return self.cmu
    def get_w(self):
        return self.w

    def set_nazwa(self, nazwa):
        self.nazwa = nazwa
    def set_v(self, v):
        self.v = v
    def set_uzbrojenie(self, uzbrojenie):
        self.uzbrojenie = uzbrojenie
    def set_cmu(self, cmu):
        self.cmu = cmu
    def set_w(self, w):
        self.w = w

    def __eq__(self, other):
        if self.szansa() == other.szansa():
            return True
        else:
            return False
        
    def __gt__(self, other):
        if self.szansa() > other.szansa():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.szansa() >= other.szansa():
            return True
        else:
            return False   

    def __lt__(self, other):
        if self.szansa() < other.szansa():
             return True
        else:
            return False

    def __le__(self, other):
        if self.szansa() <= other.szansa():
            return True
        else:
            return False

    def atakuj(self, other):
        """Zwraca string okreslajacy wynik walki miedzy dwiema jednostkami"""
        if self.szansa() == other.szansa():
            return "Remis"
        elif self.szansa() > other.szansa():
            return "Zwyciestwo"
        elif self.szansa() < other.szansa():
            return "Porazka"
        else:
            return 0


class Mysliwce(StarWarsVehicle):
    """
    Obiekt Mysliwce opisuje nam wlasnosci mysliwcow.
    
    Mysliwiec to jednostka latajaca.
 
    Parameters
    ----------
    nazwa: str
        trzyma nazwe mysliwa
    v: int or float
        trzyma predkosc mysliwca
    uzbrojenie: str
        trzyma opis uzbrojenia mysliwca
    cmu: int or float
        trzyma wartosc liczbowa uzbrojenia mysliwca
    w: int or float
        trzyma wartosc wytrzymalosci mysliwca
    cena: int or float
        trzyma cene mysliwca
    hipernaped: boolean
        trzyma wartosc boolowska hipernapedu mysliwca
        
        
    Attributes
    ----------
    nazwa: tu przechowujemy informacje o parametrze nazwa
    v: tu przechowujemy informacje o parametrze v
    uzbrojenie: tu przechowujemy informacje o parametrze uzbrojenie
    cmu: tu przechowujemy informacje o parametrze cmu
    w: tu przechowujemy informacje o parametrze w
    cena: tu przechowujemy informacje o parametrze cena
    hipernaped: tu przechowujemy informacje o parametrze hipernaped
    
    Examples
    --------
    >>> p2 = Mysliwce('Nazwa2', 400, 'dwie rakiety o mocy 500', 2*500, 1000, 55000, True)
    >>> p2.szansa()
    880.0
    """
    def __init__(self, nazwa, v, uzbrojenie, cmu, w, cena, hipernaped):
        StarWarsVehicle.__init__(self, nazwa, v, uzbrojenie, cmu, w)
        self.cena = cena
        self.hipernaped = hipernaped

    def __str__(self):
        opis = "Nazwa: " + str(self.nazwa) + "\n" + "Predkosc: " + str(self.v) + "\n" + \
        "Uzbrojenie: " + str(self.uzbrojenie) + "\n" + "Calkowita moc uzbrojenia: " \
        + str(self.cmu) + "\n" + "Wytrzymalosc: " + str(self.w) + "\n" + \
        "Cena: " + str(self.cena) + "\n" + "Hipernaped: " + str(self.hipernaped)
        return opis

    def get_cena(self):
        return self.cena
    def get_hipernaped(self):
        return self.hipernaped
    
    def set_cena(self, cena):
        self.cena = cena
    def set_hipernaped(self, hipernaped):
        self.hipernaped = hipernaped
        
class Transportowce(StarWarsVehicle):
    """
    Obiekt Transportowce opisuje nam wlasnosci transportowcow.
    
    Transportowiec to jednostka plywajaca, przewozaca towary lub inny sprzet.
 
    Parameters
    ----------
    nazwa: str
        trzyma nazwe transportowca
    v: int or float
        trzyma predkosc transportowca
    uzbrojenie: str
        trzyma opis uzbrojenia transportowca
    cmu: int or float
        trzyma wartosc liczbowa uzbrojenia transportowca
    w: int or float
        trzyma wartosc wytrzymalosci transportowca
    cena: int or float
        trzyma cene transportowca
    ladownosc: int or float
        trzyma wartosc ladownosci transportowca
        
        
    Attributes
    ----------
    nazwa: tu przechowujemy informacje o parametrze nazwa
    v: tu przechowujemy informacje o parametrze v
    uzbrojenie: tu przechowujemy informacje o parametrze uzbrojenie
    cmu: tu przechowujemy informacje o parametrze cmu
    w: tu przechowujemy informacje o parametrze w
    cena: tu przechowujemy informacje o parametrze cena
    ladownosc: tu przechowujemy informacje o parametrze ladownosc
    
    Examples
    --------
    >>> p3 = Transportowce('Nazwa3', 500, 'trzy miny o mocy 200', 3*200, 3000, 1000000, 660)
    >>> p3.szansa()
    1300.0
    """
    def __init__(self, nazwa, v, uzbrojenie, cmu, w, cena, ladownosc):
        StarWarsVehicle.__init__(self, nazwa, v, uzbrojenie, cmu, w)
        self.cena = cena
        self.ladownosc = ladownosc

    def __str__(self):
        opis = "Nazwa: " + str(self.nazwa) + "\n" + "Predkosc: " + str(self.v) + "\n" + \
        "Uzbrojenie: " + str(self.uzbrojenie) + "\n" + "Calkowita moc uzbrojenia: " \
        + str(self.cmu) + "\n" + "Wytrzymalosc: " + str(self.w) + "\n" + \
        "Cena: " + str(self.cena) + "\n" + "Ladownosc: " + str(self.ladownosc)
        return opis

    def get_cena(self):
        return self.cena
    def get_ladownosc(self):
        return self.ladownosc
    
    def set_cena(self, cena):
        self.cena = cena
    def set_ladownosc(self, ladownosc):
        self.ladownosc = ladownosc
        
class Stacjonarne(StarWarsVehicle):
    """
    Obiekt Stacjonarne opisuje nam wlasnosci pojazdow stacjonarnych.
    
    Pojazd stacjonarny to???
 
    Parameters
    ----------
    nazwa: str
        trzyma nazwe stacjonarnego
    v: int or float
        trzyma predkosc stacjonarnego
    uzbrojenie: str
        trzyma opis uzbrojenia stacjonarnego
    cmu: int or float
        trzyma wartosc liczbowa uzbrojenia stacjonarnego
    w: int or float
        trzyma wartosc wytrzymalosci stacjonarnego
    cena: int or float
        trzyma cene stacjonarnego
    pojemnosc_baku: int or float
        trzyma wartosc ladownosci stacjonarnego
        
        
    Attributes
    ----------
    nazwa: tu przechowujemy informacje o parametrze nazwa
    v: tu przechowujemy informacje o parametrze v
    uzbrojenie: tu przechowujemy informacje o parametrze uzbrojenie
    cmu: tu przechowujemy informacje o parametrze cmu
    w: tu przechowujemy informacje o parametrze w
    cena: tu przechowujemy informacje o parametrze cena
    pojemnosc_baku: tu przechowujemy informacje o parametrze pojemnosc_baku
    
    Examples
    --------
    >>> p4 = Stacjonarne('Nazwa4', 9000, 'trzy karabiny o mocy 100', 3*100, 300, 1000, 808)
    >>> p4.szansa()
    2040.0
    """
    def __init__(self, nazwa, v, uzbrojenie, cmu, w, cena, pojemnosc_baku):
        StarWarsVehicle.__init__(self, nazwa, v, uzbrojenie, cmu, w)
        self.cena = cena
        self.pojemnosc_baku = pojemnosc_baku

    def __str__(self):
        opis = "Nazwa: " + str(self.nazwa) + "\n" + "Predkosc: " + str(self.v) + "\n" + \
        "Uzbrojenie: " + str(self.uzbrojenie) + "\n" + "Calkowita moc uzbrojenia: " \
        + str(self.cmu) + "\n" + "Wytrzymalosc: " + str(self.w) + "\n" + \
        "Cena: " + str(self.cena) + "\n" + "Pojemnosc baku: " + str(self.pojemnosc_baku)
        return opis

    def get_cena(self):
        return self.cena
    def get_pojemnosc_baku(self):
        return self.pojemnosc_baku
    
    def set_cena(self, cena):
        self.cena = cena
    def set_pojemnosc_baku(self, pojemnosc_baku):
        self.pojemnosc_baku = pojemnosc_baku

# przyklady instancji klas
mys1 = Mysliwce('Orzel', 600, '4 dzialka mocy 200', 4*200, 500, 20000, True)
mys2 = Mysliwce('Wrobel', 201, '60 dzial mocy 50', 60*50, 600, 34000, False)
mys3 = Mysliwce('Kanarek', 122, '10 armatek mocy 20, 2 torpedy mocy 100', 10*20+2*100, 300, 9999, False) 
tra1 = Transportowce('Ryba', 300, '6 torped mocy 100', 6*100, 1000, 60000, 2000)
tra2 = Transportowce('Rekin', 569, '2 miny mocy 1000', 2*1000, 2000, 50000, 999)
tra3 = Transportowce('Orka', 100, '50 dzialek mocy 60', 50*60, 1500, 35000, 4000)
sta1 = Stacjonarne('Jeż', 400, '2 pociski mocy 500', 2*500, 300, 5000, 800)
sta2 = Stacjonarne('Borsuk', 333, '5 dzialek mocy 550, 2 armatki mocy 40', 5*550+2*40, 888, 6000, 500)
sta3 = Stacjonarne('Rosomak', 599, '2 dzialka mocy 700', 2*700, 1500, 11000, 1500)

lista = [mys1, mys2, mys3, tra1, tra2, tra3, sta1, sta2, sta3]

# walka kazdy z kazdym
for i in lista:
    for j in lista:
        print('Szansa', i.nazwa, ':', i.szansa(), '\nSzansa', j.nazwa, ':', j.szansa())
        if i.atakuj(j) == 'Remis':
            print(i.atakuj(j), '\n')
        else:
            print(i.atakuj(j),'dla', i.nazwa, '\n')

# inne testy
print(mys1)
print(mys1.get_cmu(), mys1.szansa())
print(sta3.get_pojemnosc_baku(), sta3.szansa())
