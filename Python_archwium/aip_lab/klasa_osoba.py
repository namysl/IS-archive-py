# zad 1, Ewa Namysł

class Osoba():

    def __init__(self, imie, nazwisko, pesel, rok_ur, plec):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.rok_ur = rok_ur
        self.plec = plec

    def podaj_dane(self):
        self.imie = input("Wpisz imię: ")
        self.nazwisko = input("Wpisz nazwisko: ")
        self.pesel = int(input("Wpisz pesel: "))
        self.rok_ur = int(input("Wpisz rok urodzenia: "))
        self.plec = input("Wpisz płeć: ")

    def wypisz_dane(self):
        dane_osoba = (self.imie, self.nazwisko, self.pesel, \
                      self.rok_ur, self.plec)
        return dane_osoba


class Student(Osoba):

    def __init__(self, imie, nazwisko, pesel, rok_ur, plec, nr_indeksu):
        super().__init__(imie, nazwisko, pesel, rok_ur, plec)
        self.nr_indeksu = nr_indeksu

    def podaj_nr_indeksu(self):
        self.nr_indeksu = int(input("Wpisz numer indeksu: "))

    def wypisz_dane(self):
        dane_student = (self.imie, self.nazwisko, self.pesel, \
                        self.rok_ur, self.plec, self.nr_indeksu)
        return dane_student


class Wykladowca(Osoba):

    def __init__(self, imie, nazwisko, pesel, rok_ur, plec, tytul):
        super().__init__(imie, nazwisko, pesel, rok_ur, plec)
        self.tytul = tytul

    def podaj_tytul(self):
        self.tytul = input("Wpisz tytuł lub stopień naukowy: ")

    def wypisz_dane(self):
        dane_wykladowca = (self.imie, self.nazwisko, self.pesel, \
                           self.rok_ur, self.plec, self.tytul)
        return dane_wykladowca


class Stypendysta(Student):

    def __init__(self, imie, nazwisko, pesel, rok_ur, plec, \
                 nr_indeksu, stypendium):
        super().__init__(imie, nazwisko, pesel, rok_ur, plec, nr_indeksu)
        self.stypendium = stypendium

    def podaj_stypendium(self):
        self.stypendium = float(input("Podaj kwotę stypendium: "))

    def wypisz_dane(self):
        dane_stypendysta = (self.imie, self.nazwisko, self.pesel, \
                            self.rok_ur, self.plec, self.nr_indeksu, self.stypendium)
        return dane_stypendysta



osoba1 = Osoba("Jan", "Kowalski", 93121211111, 1993, "M")
student1 = Student("Anna", "Nowak", 92111133333, 1992, "K", 292001)
wykladowca1 = Wykladowca("Robert", "Kowal", 79101044444, 1979, "M", "dr hab.")
stypendysta1 = Stypendysta("Katarzyna", "Nowakowska", 97020255555, 1997, "K", 311001, 497.98)
