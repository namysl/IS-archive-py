class ZeroMianownik(Exception):
    def __str__(self):
        return "Mianownik jest zerem - popraw dane"

class Ulamek(object):
    def __init__(self, licznik, mianownik = 1):
        self.licznik = licznik
        if mianownik == 0: 
            raise ZeroMianownik
        self.mianownik = mianownik

    def __str__(self):
        print("str")
        return str(self.licznik) + "/" + str(self.mianownik)

    def __mul__(self, ulamek): # self * other
        print("Metoda mul")
        return Ulamek(self.licznik * ulamek.licznik, self.mianownik * ulamek.mianownik)

    def __rmul__(self, other): # other * self
        print("Metoda rmul")
        return Ulamek(self.licznik * other, self.mianownik)

    def __truediv__(self, ulamek):
        #zabezpieczenie 
        return Ulamek(self.licznik * ulamek.mianownik, self.mianownik * ulamek.licznik)

    def __lt__(self, u): # self < other
        nwww = nww(self.mianownik, u.mianownik)
        self.licznik = (self.licznik * nwww)/self.mianownik
        # self.mianownik = self.mianownik * nwww
        u.licznik = (u.licznik * nwww)/u.mianownik
        # u.mianownik = u.mianownik * nwww
        if self.licznik < u.licznik:
            return True
        else:
            return False

    def __add__(self, ulamek):
        """x + y"""
        print("Metoda add")
        
        dod = Ulamek(self.licznik * ulamek.mianownik + ulamek.licznik * self.mianownik, \
                      self.mianownik * ulamek.mianownik)
        print(dod)
        return dod
    
    def __iadd__(self, other):
        """ x += y"""
        print("Metoda iadd")
        
        dodeq = Ulamek(self.licznik * other.mianownik + other.licznik * self.mianownik, \
                      self.mianownik * other.mianownik)
        print(dodeq)
        return dodeq

    def __sub__(self, ulamek):
        """x - y"""
        
        print("Metoda sub")
        ode = Ulamek(self.licznik * ulamek.mianownik - ulamek.licznik * self.mianownik, \
                      self.mianownik * ulamek.mianownik)
        print(ode)
        return ode

    def __isub__(self, other):
        """x -= y"""
        
        print("Metoda isub")
        odeeq = Ulamek(self.licznik * other.mianownik - other.licznik * self.mianownik, \
                      self.mianownik * other.mianownik)
        print(odeeq)
        return odeeq

    def skroc(self):
        """Skraca ulamek do najmniejszej mozliwej formy.
        Jesli wynikiem skrocenia nadal jest ulamek, to podmienia na skrocony.
        W innych przypadkach nie zmienia parametrow."""
        nwd = (self.licznik % self.mianownik)        
        if nwd == 0:
            return int(self.licznik / self.mianownik)
        else:
            self.licznik = int(self.licznik/nwd)
            self.mianownik = int(self.mianownik/nwd)
            print(self.licznik,"/",self.mianownik)
            return Ulamek(self.licznik, self.mianownik)

        
    def __le__(self, ulamek): # <=
        """Sprawdza czy ulamek jest mniejszy lub rowny innemu ulamkowi."""
        self_licznik = self.licznik * ulamek.mianownik 
        self_mianownik = self.mianownik * ulamek.mianownik

        ulamek_licznik = ulamek.licznik * self.mianownik
        ulamek_mianownik = ulamek.mianownik * self.mianownik

        pierwsza = self_licznik / self_mianownik
        druga = ulamek_licznik / ulamek_mianownik
        
        if pierwsza <= druga:
            return True
        else:
            return False
        
    def __eq__(self, ulamek): # ==
        """Sprawdza czy ulamek jest rowny innemu ulamkowi."""
        self_licznik = self.licznik * ulamek.mianownik 
        self_mianownik = self.mianownik * ulamek.mianownik

        ulamek_licznik = ulamek.licznik * self.mianownik
        ulamek_mianownik = ulamek.mianownik * self.mianownik

        pierwsza = self_licznik / self_mianownik
        druga = ulamek_licznik / ulamek_mianownik
        
        if pierwsza == druga:
            return True
        else:
            return False

    def __ge__(): # >=
        """Sprawdza czy ulamek jest wiekszy lub rowny innemu ulamkowi."""
        self_licznik = self.licznik * ulamek.mianownik 
        self_mianownik = self.mianownik * ulamek.mianownik

        ulamek_licznik = ulamek.licznik * self.mianownik
        ulamek_mianownik = ulamek.mianownik * self.mianownik

        pierwsza = self_licznik / self_mianownik
        druga = ulamek_licznik / ulamek_mianownik
        
        if pierwsza >= druga:
            return True
        else:
            return False

    def __gt__(): # >
        """Sprawdza czy ulamek jest wiekszy od innego ulamka."""
        self_licznik = self.licznik * ulamek.mianownik 
        self_mianownik = self.mianownik * ulamek.mianownik

        ulamek_licznik = ulamek.licznik * self.mianownik
        ulamek_mianownik = ulamek.mianownik * self.mianownik

        pierwsza = self_licznik / self_mianownik
        druga = ulamek_licznik / ulamek_mianownik
        
        if pierwsza > druga:
            return True
        else:
            return False


    def __setattr__(self, name, value): # setattr dla klasy Ulamek
        if name == 'licznik' or name == 'mianownik': # jesli nazwa atrybutu pojawia sie w __init__
            object.__setattr__(self, name, value) # to zezwala na zmiane wartosci pola
        else: # jesli nie ma takiego atrybutu w __init__
            raise AttributeError('Nie mozna stworzyc nowego atrybutu') # wyrzuca blad


    
class Zespolone:
    def __init__(self, re, im):
        self.re = re 
        self.im = im

    def __add__(self, other):
        """Dodawanie liczb zespolonych"""
        suma = self.re + other.re, self.im + other.im
        return suma
    
    def __setattr__(self, name, value): # setattr dla klasy Zespolone
        if name == 're' or name == 'im': # podobna sytuacja jak w setattr Ulamek
            object.__setattr__(self, name, value)
        else:
            raise AttributeError('Nie mozna stworzyc nowego atrybutu')


ulamek1 = Ulamek(1, 2)
urojona1 = Zespolone(2, 3)
