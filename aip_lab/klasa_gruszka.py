class Gruszka:
    '''
    Obiekt Gruszka opisuje nam wlasnosci gruszek.
 
    Args:
        odmiana (str): trzyma odmiane owocu 
        waga (num): trzyma wage gruszek
        smak (str): opisuje smak gruszek (slodki, kwasny, itd.)
 
    Attributes:
        odmiana: tu przechowujemy informacje o odmianie 
        waga: tu przechowujemy informacje o wadze
        smak: tu przechowujemy informacje o smaku
    '''
    
    def __init__(self, odmiana, waga, smak):
        self.odmiana = odmiana
        self.waga = waga
        self.smak = smak
        

class Orzech:
    '''
    Obiekt Orzech opisuje wlasnosci orzechow.

    Args:
        odmiana (str): trzyma odmiane orzecha
        rozmiar (num): trzyma rozmiar orzecha
        cena (num): trzyma cene orzecha

    Attributes:
        odmiana: tu przechowujemy informacje o odmianie
        rozmiar: tu przechowujemy informacje o rozmiarze
        cena: tu przechowujemy informacje o cenie
    '''
    
    def __init__(self, odmiana, rozmiar, cena):
        self.odmiana = odmiana
        self.rozmiar = rozmiar
        self.cena = cena

class Motor:
    '''
    Obiekt Motor opisuje wlasnosci motorow.

    Args:
        marka (str): trzyma marke motoru
        pojemnosc (num): trzyma pojemnosc motoru
        kolor (str): trzyma kolor motoru
        KM (int): trzyma KM motoru

    Attributes:
        marka: tu przechowujemy informacje o marce
        pojemnosc: tu przechowujemy informacje o pojemnosci
        kolor: tu przechowujemy informacje o kolorze
        KM: tu przechowujemy informacje o KM
    '''

    def __init__(self, marka, pojemnosc, kolor, KM):
        self.marka = marka
        self.pojemnosc = pojemnosc
        self.kolor = kolor
        self.KM = KM

class Kot:
    '''
    Obiekt Kot opisuje wlasnosci kotow.

    Args:
        rasa (str): trzyma rase kota
        umaszczenie: trzyma umaszczenie kota
        imie: trzyma imie kota

    Attributes:
        rasa: tu przechowujemy informacje o rasie
        umaszczenie: tu przechowujemy informacje o umaszczeniu
        imie: tu przechowujemy informacje o imieniu
    '''
    
    def __init__(self, rasa, umaszczenie, imie):
        self.rasa = rasa
        self.umaszczenie = umaszczenie
        self.imie = imie

class Ksiazka:
    '''
    Obiekt Ksiazka opisuje wlasnosci ksiazek.

    Args:
        tytul: trzyma tytul ksiazki
        autor: trzyma autora ksiazki
        rok_wydania: trzyma rok wydania ksiazki
        oprawa: trzyma oprawe ksiazki
        ISBN: trzyma ISBN ksiazki
        cena: trzyma cene ksiazki
        kategoria: trzyma kategorie ksiazki
        wydawnictwo: trzyma wydawnictwo ksiazki

    Attributes:
        tytul: tu przechowujemy informacje o tytule
        autor: tu przechowujemy informacje o autorze
        rok_wydania: tu przechowujemy informacje o roku wydania
        oprawa: tu przechowujemy informacje o oprawie
        ISBN: tu przechowujemy informacje o ISBN
        cena: tu przechowujemy informacje o cenie
        kategoria: tu przechowujemy informacje o kategorii
        wydawnictwo: tu przechowujemy informacje o wydawnictwie
    '''
    def __init__(self, tytul, autor, rok_wydania, oprawa, \
                 ISBN, cena, kategoria, wydawnictwo):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.oprawa = oprawa
        self.ISBN = ISBN
        self.cena = cena
        self.kategoria = kategoria
        self.wydawnictwo = wydawnictwo
