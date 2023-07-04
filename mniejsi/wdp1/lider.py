A = [1, 2, 3, 4, 2, 2, 2]
B = [1, 2, 2, 3, 3, 3, 3, 2, 3]
C = [10, 30, 40, 30, 10, 10]

def lider(lista):
    slownik = {}

    for i in lista:
        if i in slownik:
            slownik[i] += 1
        else:
            slownik[i] = 1

    maks = 0
    maks_klucz = 0
    
    for key, value in slownik.items():
        if value > maks:
            maks = value
            maks_klucz = key
    
    if maks > len(lista)/2:
        return maks_klucz
    else:
        return None

    
print(lider(A))
print(lider(B))
print(lider(C))
