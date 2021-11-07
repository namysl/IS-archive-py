def nonagonal(n):
    """Oblicza oraz zwraca wartosc liczby niagonalnej dla danego n"""
    wzor = (n * (7 * n - 5)) // 2
    return wzor

# testy:
# 5 pierwszych liczb (poczawszy od n=1): 1, 9, 24, 46, 75
print(nonagonal(1), nonagonal(2), nonagonal(3), nonagonal(4), nonagonal(5))

class IteratorNonagonal:
    """Obiekt IteratorNonagonal sluzy do zwracania kolejnych liczb nieagonalnych

    Examples
    ________
    >>> nonagon = IteratorNonagonal()
    >>> next_nonagon = iter(nonagon)
    >>> print(next(next_nonagon))
    1
    >>> print(next(next_nonagon))
    9
    """
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 1
        return nonagonal(self.n)

# testy dla klasy iteratora:

iter_klasa = IteratorNonagonal()
nastepny = iter(iter_klasa)

for i in range(0, 10):  # 10 pierwszych liczb
    print(next(nastepny))


# generator - yield
def generator_nonanogal():
    """Zwraca kolejne wartosci liczb nieagonalnych"""
    num = 1
    while True:
        yield nonagonal(num)
        num += 1

print('generator z yield:')

gen_yield = generator_nonanogal()
for i in range(0, 10):  # do 10 liczb
    print(next(gen_yield))



def infinity():
    x = 1
    while True:
        yield x
        x += 1

print('wyrazenie generujace')
gen_exp = (nonagonal(x) for x in infinity())

for nastepny in range(0, 10):
    print(next(gen_exp))