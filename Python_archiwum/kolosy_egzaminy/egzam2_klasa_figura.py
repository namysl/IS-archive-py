class Ksztalt:
    """Obiekt Ksztalt opisuje nam podstawowe wlasnosci ksztaltow

        Parameters
        ----------
        lokacja: tuple
            trzyma lokacja

        Attributes
        ----------
        lokacja: tu przechowujemy informacje o parametrze lokacja

        Examples
        >>> k1 = Ksztalt((0.0, 0.0))
        >>> print(k1)
        Lokacja klasy Ksztalt: (0.0, 0.0)
        --------

        """
    def __init__(self, lokacja=(0.0, 0.0)):
        self.lokacja = lokacja

    def __str__(self):
        return str('Lokacja klasy Ksztalt: {}').format(self.lokacja)

    def __repr__(self):
        return 'instancja klasy' + __class__.__name__

    def pole(self):
        raise NotImplemented("Funkcja pole nie zostala zaimplementowana")

    def obwod(self):
        raise NotImplemented("Funkcja pole nie zostala zaimplementowana")


class Prostokat(Ksztalt):
    """Obiekt Prostokat opisuje nam podstawowe wlasnosci prostokatow

        Parameters
        ----------
        lokacja: tuple
            trzyma lokacja
        bok_a: float
            trzyma bok_a
        bok_b: float
            trzyma bok_b

        Attributes
        ----------
        lokacja: tu przechowujemy informacje o parametrze lokacja
        bok_a: tu przechowujemy informacje o parametrze bok_a
        bok_b: tu przechowujemy informacje o parametrze bok_b

        Examples
        --------
        >>> k2 = Prostokat((1, 1), 5, 5)
        >>> print(k2.obwod())
        20.0
        """
    def __init__(self, lokacja, bok_a, bok_b):
        super().__init__(lokacja)

        assert isinstance(bok_a, float)
        assert isinstance(bok_b, float)
        self.bok_a = bok_a
        self.bok_b = bok_b

    def get_bok_a(self):
        return self.bok_a

    def set_bok_a(self, new):
        assert isinstance(new, float)
        self.bok_a = new

    def get_bok_b(self):
        return self.bok_b

    def set_bok_b(self, new):
        assert isinstance(new, float)
        self.bok_b = new

    def pole(self):
        """Oblicza pole prostokata"""
        pole = self.bok_a * self.bok_b
        return pole

    def obwod(self):
        """Oblicza obwod prostokata"""
        obwod = 2 * self.bok_a + 2 * self.bok_b
        return obwod

class Kolo(Ksztalt):
    """Obiekt Ksztalt opisuje nam podstawowe wlasnosci ksztaltow

        Parameters
        ----------
        lokacja: tuple
            trzyma lokacja
        promien: float
            trzyma promien

        Attributes
        ----------
        lokacja: tu przechowujemy informacje o parametrze lokacja
        promien: tu przechowujemy informacje o parametrze promien

        Examples
        --------
        >>> k3 = Kolo((0, 0), 10.0)
        >>> print(k3.pole())
        314.0
        """

    def __init__(self, lokacja, promien):
        super().__init__(lokacja)

        assert isinstance(promien, float)
        self.promien = promien

    def get_promien(self):
        return self.promien

    def set_promien(self, new):
        assert isinstance(new, float)
        self.promien = new

    def pole(self):
        """Oblicza pole kola"""
        pole = 3.14 * self.promien ** 2
        return pole

    def obwod(self):
        """Oblicza obwod kola"""
        obwod = 2 * 3.14 * self.promien
        return obwod


ksz1 = Ksztalt((2.0, 3.0))
print(ksz1)

pros1 = Prostokat((1, 1), 20.0, 10.0)
print(pros1)
print(pros1.get_bok_b())
print(pros1.pole())

kolo1 = Kolo((2, 2), 20.5)
print(kolo1.obwod())
print(kolo1.pole())
kolo1.set_promien(36.0)
