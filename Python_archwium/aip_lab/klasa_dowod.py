#zad1 - Ewa Namysł

import datetime

class Osoba:

    def __init__(self, imie, nazwisko, data_ur, miejsc_ur, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_ur = data_ur
        self.miejsc_ur = miejsc_ur
        self.pesel = pesel


    def wypisz_dane(self):
        dane = (self.imie, self.nazwisko, self.data_ur, self.miejsc_ur, self.pesel, self.data_waznosci())
        return dane


    def zmiana_nazwiska(self):
        self.nazwisko = input("Podaj nowe nazwisko: ")


    def data_waznosci(self):
        dzisiaj = datetime.date.today()
        waznosc = str(dzisiaj.year + 10) + '.' + str(dzisiaj.month) + '.' + str(dzisiaj.day)
        return waznosc


    def sprawdz_pesel(self):
        self.pesel = str(self.pesel)
        if len(self.pesel) < 11:
            print("Numer pesel jest zbyt krótki")
        elif len(self.pesel) > 11:
            print("Numer pesel jest zbyt długi")
        else:
            print("Sprawdzam poprawność numeru pesel")

        lista = [int(x) for x in str(self.pesel)]
        wynik = 1*lista[0] + 3*lista[1] + 7*lista[2] + 9*lista[3] + 1*lista[4] + 3*lista[5] + 7*lista[6] + 9*lista[7] + 1*lista[8] + 3*lista[9]

        lista2 = [int(x) for x in str(wynik)]
        sprawdz = abs((lista2[-1]) - 10)

        if int(sprawdz) == int(self.pesel[-1]):
            print("Pesel prawidłowy")
        else:
            print("Pesel nie jest prawidłowy")


osoba1 = Osoba("Igrek", "Iksiński", "1993-10-10", "Zakopane", "93101011123")
