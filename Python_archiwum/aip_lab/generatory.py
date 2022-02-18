def liczby(): # funkcja generujaca liczby parzyste do 20
    for i in range(11):
        yield i * 2

gen1 = liczby() # generator
gen1.__next__()





def parzyste(): # funckja generujaca liczby parzyste do niekonczonosci
    i = 0
    while True: # nieskonczonosc
        yield i
        i = i + 2

gen2 = parzyste() # generator
gen2.__next__() # operacje na obiekcie generatora pozwolaja uzyskać kolejne liczby parzyste
next(gen2)

#while True:
#    print(gen2.__next__())






def ret():
    for i in range(5):
        if i == 3:
            return # konczy dzialanie
        else:
            yield i # dopoki i != 3



# wyrazenie generujace
elements = (x * 2 for x in range(6))
next(elements)
