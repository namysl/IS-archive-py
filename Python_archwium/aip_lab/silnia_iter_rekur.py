import math

def silnia_rekur(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia_rekur(n-1)


def silnia_iter(n):
    if n == 0 or n == 1:
        return 1
    else:
        silnia = 1
        while n > 1:
            silnia *= n
            n -= 1
        return silnia

print(silnia_rekur(4))
print(silnia_iter(4))
print(math.factorial(4))
