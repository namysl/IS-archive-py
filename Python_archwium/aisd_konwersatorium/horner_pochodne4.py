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
def HornerPochodne2(n, A, c, k):
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
        wynik = A[0]

        i = 1
        while i != n+1:
            wynik = c * wynik + A[i]
            i += 1
        return wynik

    else: # k-ta pochodna
        x = 1
        while x != k+1:
            temp = []  # wartosci z kolejnych iteracji Hornera
            wynik = A[0]
            temp.append(wynik)

            i = 1
            while i != n:
                wynik = c * wynik + A[i]
                temp.append(wynik)
                i += 1

            wynik_q = temp[0]  # wartosci z obliczania q
            j = 1
            while j < len(temp):
                wynik_q = wynik_q * c + temp[j]
                j += 1

            pochodna_silnia = wynik_q * silnia_iter(x)
            lista_pochodne.append(pochodna_silnia)

            x += 1
            n -= 1
            A = temp[:]

        return lista_pochodne[-1]  # wartosc k-tej pochodnej bedzie ostatnia na liscie


n1 = 3
A2 = [-2, 2, -4, 3]
c1 = -1

print(HornerPochodne2(n1, A2, c1, 0))  # wartosc wielomianu = 11
print(HornerPochodne2(n1, A2, c1, 3))  # trzecia pochodna

n2 = 4
A2 = [3, -6, 0, -4, -9]
c2 = 3

print(HornerPochodne2(n2, A2, c2, 0))  # = 60
print(HornerPochodne2(n2, A2, c2, 4))