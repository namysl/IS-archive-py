def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


class IteratorFibo:
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 1
        return fibo(self.n)


def generator_fibo():
    n = 0
    while True:
        yield fibo(n)
        n += 1


def infinity():
    i = 0
    while True:
        yield i
        i += 1

        
# wyrazenie generujace
gen_expression = (fibo(n) for n in infinity())
for x in gen_expression:
    print(x)

# funkcja
#print(fibo(6))

# generator - klasa
fibo_gen = IteratorFibo()
fibo_iter = iter(fibo_gen)

#for x in fibo_iter:
#    print(x)

# iterator
#f = generator_fibo()
#for x in f:
#    print(x)
