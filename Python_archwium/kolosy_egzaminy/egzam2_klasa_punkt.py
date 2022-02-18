class Punkt:
    """Obiekt Punkt opisuje nam podstawowe wlasnosci punktu.

    Parameters
    ----------
    x: float
        trzyma x opisujacy osie odcietych
    y: float
        trzyma y opisujacy osie rzednych

    Attributes
    ----------

    x: tu przechowujemy informacje o parametrze x
    y: tu przechowujemy informacje o parametrze y

    Examples
    --------
    >>> p = Punkt(1.5, 12.5)
    >>> print(p)
    Punkt (2.0, 3.0)

    """
    def __init__(self, x=0.0, y=0.0):
        assert isinstance(x, float), 'osie odcietych musza byc typu float'
        assert isinstance(y, float), 'osie rzednych musza byc typu float'
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def set_x(self, new):
        assert isinstance(new, float)
        self.x = new

    def get_y(self):
        return self.y

    def set_y(self, new):
        assert isinstance(new, float)
        self.y = new

    def __repr__(self):
        return str('Punkt ({}, {})').format(self.x, self.y)

    def __str__(self):
        return str('Punkt ({}, {})').format(self.x, self.y)


class RuchomyPunkt(Punkt):
    """Obiekt Ruchomy Punkt opisuje nam podstawowe wlasnosci ruchomych punktow.

    Parameters
    ----------
    x: float
        trzyma x opisujacy osie odcietych
    y: float
        trzyma y opisujacy osie rzednych
    v_x: float
        trzyma v_x opisujacy predkosc punktu x
    v_y: float
        trzyma v_y opisujacy predkosc punktu y

    Attributes
    ----------
    x: tu przechowujemy informacje o parametrze x
    y: tu przechowujemy informacje o parametrze y
    v_x: tu przechowujemy informacje o parametrze v_x
    v_y: tu przechowujemy informacje o parametrze v_y

    Examples
    --------
    >>> rp = RuchomyPunkt(8.8, 1.0, 12.5, 0.6)
    >>> rp.oblicz_wek_predkosci()
    156.61
    """
    def __init__(self, x, y, v_x=0.0, v_y=0.0):
        super().__init__(x, y)

        assert isinstance(v_x, float), 'szybkosc x musi byc typu float'
        assert isinstance(v_y, float), 'szybkosc y musi byc typu float'
        self.v_x = v_x
        self.v_y = v_y

    def get_v_x(self):
        return self.v_x

    def set_v_x(self, new):
        assert isinstance(new, float)
        self.v_x = new

    def get_v_y(self):
        return self.v_y

    def set_v_y(self, new):
        assert isinstance(new, float)
        self.v_y = new

    def __repr__(self):
        return str('Ruchomy Punkt ({}, {}) o predkosci ({}, {})').format(self.x, self.y, self.v_x, self.v_y)

    def __str__(self):
        return str('Ruchomy Punkt ({}, {}) o predkosci ({}, {})').format(self.x, self.y, self.v_x, self.v_y)

    def wektor_predkosci(self):
        v = (self.v_x, self.v_y)
        return v

    def oblicz_wek_predkosci(self):
        v2 = self.v_x ** 2 + self.v_y ** 2
        return v2


punkt1 = Punkt(2.0, 3.0)
print(punkt1.get_x())

# assertion error, musi byc float:
# punkt1.set_x(2)

print(punkt1.get_x())
print(punkt1)

ruchpunkt1 = RuchomyPunkt(12.5, 1.5)
print(ruchpunkt1)

ruchpunkt1.set_v_x(1.3)
ruchpunkt1.set_v_y(2.3)

print(ruchpunkt1)
print(ruchpunkt1.wektor_predkosci())
print(ruchpunkt1.oblicz_wek_predkosci())
