def hashing_str(klucz, m):
    """Funkcja skrotu dla stringow"""
    assert isinstance(klucz, str), "klucz powinien byc typu str"

    suma = 0
    for litera in klucz:
        suma += ord(litera)
    return suma % m


def hashing_tuple(klucz, m):
    """Funkcja skrotu dla krotek"""
    assert isinstance(klucz, tuple), "klucz powinien byc typu tuple"
    
    return len(klucz) % m


def hashing_float(klucz, m):
    """Funkcja skrotu dla floatow"""
    assert isinstance(klucz, float), "klucz powinien byc typu float"
    
    return int(klucz % m)
