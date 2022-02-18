# sortowanie: bogosort, insertion sort, insertion sort with sentinel, quicksort

import random
 
def bogosort(lista):
    '''
    Zlozonosc obliczeniowa: śr. i pes. O((n+1)!)
    Optymistyczny przypadek zaklada, ze sortowanie uda sie za pierwszym razem.
    W najgorszym przypadku prawidlowe posortowanie moze sie nigdy nie udac.'''

    def posortowana(lista):
        '''Funkcja pomocniczna dla bogo_sort,
        sprawdzajaca czy lista zostala posortowana.
        Korzysta z funkcji sorted (timsort, śr. O(n log n)),
        ale w przypadku bogosort to nie ma znaczenia'''
        
        if lista == sorted(lista): # jesli lista zostala posortowana 
            return True
        else: # jesli nadal jest nieposortowana
            return False 

    while not posortowana(lista): # dopoki lista nie jest posortowana
        random.shuffle(lista) # nastepna losowa kolejnosc listy
    return lista # zwroc liste, jesli zostala posortowana


def insertion(lista):
    '''Zlozonosc obliczeniowa: śr./pes. O(n^2)'''
    
    n = len(lista)
    for i in range(1, n): # zaczynamy od drugiego elementu w liscie
        klucz = lista[i] # zmienna, ktora bedzie przybierac wartosci listy z indeksem i
        j = i - 1 # element poprzedzajacy
        while j >= 0 and lista[j] > klucz: # wartosc pod lista[j] wieksza od lista[i]; szukanie miejsca dla odpowiedniej wartosci
            lista[j+1] = lista[j] # zmiana miejsc
            j -= 1 # dekrementacja j
        lista[j+1] = klucz # podstawienie zmiennej na miejsce innej wartosci
    return lista


def insertion_sentinel(lista):
    '''Zlozonosc ta sama co w przypadku insertion sort bez wartownika'''
    
    lista[0] = -1 # wartownik wstawiany na pierwsze miejsce listy
    for i in range(2, len(lista)): # petla od drugiego elementu w liscie
        klucz = lista[i]
        j = i - 1
        while lista[j] > klucz: # porownuje tylko z kluczem
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = klucz
    return lista
            
def quicksort(lista):
    '''
    Zlozonosc obliczeniowa: śr. O(n log n)
                            pes. O(n^2)

    Nazwa quicksort wynika z szybkosci z ktora algorytm jest w stanie posortowac
    liste, jesli wybierzemy odpowiedni pivot (element podzialu).
    Przypadek optymistyczny zaklada, ze pivot bedzie mediana listy.
    Przypadek sredni, czyli losowy wybor elementu z listy jako pivot.
    Przypadek pesymistyczny - wybor najmniejszego lub najwiekszego elementu z listy.'''
    
    mniejsze = [] # pusta lista na elementy mniejsze od elementu podzialu
    pivot_l = [] # element podzialu 
    wieksze = [] # elementy wieksze od elementu podzialu
    if len(lista) <= 1: # jesli lista ma tylko jeden element lub jest pusta
        return lista # lista jest juz posortowana, zwraca ja 
    else: # len(lista) wieksze od 1 
        pivot = lista[0] # pivot jest pierwszym elementem nieposortowanej listy
        for element in lista: # iterujac przez elementy listy
            if element < pivot: 
                mniejsze.append(element) # dodaje do podlisty elementy mniejsze od pivotu
            elif element > pivot:
                wieksze.append(element) # dodaje do podlisty elementy wieksze od pivotu
            else:
                pivot_l.append(element)
        mniejsze = quicksort(mniejsze) # rekurencyjne sortowanie podlisty mniejszych elementow
        wieksze = quicksort(wieksze) # rekurencyjne sort. podlisty wiekszych elementow

        # zwraca posortowana oryginalna liste    
        wynik = mniejsze + pivot_l + wieksze
        return wynik
        

L = [14, 10, 3, 12, 11, 55, 66, 1, 89, 3]
LL = [3, 5, 1, 4, 2]
LLL = [9, 8, 7, 6, 5, 4, 3, 2, 1]
