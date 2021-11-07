# zad 2, Ewa Namysł

class Lodz():
    def __init__(self, nazwa, nr_eni, rok_wodowania, dlugosc):
        self.nazwa = nazwa
        self.nr_eni = nr_eni
        self.rok_wodowania = rok_wodowania
        self.dlugosc = dlugosc

    def wypisz(self):
        dane_lodz = "nazwa: {}, nr ENI: {}, rok wodowania: {}, długość: {} m".format( \
            self.nazwa, self.nr_eni, self.rok_wodowania, self.dlugosc)
        print(dane_lodz)

    def wpisz(self):
        self.nazwa = input("Wpisz nazwę łodzi: ")
        self.nr_eni = int(input("Wpisz numer ENI: "))
        self.rok_wodowania = int(input("Wpisz rok wodowania: "))
        self.dlugosc = float(input("Wpisz długość kadłuba [m]: "))

    def zmien(self):
        print("Co chcesz zmienić? Wybierz i wprowadź:")
        print("1-nazwę, 2-nr ENI, 3-rok wodowania, 4-długość")
        x = int(input())

        if x == 1:
            self.nazwa = input("Podaj nową nazwę: ")
        elif x == 2:
            self.nr_eni = int(input("Podaj nowy nr ENI: "))
        elif x == 3:
            self.rok_wodowania = int(input("Podaj rok: "))
        elif x == 4:
            self.nr_eni = float(input("Podaj długość kadłuba [m]: "))
        else:
            print("Błędny kod")



class Pojazd():
    def __init__(self, nr_rejestr, nr_vim, marka, rok_produk, waga):
        self.nr_rejestr = nr_rejestr
        self.nr_vim = nr_vim
        self.marka = marka
        self.rok_produk = rok_produk
        self.waga = waga

    def wypisz(self):
        dane_pojazd = "nr rejestr.: {}, nr VIM: {}, marka: {}, rok produkcji: {}, waga: {} kg".format( \
            self.nr_rejestr, self.nr_vim, self.marka, self.rok_produk, self.waga)
        print(dane_pojazd)

    def wpisz(self):
        self.nr_rejestr = input("Wpisz numer rejestracyjny: ")
        self.nr_vim = input("Wpisz numer VIM: ")
        self.marka = input("Wpisz markę: ")
        self.rok_produk = int(input("Wpisz rok produkcji: "))
        self.waga = int(input("Wpisz wagę całkowitą [kg]: "))


    def zmien(self):
        print("Co chcesz zmienić? Wybierz i wprowadź:")
        print("1-nr rejestracyjny, 2-nr VIM, 3-markę, 4-rok produkcji, 5-wagę")
        x = int(input())

        if x == 1:
            self.nr_rejestr = input("Podaj nowy numer: ")
        elif x == 2:
            self.nr_vim = input("Podaj nr VIM: ")
        elif x == 3:
            self.marka = input("Podaj markę: ")
        elif x == 4:
            self.rok_produkcji = int(input("Podaj rok: "))
        elif x == 5:
            self.waga = int(input("Podaj wagę [kg]: "))
        else:
            print("Błędny kod")


        
class Amfibia(Lodz, Pojazd):
    def __init__(self, nazwa, nr_eni, rok_wodowania, dlugosc, nr_rejestr, nr_vim, marka, rok_produk, waga):
        Lodz.__init__(self, nazwa, nr_eni, rok_wodowania, dlugosc)
        Pojazd.__init__(self, nr_rejestr, nr_vim, marka, rok_produk, waga)



a1 = Amfibia(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(Amfibia.__mro__) #mro klasy Amfibia

"""
Zgodnie z Method Resolution Order, metoda bedzie poszukiwana najpierw
wewnatrz klasy dziecka (w tym przypadku Amfibia). Jesli jej tam nie znajduje,
zaczyna szukac w klasie pierwszego rodzica (Lodz ma taka metode, wiec jej uzywa).
Jesli pierwszy rodzic nie posiada metody o podanej nazwie, to poszukiwania
przechodza do klasy kolejnego rodzica itd.
"""

a1.wypisz() #uzywa metody z klasy Lodz (pierwszy rodzic)
