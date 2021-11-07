class Peak(object):
    """DOCSTRING!!!"""
    
    def __init__(self, L):
        self._L = L[:]
        self._n = len(self._L)
        self._m = len(self._L[0])

    def get_dim(self):
        """Zwraca rozmiary tablicy"""
        return (self._n, self._m) # dla C n=4, m=5

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
        """Zwraca lokalizację wartości w liście"""
        
        for i in range(len(self._L)):
            part = self._L[i]
            for j in range(len(part)):
                if part[j] == value:
                    return (i, j)


    def exhaustive(self, start=(0,0)): # brute force Machury
        """przeszukiwanie wyczerpujace"""
        loc = start[:]
        print('loc', loc)

        found = False
        while not found:
            left = top = right = bottom = None
            pos = self.get_val(loc)
            print('pos', pos)
            if loc[0] == 0:
                top = pos
                print('TOP loc[0] == 0:', top)
            if loc[0] == self._n - 1:
                bottom = pos
                print('BOT loc[0] == self._n - 1:', bottom, 'n:', self._n)
            if loc[1] == 0:
                left = pos
                print('LEFT loc[1] == 0:', left)
            if loc[1] == self._m - 1:
                right = pos
                print('RIGHT loc[1] == self._m - 1:', right, 'm:', self._m )
            
            if left == None:
                left = self.get_val((loc[0], loc[1]-1))
                print('get_val lef:t', left) 
            if right == None:
                right = self.get_val((loc[0], loc[1]+1))
                print('get_val right:', right)
            if top == None:
                top = self.get_val((loc[0]-1, loc[1]))
                print('get_val top:', top)
            if bottom == None:
                bottom = self.get_val((loc[0]+1, loc[1]))
                print('get_val bot:', bottom)

            if pos >= left and pos >= top and pos >= right and pos >= bottom:
                print("pos >= all:", pos)
                found = True
            else:
                buf = self.next_element(loc)
                if buf == -1:
                    found = True
                else:
                    loc = buf[:]
        print(self.get_val(loc))
        print(loc)
        return loc


    def b(self, start = (0, 0)):
        mniejloc = start[:]
        n = start[0]
        m = start[1]
        print('mniej loc:', mniejloc)
        mniej = self.get_val(mniejloc)
        print('mniej value:', mniej)


        if n == 0 and m == 0:
            pass
        if n == self._n - 1 and m == 0:
            pass
        if n == 0 and m == self._m - 1:
            pass
        if n == self._n - 1 and m == self._m - 1:
            pass
        if n == 0 and m < self._m:
            pass
        if n < self._n and m == 0:
            pass
        if n < self._n -1 and m == self._m - 1:
            pass
        if n == self._n - 1 and m < self._m - 1:
            pass

        
        else:
            gora = n - 1, m
            gora = self.get_val(gora)
        
            dol = n + 1, m
            dol = self.get_val(dol)

            lewo = n, m - 1
            lewo = self.get_val(lewo)
        
            prawo = n, m + 1
            prawo = self.get_val(prawo)
            
            print('gora:', gora, 'dol:', dol, 'lewo:', lewo, 'prawo:', prawo)

        #x = 0
        #for lista in self._L:
         #   for el in lista:  
          #      print('el:', el)
        
        if mniej >= gora and mniej >= dol and mniej >= lewo and mniej >= prawo:
            print('OK!')
        else:
            k = self.next_element((mniejloc))
            nn = k[0] - 1
            mm = k[1] - 1
            nnmm = nn, mm
            if k == -1:
                print('DUPA')
            else:
                self.b((nnmm))

                    
    def bt(self, start = (0, 0)): #brute force
        xy = self.get_val(start)
        n = start[0]
        m = start[1]

        try:
            if self._L[n+1][m] is None or self._L[n][m+1] is None:
                print('ooo')
                if self.next_element(xyz) == -1:
                    print('uwu')
        except IndexError:
            print('ffas')
            print(xy)
        if self._L[n+1][m] <= xy >= self._L[n][m + 1]:
                print(xy)
        else:
            if n <= self._n:
                print(n+1, m)
                self.bt(start = (n+1, m))
            else:
                print(n, m+1)
                self.bt(start = (n, m+1))


    def g(self, start = (0,0)): #greedy
        element = start[:]
        loc = self.get_loc(element)
        
        if element < self.next_element(element):
            element = self.next_element(element)
            element = self.get_loc(element)
            print(element)
        else:
            if element < self._L:
                print('sa')

               
    def dac(self, name_of_the_list): # DIVIDE AND CONQUER
        """DO ZROBIENIA W DAC:
        - docstring
        - przyklady wykorzystania klas i funkcji"""

        assert (self._m % 2) == 1, \
        "Nie mozna wyznaczyc srodka listy o parzystej liczbie kolumn, uzyj innej metody"
        
        L = name_of_the_list[:]
        middle = len(L[0]) // 2 # srodkowa kolumna listy 

        if len(L[0]) > 2:
            maximum = L[0][middle] # tutaj zapisuje najwiekszy element
            for row in range(0, self._n):
                if L[row][middle] > maximum:
                    maximum = L[row][middle] # jesli znajdzie wiekszy, nadpisuje max
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



    def idt(self): # PSEUDOALGORYTM DO TESTOW
        """Najwiekszy element listy zawsze bedzie wierzcholkiem"""
        L = self._L[:]
        maximum = 0
        for sublist in L:
            for element in sublist:
                if element > maximum:
                    maximum = element
                else:
                    continue
        return self.get_loc(maximum)




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

BB = [[1, 2, 3, 4, 5],
     [5, 6, 7, 8, 9]]
b = Peak(BB)

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

JJ = [[101, 1, 45, 13, 10],
    [24, 8, 59, 17, 92],
    [83, 0, 4, 113, 11],
    [62, 77, 85, 30, 9]]
j = Peak(JJ)
