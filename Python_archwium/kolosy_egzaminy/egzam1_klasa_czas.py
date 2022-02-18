class WrongSeconds(Exception):
    """Wyjatek obslugujacy klase Czas"""
    def __init__(self, blad):
        self.blad = blad

    def __str__(self):
        info = "Wartosc wieksza lub rowna 60, podana wartosc: {}".format(self.blad)
        return info


class WrongMinutes(Exception):
    """Wyjatek obslugujacy klase Czas"""
    def __init__(self, blad):
        self.blad = blad

    def __str__(self):
        info = "Wartosc wieksza lub rowna 60, podana wartosc: {}".format(self.blad)
        return info


class Czas:
    """
    Obiekt Czas opisuje nam podstawowe wlasnosci czasu.

    Parameters
    ----------
    dzien: int
        trzyma dzien
    godzina: int
        trzyma godzine
    minuta: int
        trzyma minute
    sekunda: int
        trzyma sekunde

    Attributes
    ----------
    dzien: tu przechowujemy informacje o parametrze dzien
    godzina: tu przechowujemy informacje o parametrze godzina
    minuta: tu przechowujemy informacje o parametrze minuta
    sekunda: tu przechowuje informacje o parametrze sekunda

    Examples
    --------
    >>> time1 = Czas(0, 15, 20, 59)
    >>> time2 = Czas(0, 1, 1, 1)
    >>>time1 + time2
    '16h 22m 0s'
    >>>print(time1)
    15:20:59, dzien bez zmiany
    """

    def __init__(self, godzina, minuta, sekunda, dzien=0):
        self.godzina = godzina

        if minuta >= 60:
            raise WrongMinutes(minuta)
        else:
            self.minuta = minuta

        if sekunda >= 60:
            raise WrongSeconds(sekunda)
        else:
            self.sekunda = sekunda

        self.dzien = dzien

    def get_godzina(self):
        return self.godzina

    def get_minuta(self):
        return self.minuta

    def get_sekunda(self):
        return self.sekunda

    def get_dzien(self):
        return self.dzien

    def set_godzina(self, nowagodzina):
        self.godzina = nowagodzina

    def set_minuta(self, nowaminuta):
        self.minuta = nowaminuta

    def set_sekunda(self, nowasekunda):
        self.sekunda = nowasekunda

    def set_dzien(self, nowydzien):
        self.dzien = nowydzien

    def __add__(self, other):
        self.sekunda += other.sekunda
        self.minuta += other.minuta
        self.godzina += other.godzina
        self.dzien += other.dzien

        if self.sekunda > 59:
            self.minuta += 1
            self.sekunda -= 60

        if self.minuta > 59:
            self.godzina += 1
            self.minuta -= 60

        if self.godzina > 23:
            self.dzien += 1
            self.godzina -= 24

        return self

    def __lt__(self, other):
        if self.dzien < other.dzien:
            return True
        elif self.dzien == other.dzien:
            if self.godzina < other.godzina:
                return True
            elif self.godzina == other.godzina:
                if self.minuta < other.minuta:
                    return True
                elif self.minuta == other.minuta:
                    if self.sekunda < self.sekunda:
                        return True
                    elif self.sekunda == self.sekunda:
                        print("sa rowne")
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __str__(self):
        hour = self.godzina
        minute = self.minuta
        second = self.sekunda

        if self.dzien == 0:
            day = "dzien bez zmiany"
        elif self.dzien < 1:
            day = "dzien poprzedni"
        else:
            day = "dzien następny"

        if self.godzina < 10:
            hour = "0{}".format(self.godzina)
        if self.minuta < 10:
            minute = "0{}".format(self.minuta)
        if self.sekunda < 10:
            second = "0{}".format(self.sekunda)

        return "{}:{}:{}, {}".format(hour, minute, second, day)

    def strefa1(self, miasto):
        warszawa = 1
        londyn = 0
        nowyjork = -5
        tokio = 9
        sydnej = 10
        moskwa = 3
        losangeles = -8

        if miasto == "Warszawa":
            miasto = warszawa
        elif miasto == "Londyn":
            miasto = londyn
        elif miasto == "Nowy Jork":
            miasto = nowyjork
        elif miasto == "Tokio":
            miasto = tokio
        elif miasto == "Sydnej":
            miasto = sydnej
        elif miasto == "Moskwa":
            miasto = moskwa
        elif miasto == "Los Angeles":
            miasto = losangeles
        else:
            return "Błąd lub brak miasta"

        if self.godzina == 0:
            self.godzina = 24
        newhour = self.godzina + miasto

        if newhour > 23:
            newhour -= 24

        if newhour < 0:
            newhour = 24 - abs(newhour)

        newtime = "{}:{}:{}".format(newhour, self.minuta, self.sekunda)
        return newtime

    def strefa2(self, miasto):
        cities = {"Warszawa": 1, "Londyn": 0, "Nowy Jork": -5, "Tokio": 9,
                  "Sydnej": 10, "Moskwa": 3, "Los Angeles": -8}

        for key in cities.keys():
            if miasto == key:
                wartosc = cities.get(miasto)
            else:
                continue

        if self.godzina == 0:
            self.godzina = 24
        newhour = self.godzina + miasto

        if newhour > 23:
            newhour -= 24

        if newhour < 0:
            newhour = 24 - abs(newhour)

        newtime = "{}:{}:{}".format(newhour, self.minuta, self.sekunda)
        return newtime

    def strefa3(self, miasto):
        cities = {"Warszawa": 1, "Londyn": 0, "Nowy Jork": -5, "Tokio": 9,
                  "Sydnej": 10, "Moskwa": 3, "Los Angeles": -8}

        wartosc = cities.get(miasto)
        if self.godzina == 0:
            self.godzina = 24
        newhour = self.godzina + miasto

        if newhour > 23:
            newhour -= 24

        if newhour < 0:
            newhour = 24 - abs(newhour)

        newtime = "{}:{}:{}".format(newhour, self.minuta, self.sekunda)
        return newtime


# testy:
# t = Czas(1, 11, 60, 59)  # wyjatek
t = Czas(0, 11, 2, 59)
print(t)  # __str__

time1 = Czas(0, 15, 20, 59)
time2 = Czas(0, 1, 1, 1)

print(time1 + time2)  # __add__
print(time1 < time2)  # __lt__
