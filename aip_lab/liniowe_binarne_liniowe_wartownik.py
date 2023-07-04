# Wyszukiwanie: liniowe, binarne, liniowe z wartownikiem 

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
LL = [3, 11, 15, 33, 45, 60, 90, 111, 133, 656, 890, 999, 1000]
LLL = [2, 4, 8, 16, 32, 64, 128]

def liniowe(lista, szukany_el):
    '''Szuka danego elementu porownujac z kazdym elementem listy (nie musi
    byc posortowana).

    W najgorszym przypadku zlozonosc obliczeniowa wyszukiwania
    liniowego wynosi O(n), gdzie n jest liczba elementow w danej liscie.
    Wowczas poszukiwany element znajduje sie na samym koncu listy
    (lub nie ma go w niej wcale), a algorytm musi dokonac porownania
    z kazdym elementem listy, zanim odnajdzie ten, ktorego szukamy.'''

    indeks = 0 # indeks elementu w liscie 
    liczba_indeksow = len(lista) - 1 # ilosc dostepnych w liscie indeksow

    while True:
        if lista[indeks] == szukany_el: # element listy jest elementem poszukiwanym
            return ('znaleziono poszukiwany element w liscie pod indeksem: {}'
                    .format(indeks))
        else: # przypadek indeks > liczba_indeksow: wartosc indeks wykracza poza liste
            return 'nie znaleziono poszukiwanego elementu'
        indeks += 1 # inkrementacja indeks


def binarne(lista, szukany_el):
    '''Porownuje szukany element ze srodkowa wartoscia listy, nastepnie
    w zaleznosci od tego, czy element byl wiekszy lub mniejszy, dzieli
    liste na coraz mniejsze przedzialy w ktorych dokonuje kolejnych porownan.
    Algorytm powtarza sie do momentu odnalezienia elementu.
    Lista musi byc wczesniej posortowana.

    Pesymistyczna zlozonosc wynosi O(log n), gdzie n to liczba elementow
    w liscie, czyli robi log n porownan w celu odnalezienia danego elementu.
    Przykladem jest brak poszukiwanego elementu w liscie,
    lista jest dzielona na coraz mniejsze czesci, a za kazdym razem
    dokonywane sa porownania, aby ostatecznie stwierdzic, ze element nie znajduje sie
    w danej liscie. '''
    
    srodek = len(lista) // 2 # wyznaczenie srodka listy
    lewa = lista[:srodek] # przedzial listy od pierwszego elementu do srodkowego
    prawa = lista[srodek+1:] # przedzial listy od nastepnego elementu po srodkowym
                            # do ostatniego elementu listy

    if len(lista) != 0: # jesli lista nie jest pusta
        if szukany_el == lista[srodek]: # szukany element jest srodkowym elementem listy
            return 'znaleziono podany element'

        elif szukany_el > lista[srodek]: # szukany element jest wiekszy od srodkowego el listy
            # rekurencja z prawa czescia listy jako argumentem
            return binarne(prawa, szukany_el) 
    
        elif szukany_el < lista[srodek]: # szukany element jest mniejszy srodkowego el listy
            # rekurencja z lewa czescia listy jako argumentem
            return binarne(lewa, szukany_el) 
    else: # w liscie nie ma szukanego elementu
        return 'nie znaleziono podanego elementu'

def liniowe_wartownik(lista, szukany_el):
    '''Szukana wartosc umieszczana jest na koncu listy jako wartownik'''
    lista = lista[:] # kopia listy, aby oryginalna nie byla modyfikowana

    lista.append(szukany_el) # dodajemy poszukiwany element na sam koniec listy
    indeks = 0 # indeks elementow

    while True:
        if lista[indeks] != szukany_el: # jesli wartosc listy pod tym indeksem nie jest poszukiwanym elementem
            indeks += 1 # inkrementacja
        else: # znajduje poszukiwany element
            if indeks != len(lista) - 1: # jesli szukany element pojawil sie przed wartownikiem
                return ('znaleziono poszukiwany element, indeks w liscie: {}'
                        .format(indeks))
            else: # szukany_el = wartownik, czyli w oryginalnej liscie nie pojawil sie poszukiwany element
                return 'nie znaleziono poszukiwanego elementu'
