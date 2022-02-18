# nieskoczonosc
def infinity():
    x = 0
    while True:
        yield x
        x += 1


# wzor
def catalan(n):
    if n == 0:
        return 1
    else:
        wynik = 0
        for i in range(n):
            wynik += catalan(i) * catalan(n-1-i)
        return wynik

print('funkcja:')

print(catalan(10))

print('*'*10)


# iterator - klasa (__iter__, __next__, StopIteration)
class Iterator:
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 1
        return catalan(self.n)

print('iterator - klasa:')

iter_class = Iterator()
A = iter(iter_class)

for i in range(0, 10):  # 10 liczb
    print(next(A))

print('*'*10)


# generator - yield
def generator():
    num = 0
    while True:
        yield catalan(num)
        num += 1

print('generator z yield:')
"""
gen_yield = generator()
for i in infinity():  # nieskonczonosc
    print(next(gen_yield))

"""
print('*'*10)


# wyrazenie generujace - generator
print('wyrazenie generujace')
gen_exp = (catalan(x) for x in infinity())

for nastepny in infinity():
    print(next(gen_exp))
