#zad 3, Ewa Namysł

class CialoNiebieskie():
    def __init__(self, nazwa, masa, opis):
        self.nazwa = nazwa
        self.masa = masa
        self.opis = opis

    def zwrot_info(self):
        print("nazwa:", self.nazwa, "\nmasa:", self.masa)

    def zwrot_opis(self):
        print("opis:", self.opis)


class Planeta(CialoNiebieskie):
    def __init__(self, nazwa, masa, opis, obieg, rotacja, ciezar):
        super().__init__(nazwa, masa, opis)
        self.obieg = obieg
        self.rotacja = rotacja
        self.ciezar = ciezar

    def zwrot_info(self):
        print("nazwa:", self.nazwa, "\nmasa:", self.masa, \
              "\nobieg wokół Słońca:", \
              self.obieg, "\nczas rotacji wokół osi:", self.rotacja, \
              "\nile razy cięższe od Ziemi:", self.ciezar)


class Slonce(CialoNiebieskie):
    def __init__(self, nazwa, masa, opis, klasa, podklasa, ciezar):
        super().__init__(nazwa, masa, opis)
        self.klasa = klasa
        if podklasa not in [i for i in range (1, 10)]:
            raise PodklasaError(podklasa)
        else:
            self.podklasa = podklasa
        self.ciezar = ciezar

    def zwrot_info(self):
        print("nazwa:", self.nazwa, "\nmasa:", self.masa, \
            "\nklasa:", self.klasa, "\npodklasa:", self.podklasa, \
            "\nile razy cięższe od Słońca:", self.ciezar)


class PodklasaError(Exception):
    def __init__(self, podkl):
        self.podkl = podkl
    def __str__(self):
        info = "Wartość spoza zakresu od 1 do 9, wprowadzona wartość:" + " " + str(self.podkl)
        return info
    
cn1 = CialoNiebieskie("Księżyc", "7,347 673 * 10^22", \
                      "Naturalny satelita Ziemi")
p1 = Planeta("Wenus", "4,867 * 10^24", "Planeta skalista", \
             "224,701 dni", 2.143, 0.0534)
s1 = Slonce("Taygeta", "21.232 * 10^43", "gromada Plejad", "B", 5, 6.0)
s2 = Slonce("Alkione", "11.9834 * 10^30", "gwiazdozbiór Byka", "B", -12, 5.9)
