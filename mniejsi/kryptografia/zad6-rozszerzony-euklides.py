def rozszerzony_euklides(a, m):
    if m == 0:
        return a, 1, 0

    gcd, x_prev, y_prev = rozszerzony_euklides(m, a % m)
    x = y_prev
    y = x_prev - (a // m) * y_prev

    return gcd, x, y


def znajdz_odwrotny(a, m):
    gcd, x, y = rozszerzony_euklides(a, m)
    if gcd != 1:
        raise ValueError("Element odwrotny nie istnieje.")
    else:
        return x % m


element = 6
modulo = 11
odwrotny = znajdz_odwrotny(element, modulo)
print("Element odwrotny do", element, "modulo", modulo, "wynosi:", odwrotny)
