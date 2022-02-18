def HornerPochodne(n, A, c):
    j = 0
    ddxList = []
    while j < n:
        q = []
        q.append(A[0])
        i = 1
        while i < len(A)-1:
            q.append(q[i-1] * c + A[i])
            i += 1

        total = q[0]
        i = 1

        while i < len(q):
            total = total * c + q[i]
            i += 1
        ddxList.append(total * silnia(j+1))
        A = q[::]
        j += 1

    return ddxList

def silnia(n):
    if n < 2:
        return 1
    else:
        return n * silnia(n-1)

def i_silnia(n):
    result = 1
    i = 2
    while i <= n:
        result *= i
    return result

A1 = [3, -4, 2, -2]
A2 = [-2, 2, -4, 3]
c1 = -1
k1 = 0
n1 = 3

print(HornerPochodne(n1, A2, c1))

n2 = 4
A3 = [3, -6, 0, -4, -9]
c2 = 3

print(HornerPochodne(n2, A3, c2))
