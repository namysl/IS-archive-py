A = [[1,1,0,0,0], [0,1,0,0,0], [1,1,1,1,0], [0,1,0,1,0], [0,1,0,1,1]]

def idol(lista):
    nieidole = []
    len_ = len(A)
    
    for x in range(len_):
        for y in range(len_):
            if lista[x][y] == 1 and x != y:
                nieidole.append(lista[x])
                break
            else:
                continue
                
    Idol = [x for x in lista if x not in nieidole]

    return Idol

print(idol(A))
