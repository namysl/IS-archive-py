#zad6

def nie_przez_zero(liczba1, liczba2):
    try:
        x = int(liczba1) / int(liczba2)
        print(x)
    except ZeroDivisionError:
        x = 0
        print("Nie można dzielić przez 0")

#zad7

class Error(Exception):
    pass

class Jednocyfr(Error):
    pass

def jednocyfr():
    while True:
        try:
            x = int(input("Podaj liczbę: "))
            if x > 9 or x < -9:
                raise Jednocyfr
            break
        except Jednocyfr:
            print("Liczba nie jest jednocyfrowa")
    print("OK")
