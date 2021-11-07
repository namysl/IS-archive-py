def silnia_iter(n):
    if n == 0 or n == 1:
        return 1
    else:
        silnia = 1
        while n > 1:
            silnia *= n
            n -= 1
        return silnia

def HornerPochodna_iter(n, A, c, k):
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
    k_copy = k # trzyma poczatkowa wartosc k
    temp = []  # trzyma kolejne wartosci zmiennej wynik_horner

    if k == 0:  # jesli chcemy wartosc wielomianu
        k = n

    while k != 0:
        wynik_horner = A[-1]
        A.pop(-1)
        temp.append(wynik_horner)
        i = len(A) - 1
        while i != 0:
            wynik_horner = c * wynik_horner + A[i]
            temp.append(wynik_horner)
            i -= 1
        # ???
        # ten fragment nie ma sensu, zaprintowac kiedy k = 0, w innym przypadku byc musi
        # ???
        #wynik_horner = c* wynik_horner + A[i]  # jesli k bylo rozne od 0
        print('wynik horner:', wynik_horner)
        print('temp:', temp)
        print('~~~~')

        temp.reverse()  # odwraca wyniki, aby w kolejnej petli obliczac w poprawnej kolejnosci
        A = temp[:]  # kopiuje tymczasowa liste do A
        temp.clear()  # czysci tymczasowa liste,
        k -= 1

    print('horner po petli:', wynik_horner)
    print('input k:', k_copy)
    if k_copy == 0:
        wynik_horner *= silnia_iter(n)
        print('silnia:', silnia_iter(n))

    return wynik_horner

n1 = 3
A1 = [3, -4, 2, -2]
c1 = -1
k1 = 0

#print(HornerPochodna_iter(n1, A1, c1, 0))


def pochodna_Hornerek(n, A, c, k):
    pochodne = []
    n_copy = n

    if k == 0:  # wartosc wielomianu
        wynik = A[-1]
        while n > 0:
            wynik = c * wynik + A[n-1]
            n -= 1
        return wynik

    else: # k-ta pochodna

        x = 1
        while x != k+1:
            print('\nPIERWSZA CZESC:')

            temp = []
            wynik = A[-1]
            temp.append(wynik)

            i = len(A) - 1
            while i != 1:
                wynik = c * wynik + A[i-1]
                temp.append(wynik)
                i -= 1

            print('2) temp:', temp)



            print('\nDRUGA CZESC:')

            wynik2 = temp[0]
            print('4) wynik2:', wynik2)
            for i in range(1, len(temp)):
                print('5) c:', c, 'wynik2:', wynik2, 'temp[i]:', temp[i])
                wynik2 = wynik2 * c + temp[i]
                print('6) wynik2:', wynik2)

            wynik2_silnia = wynik2 * silnia_iter(x)
            pochodne.append(wynik2_silnia)
            print('7) silnia:', silnia_iter(x))
            print('8) wynik2silnia:', wynik2_silnia)

            x += 1
            temp.reverse()
            A = temp[:]
            print('3) temp rev:', temp)



        return 'pochodne return', pochodne


print(pochodna_Hornerek(n1, A1, c1, 3))  # wartosc wielomianu = 11
