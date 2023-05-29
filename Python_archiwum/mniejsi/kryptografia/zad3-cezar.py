polskie_znaki = {260: 65, 262: 67, 280: 69, 321: 76, 323: 78, 211: 79, 346: 83, 377: 90, 379: 90}
# A = 65 -> Z = 90


def cezar_szyfruj(tekst, przesuniecie):
    szyfr = ""

    if przesuniecie > 26:
        przesuniecie = przesuniecie % 26

    for i in tekst:
        if i.isalpha():
            i = i.capitalize()
        else:
            szyfr += i
            continue

        i = ord(i)

        if i > 90:
            i = polskie_znaki[i]
        if (i + przesuniecie) > 90:
            x = (i + przesuniecie) - 90
            szyfr += chr(64+x)
        else:
            szyfr += chr(i+przesuniecie)

    return szyfr


def cezar_odszyfruj(szyfr, przesuniecie):
    tekst = ""

    if przesuniecie > 26:
        przesuniecie = przesuniecie % 26

    for i in szyfr:
        if not i.isalpha():
            tekst += i
            continue

        i = ord(i)

        if (i - przesuniecie) < 65:
            x = 65 - (i - przesuniecie)
            tekst += chr(91-x)
        else:
            tekst += chr(i-przesuniecie)

    return tekst


szyfruj = cezar_szyfruj("żółtaczka123", 54)
odszyfruj = cezar_odszyfruj(szyfruj, 2)

print(szyfruj, odszyfruj)

for n in range(0, 27):
    print(cezar_szyfruj("Stół z powyłamywanymi nogami", n), "=", cezar_odszyfruj(cezar_szyfruj("Stół z powyłamywanymi nogami", n), n))
