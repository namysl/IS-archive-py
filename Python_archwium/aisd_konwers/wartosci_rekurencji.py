import math

"""Podaj wartości rekurencji dla 1 <= n <= 32"""

def T1(n):
    """podloga n/2"""
    if n == 1:
        return 1
    else:
        return 2 * T1(n//2) + 3 * n + 1

print('podloga')
podloga = []
for x in range(1, 33):
    podloga.append(T1(x))
print(podloga)


def T2(n):
    """sufit n/2"""
    if n == 1:
        return 1
    else:
        return 2 * T2(math.ceil(n/2)) + 3 * n + 1


print('sufit')
sufit = []
for x in range(1, 33):
    sufit.append(T2(x))
print(sufit)


def T3(n):
    """podloga n/2 + sufit n/2"""
    if n == 1:
        return 1
    else:
        return T1(n//2) + T2(math.ceil(n/2)) + 3 * n + 1


print('podloga + sufit')
podloga_sufit = []
for x in range(1, 33):
    podloga_sufit.append(T3(x))
print(podloga_sufit)


"""Wartosci sa takie same dla poteg dwojki"""
