import math

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
        
    def exhaustive(self, start=(0,0)): # brute force?
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

    def force(self, start = (0, 0)):
        loc = start[:]
        ile = self._n * self._m

        for i in range(ile):
            pass        
        
    def greedy_ascent(self, start=(0,0)):
        """..."""
        pass

    """def dac(self): # divide and conquer
        L = self._L[:]
        
        # szuka środkową kolumnę
        middle = self._m // 2 # LUB: middle = math.floor(self._m/2) LUB: middle = (self._m - 0.5)/2

        #porównuje liczby w środkowej

            #4rth try - sukces?
        max = L[0][middle]
        for i in range(0, self._n):
            if L[i][middle] > max:
                max = L[i][middle]
                loc = (i, middle)
                x = i
        print("Największa w kolumnie:", max, "zlokalizowana w:", loc)
        if L[x][middle - 1] < max > L[x][middle + 1]:
            print("Mamy wierzchołek", loc)
        elif L[x][middle - 1] > max:
            print("Lewa większa:", L[x][middle - 1])
        elif L[x][middle + 1] > max:
            print("Prawa większa", L[x][middle + 1])"""
#DAC
    def dac(self): # divide and conquer
        lista = self._L[:]
        L = lista
        middle = self._m // 2
        
        max = L[0][middle]
        for i in range(0, self._n):
            if L[i][middle] > max:
                max = L[i][middle]
                locc = (i, middle)
                x = i
        print("Największa w kolumnie:", max, "zlokalizowana w:", locc)
#WIERZCHOLEK
        if L[x][middle - 1] < max > L[x][middle + 1]:
            print("Mamy wierzchołek", locc)
#LEWA WIEKSZA
        elif L[x][middle - 1] > max:
            print("Lewa większa:", L[x][middle - 1])


            #pisze tylko jedna obok: L = L[self._n - middle][self._m - x]
            """lista2 = []
            rzedy = 0
            kolumny = 0
            while rzedy < self._n and kolumny < middle:
                lista2.append(L[rzedy][kolumny]) 
                rzedy+=1
                middle+=1
            print(lista2)""" #drukuje pierwsza kolumne jako rzad


            """ # robimy fikolki zeby nie miec kolumn po prawej
            zzzz = []
            temp = []
            for sub_list in L:
                x = 0
                while x <= middle:
                    temp.append(sub_list[x])
                    x+=1
            #fikolki zeby to tez bylo lista w liscie        
            print(temp)
            kr = 0
            krak = self._m - 1
            for subb in range(self._m - 1):
                zzzz.append(temp[kr:krak])
                kr += self._m - 1
                krak += self._m - 1""" #kopia


            # robimy fikolki zeby nie miec kolumn po prawej
            temp = []
            for sub_list in L:
                x = 0
                while x < middle:
                    temp.append(sub_list[x])
                    x+=1
            #print("Lista temp:", temp)
            
            #fikolki zeby to tez bylo lista w liscie        
            temp_pogrup = []
            start = 0
            stop = middle
            for subb in range(self._m - 1):
                temp_pogrup.append(temp[start:stop])
                start += middle
                stop += middle

            #print("i:", i, "middle", middle, "start", start, "stop", stop)
            #print("self._n:", self._n, "self._m:", self._m)
            print("Lista temp_pogrup:", temp_pogrup)

                
#            L = [sub[0] for sub in L]
 #           print(L)



            #for x in L:
                #for y in x:
                    #L = L[0:middle+2]
            #print(L)





#            for x in L:
#                for y in x:
 #                   loc = (0,0)
 #                   if loc[1] < locc[1]:
  #                      #L = L[0:i][0:middle +1]
   #             else:
    #                continue"""

#PRAWA WIEKSZA            
        elif L[x][middle + 1] > max:
            print("Prawa większa", L[x][middle + 1])

# robimy fikolki zeby nie miec kolumn po lewej
            temp = []
            for sub_list in L:
                x = middle + 1
                while x < self._m:
                    temp.append(sub_list[x])
                    x+=1
            print("Lista temp:", temp)
            
            #fikolki zeby to tez bylo lista w liscie        
            temp_pogrup = []
            start = 0
            stop = middle
            for subb in range(self._m - 1):
                temp_pogrup.append(temp[start:stop])
                start += middle
                stop += middle

            print("i:", i, "middle:", middle, "start:", start, "stop:", stop)
            print("self._n:", self._n, "self._m:", self._m)
            print("Lista temp_pogrup:", temp_pogrup)
        else:
            print("wierzch")

            


        
            #1st try - nie znajduje najwiekszej
        """for i in range(len(L)):
            if L[i][middle] < L[i+1][middle] and L[i+1][middle] > L[i+2][middle]:

                i+=1
                print(len(L))
                continue
            else:
                print("największa w kolumnie:", L[i][middle])"""

            #2nd try - znajduje najwieksza, jest blad wyjscia poza tablice
        """while True:
            for i in range(self._n - 1):
                if L[i][middle] <= L[i+1][middle] >= L[i+2][middle]:
                    print(L[i+1][middle])
                else:
                    L[i][middle] <= L[i+1][middle] >= L[i+2][middle]
                    i+=1
                    print("co", L[i+1][middle])"""

            #3rd try - nie wyciagne lokalizacji
        """i = 0
        temp = []
        while i <= self._n - 1:
            temp.append(L[i][middle])
            print("dopisuję", L[i][middle])
            i+=1
        else:
            print("temp:", temp, "max:", max(temp))
            big = max(temp)"""






# testy
AA = [[1,   2,  3,  4],
     [14, 15, 16,  5],
     [13, 18, 17,  6],
     [12,  9,  3,  7],
     [11, 10,  9,  8]]

a = Peak(AA)
# print("loc (2, 1)", p.exhaustive())

AA2 = [[1,   2,  3,  4, 5, 10, 11],
     [14, 15, 16, 7, 5, 1, 6],
     [13, 18, 17,  9, 6, 2, 11],
     [9,  3,  11, 7, 4, 3, 2],
     [11, 10,  9,  6, 8, 4, 2],
       [1,2,3,4, 5, 6, 7]]

a2 = Peak(AA2)


BB = [[1,2,3,4,5],
     [5,6,7,8,9]]
b = Peak(BB)
# print("loc (1, 4)", pB.exhaustive())


CC = [[10,11,12,6,5],
     [13,17,16,5,4],
     [14,16,15,4,3],
     [2, 3, 4, 3, 2]]

c = Peak(CC)

DD = [[1,2,8,4,5],
      [9,8,7,6,5],
      [10,11,12,13,14],
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
