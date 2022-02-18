# Merge Sort, Counting Sort

L = [6, 5, 4, 3, 2, 1]
LL = [3, 2, 4, 2]

T = [8, 80, 90, 14, 3, 5, 20, 10, 5, 6, 90, 34, 11, 13, 56, 9]


def scalanie(lista):
    '''Merge sort
    Zlozonosc obliczeniowa optymistyczna/srednia/pesymistyczna: O(n log n)'''
    n = len(lista)
    if n <= 1: # == lista posortowana
        return lista
    else:
        # n > 2
        podzial = n // 2 # dzieli liste na czesci
        lewa = lista[:podzial] # lista od indeksu 0 do n//2
        prawa = lista[podzial:] # lista od srodka do konca

        scalanie(lewa) # rekurencyjny podzial na kolejne podlisty
        scalanie(prawa)

        # przejscie do drugiej czesci kodu, gdzie sortuje elementy
        # i laczy je w coraz wieksze grupy
        i = 0 # dla lewej strony
        j = 0 # dla prawej
        k = 0 # dla listy wyjsciowej
        while i < len(lewa) and j < len(prawa):
            if lewa[i] < prawa[j]: # porownywanie elementow
                lista[k] = lewa[i] # dodawanie do listy, jesli spelnia warunki
                i+=1
            else: # lewa[i] > prawa[j]
                lista[k] = prawa[j] # dodaje element z prawa
                j+=1
            k+=1 # inkrementuje - kolejny indeks dla listy

        # dodawanie do listy pozostalych elementow
        while i < len(lewa): # dla lewej strony
            lista[k] = lewa[i]
            i+=1
            k+=1
        
        while j < len(prawa): # dla prawej strony
            lista[k] = prawa[j]
            j+=1
            k+=1
        # zwraca gotowa liste
        return lista 


def zliczanie(lista):
    '''Counting sort
    Zlozonosc pesymistyczna: O(n+k), gdzie k to rozpietosc zakresu
    Zaleta: zlozonosc liniowa (algorytm nie porownuje wartosci liczb)
    Wada: trzeba znac zakres liczb listy (lub go wyznaczyc), w przypadku
    duzego zakresu, lista tymczasowa w ktorej beda zapisywane powtorzenia
    bedzie bardzo dluga, nawet jesli oryginalna lista bedzie miec malo elementow'''
    n = len(lista)
    gora = max(lista) # zakres gorny
    dol = min(lista) # zakres dolny
    
    temp = [0] * (gora + 1) # w temp zapisywanie powtorzen pod kolejnymi indeksami
    # ilosc miejsc zalezy od zakresu max
    # max + 1, bo wliczamy zero

    for el in lista: # dopisywanie liczby na pozycji odpowiadajacej jej wartosci
        temp[el] += 1 # jesli jest taka liczba w liscie, dopisuje jeden na tej pozycji

    for el in range(1, gora+1): # kumulacja w temp kolejnych elementow
        temp[el] += temp[el - 1]

    wynik = [0] * n # lista w ktorej beda umieszczane wartosci w odpowiedniej kolejnosci
    i = n - 1 # indeksy

    # Find the index of each element of the original array in count array
    # place the elements in output array
    while i >= 0: # ustawia w odpowiedniej kolejnosci
        wynik[temp[lista[i]]-1] = lista[i] # podstawia indeksy i umieszcza na liscie wynik
        temp[lista[i]] -= 1 # zmniejsza wartosci w tymczasowej liscie wg indeksow listy
        i -= 1 # po umieszczeniu elementu dekrementacja i
        
    return wynik
