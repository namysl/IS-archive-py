#zad 2 - Ewa Namysł


class Adres:

    def __init__(self, imie, nazw, ulica, numdom, nummiesz, kod, miasto, kraj):
        self.imie = imie
        self.nazw = nazw
        self.ulica = ulica
        self.numdom = numdom
        self.nummiesz = nummiesz
        self.kod = kod
        self.miasto = miasto
        self.kraj = kraj

    def wypisz(self):

        dane = "{} {} ~ ul. {} {}/{} ~ {} {} ~ {}".format(self.imie, self.nazw, self.ulica, self.numdom, self.nummiesz, self.kod, self.miasto, self.kraj)
        return dane


    def zmien(self):

        #mało wygodne
        print("Co chcesz zmienić? Wybierz i wprowadź:")
        print("1-imię, 2-nazwisko, 3-ulicę, 4-numer domu, 5-numer mieszkania, 6-kod pocztowy, 7-miasto, 8-kraj")
        x = int(input())

        if x == 1:
            self.imie = input("Podaj nowe imię: ")
        elif x == 2:
            self.nazw = input("Podaj nowe nazwisko: ")

        #itd
                
        else:
            print("Błędny kod")


adres1 = Adres("Igrek", "Iksiński", "Tierieszkowej", "1", "1", "11-111", "Mikołów", "Polska")
