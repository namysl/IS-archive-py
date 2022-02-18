#zad3 - Ewa Namysł


class Konto:

    def __init__(self, osoba, adres, pin, saldo):
        self.osoba = osoba
        self.adres = adres
        self.pin = pin
        self.saldo = saldo

    def wplata(self):
        podajpin = input("Podaj PIN: ")

        if int(podajpin) != self.pin:
            print("Nieprawidłowy PIN")
        else:
            print("OK")
            gotowka = int(input("Podaj kwotę do wpłaty: "))
            self.saldo += gotowka
            print("Saldo po operacji:", self.saldo) 

    def wyplata(self):
        podajpin = input("Podaj PIN: ")
        if int(podajpin) != self.pin:
            print("Nieprawidłowy PIN")
        else:
            print("OK")
            gotowka = int(input("Podaj kwotę do wypłacenia: "))
            if self.saldo >= gotowka:
                self.saldo -= gotowka
                print("Saldo po operacji:", self.saldo)
                
            else:
                print("Brak wystarczających środków")


konto1 = Konto('Igrek Iksiński', 'Katowicka 1, 11-111 Kalisz', 1111, 500)
konto2 = Konto('Iks Igrekowski', 'Kaliska 9, 99-999 Katowice', 9999, 10000)
