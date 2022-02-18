# wzor
def cosinus(x, j):
    if j == 0:
        return 1
    else:
        return -cosinus(x, j-1) * x**2 * (2*j * (2*j - 1))**(-1)

print('funkcja:')

print(cosinus(3.14, 0) + cosinus(3.14, 1) + cosinus(3.14, 2) + cosinus(3.14, 3))

print('*'*10)


# sumowanie kolejnych wyrazow
def sumuj(x, j):
    suma = 0
    for i in range(j+1):
        suma += cosinus(x, i)
    return suma

print('suma:')

print(sumuj(3.14, 3))

print('*'*10)


# iterator - klasa
class Iterator:
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        self.j = 0
        return self

    def __next__(self):
        wynik = sumuj(self.x, self.j)
        self.j += 1
        return wynik

print('iterator - klasa:')

iter_class = Iterator(3.14)
A = iter(iter_class)

for i in range(0, 4):
    print(next(A))

print('*'*10)


# generator z yield
def generator_yield(x):
    j = 0
    suma = 0
    while True:
        suma += cosinus(x, j)
        yield suma
        j += 1

print('generator z yield:')

gen_yield = generator_yield(3.14)
for i in range(0, 4):
    print(next(gen_yield))

print('*'*10)


# nieskoczony iterator
def infinity():
    i = 0
    while True:
        yield i
        i += 1

# wyrazenie generujace / generator expressions
print('wyrazenie generujace:')

wyr_gen = (sumuj(3.14, i) for i in infinity())
for i in range(0, 4):
    print(next(wyr_gen))
