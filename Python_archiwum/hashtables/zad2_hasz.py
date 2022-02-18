def hashing_str(klucz):
    """Funkcja skrotu dla stringow"""
    assert isinstance(klucz, str), "klucz powinien byc typu str"

    suma = 0
    for litera in klucz:
        suma += ord(litera)
    return suma % len(klucz)


def hashing_tuple(klucz):
    """Funkcja skrotu dla krotek"""
    assert isinstance(klucz, tuple), "klucz powinien byc typu tuple"
    
    if type(klucz[0]) == str:
        return len(klucz)**2 - len(klucz[0])
    else:
        return len(klucz)**2 % klucz[0]


def hashing_float(klucz):
    """Funkcja skrotu dla floatow"""
    assert isinstance(klucz, float), "klucz powinien byc typu float"
    
    return int(int(klucz) % klucz//2)
