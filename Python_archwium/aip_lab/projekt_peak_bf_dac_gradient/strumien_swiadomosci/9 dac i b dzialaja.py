class Peak(object):
    """
    Obiekt Peak opisuje wlasnosci listy list
    zawierajaca wartosci liczbowe.
 
    Args:
        L: trzyma liste obiektu Peak
        
    Attributes:
        _L: tu przechowuje informacje o L 
        _n: tu przechowuje informacje o liczbie kolumn L
        _m: tu przechowuje informacje o liczbie rzedow L
    """
    
    def __init__(self, L):
        self._L = L[:]
        self._n = len(self._L)
        self._m = len(self._L[0])

    def set_list(self):
        """Zmiana wartosci listy"""
        self._L = input("Wpisz liste:")
        
    def get_list(self):
        """Zwraca liste list"""
        return self._L

    def print_list(self):
        """Wypisuje liste list z zachowaniem kolumn i rzedów"""
        for sublist in self._L:
            print(sublist)
    
    def get_dim(self):
        """Zwraca rozmiary tablicy"""
        return (self._n, self._m)

    def get_val(self, loc):
        """Zwraca wartosc na podanej pozycji"""
        return self._L[loc[0]][loc[1]]

    def next_element(self, loc):
        """Zwraca lokalizacje kolejnego elementu"""
        if loc[1] < self._m - 1:
            return loc[0], loc[1] + 1
        else:
            if loc[0] < self._n - 1:
                return loc[0] + 1, 0
            else:
                return -1

    def get_loc(self, value):
        """Zwraca lokalizacje podanej wartosci w liscie"""
        for i in range(len(self._L)):
            part = self._L[i]
            for j in range(len(part)):
                if part[j] == value:
                    return (i, j)

    def get_peak(self, algorithm):
        """Wybor algorytmu znajdujacego wierzcholek,
        nastepnie zwrot lokalizacji wierzcholka przez wybrana metode"""
        if algorithm == "dac":
            L = Peak.get_list(self)
            return Peak.dac(self, L)
        elif algorithm == "bf":
            return Peak.bf(self)
        elif algorithm is "gaa":
            pass
        else:
            print("Wybrano bledna nazwe algorytmu. \n \
                  Dostepne algorytmy: dac, bf, gaa")

    def get_max_val(self):
        """Zwraca najwiekszy element w liscie"""
        L = self._L[:]
        maximum = 0
        for sublist in L:
            for element in sublist:
                if element > maximum:
                    maximum = element
                else:
                    continue
        return self.get_loc(maximum)

    def bf(self, start = (0,0)): # BRUTE FORCE
        """Metoda brute force.
        Zaczynajac od elementu w punkcie (0, 0) przeszukuje liste list do momentu
        odnalezienia wierzcholka (wartosci wiekszej od najblizszych sasiadow)."""
        def go_up(loc):
            up = self.get_val((glob_loc[0] - 1, glob_loc[1]))
            return up
        def go_down(loc):
            down = self.get_val((glob_loc[0]+ 1, glob_loc[1]))
            return down
        def go_left(loc):
            left = self.get_val((glob_loc[0], glob_loc[1] - 1))
            return left
        def go_right(loc):
            right = self.get_val((glob_loc[0], glob_loc[1] + 1))
            return right
        def recur(loc): # rekurencja
            next_el = self.next_element((mniej_loc))
            next_el_value = self.get_val((next_el))
            if next_el == -1:
                return loc
            else:
                self.bf((next_el))
        
        mniej_loc = start[:]
        n = start[0]
        m = start[1]
        mniej = self.get_val(mniej_loc)
        glob_loc = self.get_loc(mniej)

        if n == 0 and m == 0: # lewy gorny element
            if mniej > go_down(glob_loc) and mniej > go_right(glob_loc):
                peak = self.get_loc(mniej); print(peak)
            else:
                recur(mniej_loc)
        elif n == self._n - 1 and m == 0: # lewy dolny element
            if mniej > go_up(glob_loc) and mniej > go_right(glob_loc):
                peak = self.get_loc(mniej); print(peak)
            else:
                recur(mniej_loc)
        elif n == 0 and m == self._m - 1: # prawy gorny element
            if mniej > go_down(glob_loc) and mniej > go_left(glob_loc):
                peak = self.get_loc(mniej); print(peak)
            else:
                recur(mniej_loc)
        elif n == self._n - 1 and m == self._m - 1: # prawy dolny element
            if mniej > go_left(glob_loc) and mniej > go_up(glob_loc):
                peak = self.get_loc(mniej); print(peak)
            else:
                recur(mniej_loc)
        elif n == 0 and m < self._m: # gorny rzad
            if mniej > go_left(glob_loc) and mniej > go_right(glob_loc) and mniej > go_down(glob_loc):
                peak = self.get_loc(mniej); print(peak)
            else:
                recur(mniej_loc)
        elif n == self._n - 1 and m == self._m - 1: # dolny rząd 
            if mniej > go_up(glob_loc) and mniej > go_left(glob_loc) and mniej > go_right(glob_loc):
                peak = self.get_loc(mniej); print(peak)
            else:
                recur(mniej_loc)
        elif n < self._n and m == 0: # lewa kolumna
            if mniej > go_right(glob_loc) and mniej > go_up(glob_loc) and mniej > go_down(glob_loc):
                peak = self.get_loc(mniej); print(peak)
            else:
                recur(mniej_loc)
        elif n < self._n and m == self._m - 1: # prawa kolumna 
            if mniej > go_left(glob_loc) and mniej > go_up(glob_loc) and mniej > go_down(glob_loc):
                peak = self.get_loc(mniej); print(peak)
            else:
                recur(mniej_loc)
        else: # nieskrajne przypadki
            if mniej > go_up(glob_loc) and mniej > go_down(glob_loc) and mniej > go_left(glob_loc) and mniej > go_right(glob_loc):
                peak = self.get_loc(mniej); print(peak)
            else:
                recur(mniej_loc)


    def dac(self, name_of_the_list): # DIVIDE AND CONQUER
        """Metoda divide and conquer. Za argument bierze liste list (np. w zmiennej).
        Wybiera najwiekszy element srodkowej kolumny i porownuje do wartosci sasiadow.
        Jesli nie znajdzie wierzcholka, odrzuca kolumne, ktorej sasiad byl mniejszy
        i rozpoczyna ponowne porownywanie."""

        assert (self._m % 2) == 1, \
        "Nie mozna wyznaczyc srodka listy o parzystej liczbie kolumn, uzyj innej metody"
        
        L = name_of_the_list[:]
        middle = len(L[0]) // 2 # srodkowa kolumna listy 

        if len(L[0]) > 2:
            maximum = L[0][middle] # tutaj zapisuje najwiekszy element
            for row in range(0, self._n):
                if L[row][middle] > maximum:
                    maximum = L[row][middle] # jesli znajdzie wiekszy, nadpisuje maximum
                    x = row

            if L[x][middle - 1] < maximum and maximum > L[x][middle + 1]: # WIERZCHOLEK
                return self.get_loc(maximum)

            elif L[x][middle - 1] > maximum: # LEWA WIEKSZA
                temp_list = [] # lista wartosci kolumn po lewej
                for sub_list in L:
                    x = 0
                    while x < middle:
                        temp_list.append(sub_list[x])
                        x+=1

                temp_group = [] # lista wartosci kolumn po lewej
                                # sformatowana w liste list (pierwotna forma)
                start = 0
                stop = middle
                for element in range(self._m - 1):
                    temp_group.append(temp_list[start:stop])
                    start += middle
                    stop += middle
                return self.dac(temp_group)

            elif L[x][middle + 1] > maximum: # PRAWA WIEKSZA
                temp_list = [] # lista wartosci kolumn po prawej
                for sub_list in L:
                    x = middle + 1
                    while x < self._m:
                        temp_list.append(sub_list[x])
                        x+=1

                temp_group = [] # lista wartosci kolumn po prawej
                                # sformatowana w liste list (pierwotna forma)
                start = 0
                stop = middle
                for element in range(self._m - 1):
                    temp_group.append(temp_list[start:stop])
                    start += middle
                    stop += middle
                return self.dac(temp_group)

        else: # ilosc elementow w rzedzie <= 2
            maximum = L[0][middle]
            for row in range (0, self._n):
                if L[row][middle] > maximum:
                    maximum = L[row][middle]
                    x = row

            if L[x][middle - 1] < maximum:
                return self.get_loc(maximum)
            else:
                return self.get_loc(L[x][middle - 1])

    def gr(self, start = (0, 0)): # GREEDY ASCDENT
        """Metoda zachlannego algorytmu wstepującego zwracajaca lokalizacje wierzcholka.
        Kolejnosc kierunkow w jakiej sprawdza sasiadow startujac od punktu (0, 0):
        w prawo, w dol, w lewo, w gore."""
        L = self._L
        n = start[0]
        m = start[1]
        print("START", self.get_val(start))

        def check(n, m):
            if n == 0 and m == 0: # lewy gorny element
                if L[n][m] > L[n+1][m] and L[n][m] > L[n][m+1]: return True
                else: return False
            elif n == self._n - 1 and m == 0: # lewy dolny element
                if L[n][m] > L[n-1][m] and L[n][m] > L[n][m+1]: return True
                else: return False
            elif n == 0 and m == self._m - 1: # prawy gorny element
                if L[n][m] > L[n+1][m] and L[n][m] > L[n][m-1]: return True
                else: return False
            elif n == self._n - 1 and m == self._m - 1: # prawy dolny element
                if L[n][m] > L[n][m-1] and L[n][m] > L[n-1][m]: return True
                else: return False
            elif n == 0 and m < self._m: # gorny rzad
                if L[n][m] > L[n][m-1] and L[n][m] > L[n][m+1] and L[n][m] > L[n+1][m]: return True
                else: return False
            elif n == self._n - 1 and m == self._m - 1: # dolny rząd 
                if L[n][m] > L[n-1][m] and L[n][m] > L[n][m-1] and L[n][m] > L[n][m+1]: return True
                else: return False
            elif n < self._n and m == 0: # lewa kolumna
                if L[n][m] > L[n-1][m] and L[n][m] > L[n][m+1] and L[n+1][m]: return True
                else: return False
            elif n < self._n and m == self._m - 1: # prawa kolumna 
                if L[n][m] > L[n][m-1] and L[n][m] > L[n-1][m] and L[n][m] > L[n+1][m]: return True
                else: return False
            else: # nieskrajne przypadki
                if L[n][m] > L[n-1][m] and L[n][m] > L[n+1][m] and L[n][m] > L[n][m-1] and L[n][m] > L[n][m+1]:
                    return True
                else: return False
        loc = (n, m)
        found = False
        if found == False:
            loc = (n, m)
            if L[n][m] < L[n][m+1] and m < self._m: # w prawo
                m += 1
                loc = (n, m)
                #print("IDĘ W PRAWO")
                #print('val A:', self.get_val((n,m)), (n,m))
                #print('a,b', n, m)
                if check(n, m) == True:
                    print('mamy wierzcholek')
                    print(loc)
                    found = True
                    return loc
                else:
                    self.gr((n, m))

            elif L[n][m] <= L[n+1][m] and n < self._n: # w dol
                n+=1
                #print("IDĘ W DÓŁ")
                #print('val D:', self.get_val((n, m)))
                #print('a,b:', n,m)
                if check(n,m) == True:
                    print('mamy wierzchołek')
                    print(loc)
                    found = True
                else:
                    self.gr((n, m))                

            elif L[n][m] <= L[n][m-1] and m < self._m: # w lewo
                m -= 1
                #print("IDĘ W LEWO")
                #print('val C:', self.get_val((n, m)))
                #print('a,b:', n,m)
                if check(n,m) == True:
                    print('mamy wierzchołek')
                    print(loc)
                    found = True
                else:
                    self.gr((n,m))

            elif L[n][m] <= L[n-1][m] and n < self._n: # w gore
                n -= 1
                #print("IDĘ W GÓRĘ")
                #print('val B:', self.get_val((n, m)))
                #print('a,b:', n,m)
                if check(n,m) == True:
                    print('mamy wierzchołek')
                    print(loc)
                    found = True
                else:
                    self.gr((n, m))
            else:
                loc = (n, m)
                return loc
        return loc


# testy
AA = [[1, 2, 3, 4],
     [14, 15, 16, 5],
     [13, 18, 17,  6],
     [12, 9, 3, 7],
     [11, 10, 9, 8]]
a = Peak(AA)

NN = [[1, 2, 3, 4, 5, 10, 11],
     [14, 15, 16, 7, 5, 1, 6],
     [13, 18, 17,  9, 6, 2, 11],
     [9,  3,  11, 7, 4, 3, 2],
     [11, 10,  9,  6, 8, 4, 2],
     [22, 2, 3, 4, 5, 6, 7]]
n = Peak(NN)

CC = [[10, 11, 12, 6, 5],
     [18, 17, 16, 5, 4],
     [14, 16, 15, 4, 3],
     [2, 3, 4, 3, 2]]
c = Peak(CC)

DD = [[1, 2, 8, 4, 5],
      [9, 8, 7, 6, 5],
      [10, 11, 12, 13, 14],
      [11, 16, 11, 22, 24]]
d=Peak(DD)

MM = [[1, 5, 8, 2, 4, 9, 3],
     [4, 10, 6, 15, 7, 1, 11],
     [2, 5, 13, 21, 44, 3, 6],
     [82, 100, 1, 7, 17, 77, 8]]
m = Peak(MM)

II = [[1, 1, 1],
      [1, 2, 1],
      [1, 1, 1]]
i = Peak(II)

JJ = [[1, 2, 45, 13, 10],
    [24, 8, 59, 17, 92],
    [12, 0, 60, 113, 11],
    [62, 77, 85, 30, 9]]
j = Peak(JJ)
