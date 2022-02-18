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



#Uzupelnij klase Ulamek powyzej o mozliwosc dodawania (+, +=),
#odejmowania (−, −=), dzielenia, skracania, porównywania (<=, <, >=, =) ulamkow.


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
    
# dzielenie juz bylo w programie (__truediv__)

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

    def __ge__(self, ulamek): # >=
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

    def __gt__(self, ulamek): # >
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



# do testow
u1 = Ulamek(1, 2)
u2 = Ulamek(1, 3)
u3 = Ulamek(6, 36)
u4 = Ulamek(36, 6)
u5 = Ulamek(0, 5)
u6 = Ulamek(8, 8)
u7 = Ulamek(9, 1)
u8 = Ulamek(10, 4)
u9 = Ulamek(9,2)
u10 = Ulamek(2, 4)
