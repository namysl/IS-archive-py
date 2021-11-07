import random

imiona = ['ZUZANNA', 'JULIA', 'MAJA', 'ZOFIA', 'HANNA', 'LENA', 'ALICJA',
          'MARIA', 'AMELIA', 'OLIWIA', 'ALEKSANDRA', 'WIKTORIA', 'EMILIA',
          'LAURA', 'NATALIA', 'ANTONINA', 'POLA', 'LILIANA', 'IGA', 'MARCELINA',
          'ANNA', 'GABRIELA', 'HELENA', 'MICHALINA', 'NADIA', 'KORNELIA', 'MILENA',
          'MARTYNA', 'KLARA', 'NIKOLA', 'JAGODA', 'ŁUCJA', 'BARBARA', 'KAROLINA',
          'AGATA', 'MAGDALENA', 'WERONIKA', 'KAJA', 'BLANKA', 'NELA', 'NINA',
          'ANASTAZJA', 'KINGA', 'LILIANNA', 'SARA', 'PAULINA', 'MATYLDA', 'MAŁGORZATA',
          'JOANNA',  'ANIELA', 'IZABELA', 'KALINA', 'MARTA', 'RÓŻA', 'KATARZYNA', 'EWA',
          'JAKUB', 'ANTONI', 'SZYMON', 'FILIP', 'JAN', 'WOJCIECH', 'FRANCISZEK', 'MIKOŁAJ',
          'KACPER', 'ALEKSANDER', 'MICHAŁ', 'ADAM', 'IGOR', 'PIOTR', 'WIKTOR', 'STANISŁAW',
          'LEON', 'MARCEL', 'MATEUSZ', 'TYMOTEUSZ', 'MAKSYMILIAN', 'BARTOSZ', 'NIKODEM',
          'KAROL', 'MIŁOSZ', 'OSKAR', 'OLIWIER', 'TYMON', 'DOMINIK', 'DAWID', 'TOMASZ',
          'PAWEŁ', 'IGNACY', 'ALAN', 'KRZYSZTOF', 'KAMIL', 'MACIEJ', 'NATAN', 'BARTŁOMIEJ',
          'BORYS', 'FABIAN', 'ARTUR', 'HUBERT', 'BRUNO', 'GABRIEL', 'PATRYK', 'JULIAN',
          'KUBA', 'KAJETAN', 'KSAWERY', 'OLAF', 'DANIEL', 'BŁAŻEJ', 'ERYK', 'GRZEGORZ']

nazwiska = ['NOWAK', 'KOWAL', 'WIŚNIA', 'WÓJCIK', 'KOWALCZYK', 'LEWANDOWICZ',
            'ZIELIŃ', 'WOŹNIAK', 'SZYMANEK', 'DĄBROWSKI', 'KOŹMIN', 'JANKOWIEC', 'MAZUR',
            'WOJCIECHOWICZ', 'KWIATKOWSKI', 'KRAWCZYK', 'KACZMAREK', 'WIELGUS', 'TREPKA',
            'ZAJĄC', 'KRÓL', 'PAWŁOWICZ', 'MICHALAK', 'WRÓBEL', 'WIECZOREK',
            'STĘPIEŃ', 'JAWOROWICZ', 'DUDEK', 'ADAMCZYK', 'MALINA', 'PAWLAK',
            'GÓREWICZ', 'SIKORA', 'NOWICKI', 'WITKOWSKI', 'WALCZAK', 'BARAN', 'MICHALAK',
            'SZEWCZYK', 'OSTROWIEC', 'ZALEWSKI', 'WRÓBEL', 'PIETRZAK']

ulice = ['Polna', 'Leśna', 'Słoneczna', 'Krótka', 'Szkolna', 'Ogrodowa', 'Lipowa', 'Brzozowa']
miasta = {'Bytom': '41-900', 'Ostrów Wielkopolski' : '63-400', 'Poznań' : '61-680',
           'Tychy' : '43-100', 'Wrocław' : '50-048'}
typ_opieki = ['tymczasowa', 'stała']


def all_in_one(ile, lista_imiona, lista_nazwiska, lista_miasta, lista_ulice, typ_opieki):
    output = []
    for i in range(ile//2):
        one_dml = 'INSERT INTO STOWARZYSZENIE VALUES('
        one_dml += str(random.randint(1000000000, 9999999999))
        miasto, kod = random.choice(list(lista_miasta.items()))
        one_dml += ', \'Fundacja {}\', \'{}\', \'{}\', \'{}\', {}, {}, \'{}@stowarzyszenie.pl\');'.format\
            (i+1, miasto, kod, random.choice(lista_ulice), random.randint(10, 60),
             (random.randint(111111111, 999999999)), miasto.lower()[0:5])

        output.append(one_dml)

    for i in range(ile//2):
        one_dml = 'INSERT INTO KOORDYNATOR VALUES('
        one_dml += str(random.randint(55111111111, 99111111111))
        imie = random.choice(lista_imiona)
        nazwisko = random.choice(lista_nazwiska)
        one_dml += ', \'{}\', \'{}\', {}, '.format(imie, nazwisko, random.randint(111111111, 999999999))
        one_dml += '\'{}.{}@stowarzyszenie.pl\', '.format(imie.lower()[0], nazwisko.lower())
        one_dml += '    PESEL_PRZELOZONY!!!!!!!        ,'
        one_dml += '    KRS_STOWARZYSZENIE!!!!!!!!     );'

        output.append(one_dml)

    for i in range(ile):
        one_dml = 'INSERT INTO WOLONTARIUSZ VALUES('
        one_dml += str(random.randint(55111111111, 99111111111))
        imie = random.choice(lista_imiona)
        nazwisko = random.choice(lista_nazwiska)
        one_dml += ', \'{}\', \'{}\', {}, '.format(imie, nazwisko, random.randint(111111111, 999999999))
        one_dml += '\'{}.{}@stowarzyszenie.pl\', '.format(imie.lower()[0:2], nazwisko.lower()[0:5])
        one_dml += 'TO_DATE(\'{}-{}-{}\', \'YYYY-MM-DD\'), \'aktywny\', '.format(random.randint(2015, 2021),
                                                                                 random.randint(1, 12),
                                                                                 random.randint(1, 28))
        one_dml += '    PESEL_KOORDYNATOR!!!!!!!!     );'

        output.append(one_dml)

    for i in range(ile):
        one_dml = 'INSERT INTO OPIEKUN VALUES('
        one_dml += str(random.randint(55111111111, 99111111111))
        imie = random.choice(lista_imiona)
        nazwisko = random.choice(lista_nazwiska)
        one_dml += ', \'{}\', \'{}\', {}, '.format(imie, nazwisko, random.randint(111111111, 999999999))
        one_dml += '\'{}.{}@hosting.pl\', '.format(imie.lower()[0:3], nazwisko.lower()[0:5])
        one_dml += 'TO_DATE(\'{}-{}-{}\', \'YYYY-MM-DD\'), \'{}\', '.format(random.randint(2015, 2021),
                                                                            random.randint(1, 12), random.randint(1, 28),
                                                                            random.choice(typ_opieki))
        one_dml += '    PESEL_WOLONTARIUSZ!!!!!!!!     );'

        output.append(one_dml)

    for i in range(ile//2):
        one_dml = 'INSERT INTO KLINIKA VALUES('
        one_dml += str(random.randint(1000000000, 9999999999))
        miasto, kod = random.choice(list(lista_miasta.items()))
        one_dml += ', \'Klinika {}\', \'{}\', \'{}\', \'{}\', {}, {});'.format\
            (i+1, miasto, kod, random.choice(lista_ulice), random.randint(10, 60),
             (random.randint(111111111, 999999999)))

        output.append(one_dml)

    for i in range(ile):
        one_dml = 'INSERT INTO WETERYNARZ VALUES('
        imie = random.choice(lista_imiona)
        nazwisko = random.choice(lista_nazwiska)
        one_dml += '\'{}\', \'{}\', {}, '.format(imie, nazwisko, random.randint(111111111, 999999999))
        one_dml += '    NIP_KLINIKA!!!!!!!!     );'

        output.append(one_dml)

    for i in range(ile//3):
        one_dml = 'INSERT INTO DARCZYNCA VALUES('
        one_dml += str(random.randint(55111111111, 99111111111))
        imie = random.choice(lista_imiona)
        nazwisko = random.choice(lista_nazwiska)
        one_dml += ', \'{}\', \'{}\', \'Firma {}\');'.format(imie, nazwisko, i+1)

        output.append(one_dml)

    return output


#print(all_in_one(10, imiona, nazwiska, miasta, ulice, typ_opieki))


def format2txt(list_return):
    with open('NEW_insert_sql_project.txt', 'w') as f:
        for item in list_return:
            f.write("%s\n\n" % item)

    f.close()

format2txt(all_in_one(10, imiona, nazwiska, miasta, ulice, typ_opieki))
