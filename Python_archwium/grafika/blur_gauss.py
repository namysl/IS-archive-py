from IPython.display import display
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math


path="./Koloseum.png"
img = Image.open(path)

arr = np.array(img)


def splot(RGB, Mf):
    r = int(len(Mf)/2)
    nr = 0
    for i in range(len(Mf)):
        for j in range(len(Mf[0])):
            nr += Mf[i][j]
            
    nr = max(nr, 1)
    RGB2 = np.zeros((len(RGB), len(RGB[0]),3), dtype=np.uint8,)
    for x in range(r, len(RGB)-r):
        for y in range(r, len(RGB[0])-r):
            tmp = np.zeros(3)
            for i in range(len(Mf)):
                for j in range(len(Mf[0])):
                    tmp += RGB[x-r+i][y-r+j]*Mf[i][j]
            tmp = abs(tmp)
            tmp /= nr
            [i if  i <255 else 255 for i in tmp]
            
            RGB2[x][y] = tmp
    return RGB2


def smoothGauss(RGB, sigma, r):
    """
    wygładzenia obrazu metodą filtracji splotowej w oparciu o filtr Gaussa

    RGB:   tablica z oryginalnym obrazem
    sigma: odchylenie standardowe rozkładu
    r:     promień filtracji (opisuje rozmiar filtra Gaussa, 
           macierz, z którą splatamy, ma rozmiar (2r+1)x(2r+1), 
           maksymalna przyjmowana wartość r to 12)

    return: przefiltrowana tablica RGB

    Krzywa Gaussa ma wartość maksymalną dla centralnego elementu macierzy, 
    wykorzystuje wyłącznie filtry kwadratowe.
    """
    assert r <= 12
    
    r_orig = r
    r = 2*r+1
    
    macierz = np.zeros((r, r))
     
    part = 1 / (2*math.pi * sigma**2)
    
    for x in range(0, r):
        for y in range(0, r):
            xx = x - (2*r_orig)/2
            yy = y - (2*r_orig)/2
            
            macierz[x][y] = part * math.e**(-(xx**2 + yy**2) / (2 * sigma**2))
    
    print(macierz)
    RGB = splot(RGB, macierz)
    return RGB


print('oryginał')
display(img)


result1 = smoothGauss(arr, 1, 1)  #sigma=1, r=1

imgblur1 = Image.fromarray(result1, 'RGB')
imgblur1.show()
display(imgblur1)


result2 = smoothGauss(arr, 1, 3)  #sigma=1, r=3

imgblur2 = Image.fromarray(result2, 'RGB')
imgblur2.show()
display(imgblur2)


result3 = smoothGauss(arr, 10, 1)  #sigma=10, r=1

imgblur3 = Image.fromarray(result3, 'RGB')
imgblur3.show()
display(imgblur3)


result4 = smoothGauss(arr, 10, 3)  #sigma=10, r=3

imgblur4 = Image.fromarray(result4, 'RGB')
imgblur4.show()
display(imgblur4)
