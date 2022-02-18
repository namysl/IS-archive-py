def doc_sphinx(dok = {}):
    """Generuje docstring typu Sphinx"""

    print(dok.get('Summary'), "\n")
    print(dok.get('Description'), "\n")
    for el in dok.get('Args'): # wypisuje wszystkie argumenty
        print(":param TYPE {}:".format(el))
    for el in dok.get('Attributes'): # wypisuje wszystkie atrybuty
        print(":ivar TYPE {}: tu przechowujemy wartosc zmiennej {}".format(el, el))
    print("\n:Example:")
        

doc_sphinx({'Args': ['a', 'b'], \
            'Attributes': ['a', 'b', 'c'], \
            'Summary': 'Obiekt OBIEKT opisuje nam wlasnosci obiektu.', \
            'Description': 'Tutaj powinien byc nieco dluzszy tekst opisujacy klase Obiekt.'})
