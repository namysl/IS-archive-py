from math import sqrt

class Trojkat(object):
    """
    Obiekt Trojkat opisuje nam podstawowe wlasnosci trojkatow.
    
    Trojkaty to wielokaty o trzech bokach (a, b, c).
 
    Parameters
    ----------
    a: int or float
        trzyma wymiar a, ktory jest podstawa trojkata
    b: int or float
        trzyma wymiar b
    c: int or float
        trzyma wymiar c
        
    Attributes
    ----------
    a: tu przechowujemy informacje o parametrze a
    b: tu przechowujemy informacje o parametrze b
    c: tu przechowujemy informacje o parametrze c

    Examples
    --------
    >>> t = Trojkat(2, 5, 4)
    """

    def __init__(self, a, b, c):
        assert a > 0 and b > 0 and c > 0, "Wymiary bokow trojkata musza byc wieksze od 0"
        self.a = a
        self.b = b
        self.c = c

    def get_pole(self):
        """Zwraca pole trojkata"""
        h = self.get_wysokosc()
        p = (self.a * h)/2
        return p

    def get_obwod(self):
        """Zwraca obwod trojkata"""
        ob = self.a + self.b + self.c
        return ob

    def __gt__(self, other):
        """Magic method
        Sprawdza, czy obwod pierwszego trojkata
        jest wiekszy od obwodu innego trojkata"""

        first = self.get_obwod()
        second = other.get_obwod()
        
        if first > second:
            return True
        else:
            return False

    def czy_wiekszy_od(self, other):
        """Sprawdza, czy obwod pierwszego trojkata
        jest wiekszy od obwodu innego trojkata"""
        first = self.get_obwod()
        second = other.get_obwod()
        
        if first > second:
            return True
        else:
            return False

class TrojkatProstokatny(Trojkat):
    """
    Obiekt TrojkatProstokatny opisuje nam wlasnosci trojkatow prostokatnych.
    
    Trójkąt, w którym jeden z kątów wewnętrznych jest prosty.
    
    Parameters
    ----------
    a: int or float
        trzyma wymiar podstawy trojkata prostokatnego 
    b: int or float
        trzyma wymiar przyprostokatnej trojkata prostokatnego
    c: int or float
        trzyma wymiar przeciwprostokatnej trojkata prostokatnego
        
    Attributes
    ----------
    a: tu przechowujemy informacje o parametrze a
    b: tu przechowujemy informacje o parametrze b
    c: tu przechowujemy informacje o parametrze c
    
    Example
    -------
    >>> t1 = TrojkatProstokatny(4, 3, 5)
    >>> t1.get_wysokosc()
    3
    >>> t1.get_pole()
    6.0
    >>> t1.get_obwod()
    12
    """

    def __init__(self, a, b, c):
        Trojkat.__init__(self, a, b, c)
        assert a**2 + b**2 == c**2, "Podane wymiary nie tworza trojkata prostokatnego"

    def get_wysokosc(self):
        """Zwraca wysokosc trojkata"""
        return self.b


class TrojkatRownoboczny(Trojkat):
    """
    Obiekt TrojkatRownoboczny opisuje nam wlasnosci trojkatow rownobocznych.
    
    Trójkąt, w którym wszystkie boki sa rownej dlugosci.
    
    Parameters
    ----------
    a: int or float
        trzyma wymiar jednego z bokow trojkata rownobocznego
    b: int or float
        trzyma wymiar jednego z bokow trojkata rownobocznego
    c: int or float
        trzyma wymiar jednego z bokow trojkata rownobocznego
        
    Attributes
    ----------
    a: tu przechowujemy informacje o parametrze a
    b: tu przechowujemy informacje o parametrze b
    c: tu przechowujemy informacje o parametrze c
    
    Example
    -------
    >>> t2 = TrojkatRownoboczny(5, 5, 5)
    >>> t2.get_wysokosc()
    4.330127018922193
    >>> t2.get_pole()
    10.825317547305481
    >>> t2.get_obwod()
    15
    """
        
    def __init__(self, a, b, c):
        Trojkat.__init__(self, a, b, c)
        assert a == b == c, "Wszystkie boki musza byc rowne"

    def get_wysokosc(self):
        h = (self.a * sqrt(3)) / 2
        return h


class TrojkatRownoramienny(Trojkat):
    """
    Obiekt TrojkatRownoboczny opisuje nam wlasnosci trojkatow rownoramiennych.
    
    Trójkąt, ktory ma dwa boki (ramiona) o rownej dlugosci.
    
    Parameters
    ----------
    a: int or float
        trzyma wymiar podstawy trojkata rownoramiennego
    b: int or float
        trzyma wymiar jednego z bokow trojkata rownoramiennego
    c: int or float
        trzyma wymiar jednego z bokow trojkata rownoramiennego
        
    Attributes
    ----------
    a: tu przechowujemy informacje o parametrze a
    b: tu przechowujemy informacje o parametrze b
    c: tu przechowujemy informacje o parametrze c
    
    Example
    -------
    >>> t3 = TrojkatRownoramienny(8, 6, 6)
    >>> t3.get_wysokosc()
    4.47213595499958
    >>> t3.get_pole()
    17.88854381999832
    >>> t3.get_obwod()
    20
    """

    def __init__(self, a, b, c):
        Trojkat.__init__(self, a, b, c)
        assert b == c, "Ramiona musza byc rowne"

    def get_wysokosc(self):
        pitagoras = (self.c)**2 - (self.a / 2)**2
        h = sqrt(pitagoras)
        return h

# przyklady klas
t1 = TrojkatProstokatny(4, 3, 5)
t2 = TrojkatRownoboczny(10, 10, 10)
t3 = TrojkatRownoramienny(4, 6, 6)

# testy klas
print('obwod t1, t2, t3:\n', \
      t1.get_obwod(),'\n', t2.get_obwod(),'\n', t3.get_obwod())
print('pole t1, t2, t3:\n', \
      t1.get_pole(),'\n', t2.get_pole(),'\n', t3.get_pole())
print('wysokosc t1, t2, t3:\n', \
      t1.get_wysokosc(),'\n', t2.get_wysokosc(),'\n', t3.get_wysokosc())
print('t1>t2, t2>t3, t3>t1:\n', \
      t1 > t2, '\n', t2 > t3, '\n', t3 > t1)
print('czy_wiekszy_od:\n', \
      t1.czy_wiekszy_od(t2), '\n', t2.czy_wiekszy_od(t3), '\n', t3.czy_wiekszy_od(t1))
