import math

# zad.1 - SZYFR

def bez_rozbicia(tekst):
    d = len(tekst)
    n = round(math.sqrt(d))

    tablica = [[] for i in range(n)]

    j = 0
    for wiersz in tablica:
        for i in range(n):
            if i + j < d:
                wiersz.append(tekst[i+j])
            else:
                wiersz.append('_')
        j += n
    #print(tablica)

    szyfr = ''
    for i in range(n):
        for wiersz in tablica:
            szyfr += wiersz[i]

    return szyfr


tekst = "BLĄD_JEST_PRZYWILEJEM_FILOZOFÓW_TYLKO_GŁUPCY_NIE_MYLĄ_SIĘ_NIGDY"
#print(bez_rozbicia(tekst))


def zaszyfruj(tekst):
    d = len(tekst)
    n = math.ceil(math.sqrt(d))

    tablica = [[] for i in range(n)]

    wypelnij_tablice(tablica, tekst, n, d)
    return generuj_szyfr(tablica, n)


def wypelnij_tablice(tablica, tekst, n, d):
    j = 0
    for wiersz in tablica:
        for i in range(n):
            if i + j < d:
                wiersz.append(tekst[i + j])
            else:
                wiersz.append('_')
        j += n


def generuj_szyfr(tablica, n):
    szyfr = ''
    for i in range(n):
        for wiersz in tablica:
            szyfr += wiersz[i]

    return szyfr

# print(zaszyfruj('Ewa_Namysl'))


def wyswietl_tablice(tablica):
    for wiersz in tablica:
        for znak in wiersz:
            print(znak, end = '')
        print("")


def odszyfruj(szyfr):
    tekst = ''
    n = int(math.sqrt(len(szyfr)))
    for i in range(n):
        for j in range(n):
            tekst += szyfr[i+j*n]
    return tekst




# zad.2 - LICZBA ZER

def policz_zera(a, l, p):
    licznik = 0
    liczba_zer = 0
    while l <= p:
        licznik += 1
        s = (l+p) // 2
        if a[s] == 1:
            p = s - 1
        else:
            liczba_zer += s - l + 1
            l = s + 1
    print(licznik)
    return liczba_zer

tab = [0, 0, 0, 0, 0, 0, 1, 1]