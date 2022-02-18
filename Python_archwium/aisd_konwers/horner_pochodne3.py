def silnia_iter(n):
    if n == 0 or n == 1:
        return 1
    else:
        silnia = 1
        while n > 1:
            silnia *= n
            n -= 1
        return silnia


# iteracyjnie
def HornerPochodne(n, A, c, k):
    """
    n = stopien wielomianu

    A = lista zawierajaca wspolczynniki wielomianu
        A[0...n], czyli A[0] = a0, A[1] = a1 itd.

    c = podana liczba rzeczywista

    k = 0...n
        jesli k = 0 -> zwroc wartosc wielomianu
        jesli k > 0 -> oblicza tylko k-ta pochodna danego wielomianu w punkcie c

    output -> wartosci zwracane do listy o dlugosci n+1
    """
    lista_pochodne = []

    if k == 0:  # wartosc wielomianu
        wynik = A[-1]
        while n > 0:
            wynik = c * wynik + A[n-1]
            n -= 1
        return wynik

    else:  # k-ta pochodna
        x = 1
        while x != k+1:  # od 1 do k+1, k od 0
            temp = []  # wartosci z kolejnych iteracji Hornera
            wynik = A[-1]
            temp.append(wynik)

            i = len(A) - 1
            while i != 1:
                wynik = c * wynik + A[i-1]
                temp.append(wynik)
                i -= 1

            wynik_q = temp[0]  # wartosci z obliczania q
            for i in range(1, len(temp)):
                wynik_q = wynik_q * c + temp[i]

            pochodna_silnia = wynik_q * silnia_iter(x)
            lista_pochodne.append(pochodna_silnia)

            x += 1

            temp.reverse()  # odwraca wyniki listy temp, aby ich uzyc w kolejnej iteracji
            A = temp[:]

        return lista_pochodne[-1]  # wartosc k-tej pochodnej bedzie ostatnia na liscie


n1 = 3
A1 = [3, -4, 2, -2]
c1 = -1

print(HornerPochodne(n1, A1, c1, 0))  # wartosc wielomianu = 11
print(HornerPochodne(n1, A1, c1, 3))  # trzecia pochodna

n2 = 4
A2 = [-9, -4, 0, -6, 3]
c2 = 3

print(HornerPochodne(n2, A2, c2, 0))  # = 60
print(HornerPochodne(n2, A2, c2, 4))