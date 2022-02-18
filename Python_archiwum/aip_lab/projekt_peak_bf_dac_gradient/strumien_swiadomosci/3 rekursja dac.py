class Peak(object):
    """find peak 2d"""
    
    def __init__(self, L):
        self._L = L[:]
        self._n = len(self._L)
        self._m = len(self._L[0])

    def get_dim(self):
        """zwraca rozmiary tablicy"""
        return (self._n, self._m) # dla C n=4, m=5

    def get_val(self, loc):
        """zwraca wartosc na pozycji loc"""
        return self._L[loc[0]][loc[1]]

    def next_element(self, loc):
        """zwraca lokalizacje kolejnego elem"""
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

        found = False
        while not found:
            left = top = right = bottom = None
            pos = self.get_val(loc)
            if loc[0] == 0:
                top = pos
            if loc[0] == self._n - 1:
                bottom = pos
            if loc[1] == 0:
                left = pos
            if loc[1] == self._m - 1:
                right = pos
            
            if left == None:
                left = self.get_val((loc[0], loc[1]-1))
            if right == None:
                right = self.get_val((loc[0], loc[1]+1))
            if top == None:
                top = self.get_val((loc[0]-1, loc[1]))
            if bottom == None:
                bottom = self.get_val((loc[0]+1, loc[1]))

            #print pos, ":", left, top, right, bottom
            if pos >= left and pos >= top and pos >= right and pos >= bottom:
                found = True
            else:
                buf = self.next_element(loc)
                if buf == -1:
                    found = True
                else:
                    loc = buf[:]
        return loc

    def idt(self): # PSEUDOALGORYTM
        """Najwiekszy element zawsze bedzie wierzcholkiem XD"""
        L = self._L[:]
        max = 0 # tutaj zapisuje najwiekszy element

        for sublist in L:
            for element in sublist:
                if element > max:
                    max = element
                else:
                    continue
                
        # print(max)
        return self.get_loc(max) # lokalizacja wartosci
    
        
    def dac(self, L): # DIVIDE AND CONQUER
        """DO ZROBIENIA W DAC:
        - docstring
        - przyklady wykorzystania klas i funkcji"""
        assert (self._m % 2) == 1, \
        "listy o parzystej liczbie kolumn nie mozna podzielić"
        L = L[:]
        middle = len(L[0]) // 2 # srodek listy 

        """if len(L[0]) <= 2: # gdy zostana dwie kolumny
            print("za krótkie")
            max = L[0][middle]
            for row in range(0, self._n):
                print(row, L[row][middle])
                if L[row][middle] > max:
                    max = L[row][middle]
                #PROBLEM
                else:
                    continue
                print(max)
                if max < L[row][0]:
                    print(L[row][0])
                    return self.get_loc(L[row][0])
                else:
                    return self.get_loc(max)"""

        if len(L[0]) <= 2:
            max = L[0][middle]
            for row in range (0, self._n):
                if L[row][middle] > max:
                    max = L[row][middle]
                    x = row

            if L[x][middle - 1] < max:
                print(max)
                return self.get_loc(max)
            else:
                print(L[x][middle - 1])
                return self.get_loc(L[x][middle - 1])

        else:
            max = L[0][middle] # tutaj zapisuje najwiekszy element
            for row in range(0, self._n):
                if L[row][middle] > max:
                    max = L[row][middle] # jesli znajdzie wiekszy, nadpisuje max
                    x = row

            if L[x][middle - 1] < max and max > L[x][middle + 1]: # WIERZCHOLEK
                return self.get_loc(max) # zwraca lokalizacje wierzcholka

            elif L[x][middle - 1] > max: # LEWA WIEKSZA 
                temp_list = [] # lista wartosci kolumn po lewej
                for sub_list in L:
                    x = 0
                    while x < middle:
                        temp_list.append(sub_list[x])
                        x+=1
                    
                temp_group = [] # lista wartosci kolumn po lewej
                                # sformatowana w liste list (pierwotna struktura)
                start = 0
                stop = middle
                for element in range(self._m - 1):
                    temp_group.append(temp_list[start:stop])
                    start += middle
                    stop += middle

                #print("rząd:", row, "middle:", middle, "start:", start, "stop:", stop, \
                 #     "self._n:", self._n, "self._m:", self._m)
                print("Lista temp_group:", temp_group)
                return self.dac(temp_group)
        
            elif L[x][middle + 1] > max: # PRAWA WIEKSZA
                print("Prawa większa:", L[x][middle + 1])
                temp_list = [] # lista wartosci kolumn po prawej
                for sub_list in L:
                    x = middle + 1
                    while x < self._m:
                        temp_list.append(sub_list[x])
                        x+=1

                temp_group = [] # lista wartosci kolumn po prawej
                                # sformatowana w liste list (pierwotna struktura)
                start = 0
                stop = middle
                for element in range(self._m - 1):
                    temp_group.append(temp_list[start:stop])
                    start += middle
                    stop += middle

                #print("rząd:", row, "middle:", middle, "start:", start, "stop:", stop, \
                 #     "self._n:", self._n, "self._m:", self._m)
                print("Lista temp_group:", temp_group)
                return self.dac(temp_group)
            else:
                return None





# testy
AA = [[1, 2, 3, 4],
     [14, 15, 16, 5], # dac pokazuje 15
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


BB = [[1,2,3,4,5],
     [5,6,7,8,9]]
b = Peak(BB)

CC = [[10,11,12,6,5],
     [18,17,16,5,4],
     [14,16,15,4,3],
     [2, 3, 4, 3, 2]]
c = Peak(CC)

DD = [[1,2,8,4,5],
      [9,8,7,6,5],
      [10,11,12,13,14], # dac pokazuje 14
      [11,16,11,22,24]]
d=Peak(DD)

MM = [[1,5,8,2,4,9,3],
     [4,10,6,15,7,1,11],
     [2,5,13,21,44,3,6],
     [82,100,1,7,17,77,8]]
m = Peak(MM)

II = [[1, 1, 1],
      [1, 2, 1],
      [1, 1, 1]]
i = Peak(II)


mniej = [[101, 1, 45, 13, 10],
         [24, 8, 59, 17, 92],
         [83, 0, 4, 113, 11],
         [62, 77, 85, 30, 9]]

mn = Peak(mniej)
