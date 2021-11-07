import math


# zad. 9
class Ulamek:
    def __init__(self, licznik, mianownik=1):
        self.licznik = licznik
        assert mianownik != 0, 'mianownik nie moze byc zerem'
        self.mianownik = mianownik

    def __str__(self):
        return str(self.licznik) + "/" + str(self.mianownik)

    def __add__(self, ulamek):
        dodaj = (self.licznik * ulamek.mianownik +
                 ulamek.licznik * self.mianownik,
                 self.mianownik * ulamek.mianownik)

        _licznik = dodaj[0]
        _mianownik = dodaj[1]
        nwd = (_mianownik % _licznik)

        if nwd == 0:
            return _licznik // _mianownik
        else:
            _licznik = _licznik // nwd
            _mianownik = _mianownik // nwd
            return Ulamek(_licznik, _mianownik)

    def __eq__(self, ulamek):
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


u1 = Ulamek(6, 36)
u2 = Ulamek(2, 4)
u3 = Ulamek(1, 2)

print('u1:', u1, ', u2:', u2)
print('dodawanie:', u1 + u2)
print('rownosc:', u1 == u2)
print('rownosc 2/4 = 1/2:', u2 == u3)
print('*' * 10)


# zad. 10
class Prostokat:
    def __init__(self, a=(0, 0), b=(0, 0)):
        self.a = a
        self.b = b

    def dlugosc_bokow(self):
        bok1 = abs(self.a[0] - self.b[0])
        bok2 = abs(self.a[1] - self.b[1])

        return bok1, bok2

    def polozenie_pozostalych_punktow(self):
        c = self.a[0], self.b[1]
        d = self.b[0], self.a[1]
        return c, d

    def pole(self):
        boki = self.dlugosc_bokow()
        _pole = boki[0] * boki[1]
        return _pole

    def obwod(self):
        boki = self.dlugosc_bokow()
        _obwod = boki[0] * 2 + boki[1] * 2
        return _obwod

    def przekatna(self):
        boki = self.dlugosc_bokow()
        _przekatna = math.sqrt(boki[0] ** 2 + boki[1] ** 2)
        return _przekatna

    def srodek(self):
        bok1 = self.dlugosc_bokow()[0] / 2
        bok2 = self.dlugosc_bokow()[1] / 2
        return bok1, bok2

    def __str__(self):
        return str('polozenie punktow prostokata: {}, {}, {}, {}'.format
                   (self.a, self.b,
                    self.polozenie_pozostalych_punktow()[0],
                    self.polozenie_pozostalych_punktow()[1]))

    def __eq__(self, prostokat):
        bok_a = self.dlugosc_bokow()[0]
        bok_b = self.dlugosc_bokow()[1]

        other_a = prostokat.dlugosc_bokow()[0]
        other_b = prostokat.dlugosc_bokow()[1]

        if (bok_a == other_a or bok_a == other_b) and (bok_b == other_a or bok_b == other_b):
            return True
        else:
            return False


prost1 = Prostokat((1, 2), (5, 7))
print('dlugosc bokow:', prost1.dlugosc_bokow())
print('polozenie reszty punktow:', prost1.polozenie_pozostalych_punktow())
print('pole:', prost1.pole())
print('obwod:', prost1.obwod())
print('przekatna:', prost1.przekatna())
print('srodek:', prost1.srodek())
print(prost1)

prost2 = Prostokat((2, 3), (6, 8))
print(prost1 == prost2)

prost3 = Prostokat((1, 2), (6, 8))
print(prost1 == prost3)
print('*' * 10)


# zad. 11
class Prostokat2:
    """Parameters
    ----------
    a: tuple
        trzyma wspolrzedne punktu a (lewy dolny wierzcholek)
    w: int/float
        trzyma szerokosc prostokata
    h: int/float
        trzyma wysokosc prostokata
    """

    def __init__(self, a=(0, 0), w=None, h=None):
        self.a = a
        assert w > 0
        self.w = w
        assert h > 0
        self.h = h

    def polozenie_pozostalych_punktow(self):
        a = self.a
        b = a[0] + self.w, a[1]
        c = a[0], a[1] + self.h
        d = a[0] + self.w, a[1] + self.h
        return b, c, d

    def pole(self):
        _pole = self.w * self.h
        return _pole

    def obwod(self):
        _obwod = self.w * 2 + self.h * 2
        return _obwod

    def przekatna(self):
        _przekatna = math.sqrt(self.w ** 2 + self.h ** 2)
        return _przekatna

    def srodek(self):
        bok1 = self.w / 2
        bok2 = self.h / 2
        return bok1, bok2

    def __str__(self):
        return str('polozenie punktow prostokata: {}, {}, {}, {}'.format
                   (self.a, self.polozenie_pozostalych_punktow()[0],
                    self.polozenie_pozostalych_punktow()[1],
                    self.polozenie_pozostalych_punktow()[2]))


prost4 = Prostokat2((1, 2), 4, 5)
print('polozenie reszty punktow:', prost4.polozenie_pozostalych_punktow())
print('pole:', prost4.pole())
print('obwod:', prost4.obwod())
print('przekatna:', prost4.przekatna())
print('srodek:', prost4.srodek())
print(prost4)
