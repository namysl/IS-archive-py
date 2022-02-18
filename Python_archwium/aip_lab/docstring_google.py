def docstring(dok = {}):
    """Tworzy docstring"""

    if 'Summary' in dok.keys():
        print(dok.get('Summary'), '\n')
        dok.popitem()
    for key in dok.items():
        print(key[0], ':\n')
        n = 0
        for value in key:
            print(value[n], ':\n')
            n+=1

docstring({'Args': ['A', 'B'], 'Attributes': ['A', 'B'], \
            'Summary': "Obiekt Gruszka opisuje nam wlasnosci gruszek."})


def docstring2(dok = {}):
    """Tworzy docstring w typie Google"""

    for el in range(1):
        print(dok.get('Summary'), "\n")
    print("Args:")
    for el in dok.get('Args'):
        print("{}:".format(el))
    print("\nAttributes:")
    for el in dok.get('Attributes'):
        print("{}: tu przechowujemy informacje o parametrze {}".format(el, el))
        
docstring2({'Args': ['a', 'b'], 'Attributes': ['a', 'b'], \
            'Summary': "Obiekt Gruszka opisuje nam wlasnosci gruszek."})


def docstring3(dok = {}):
    """Tworzy docstring"""

    if 'Summary' in dok.keys():
        print(dok.get('Summary'), '\n')
        dok.popitem()
    for key, value in dok.items():
        print(key, ':', '\n', value, '\n')


    
docstring3({'Args': ['a', 'b'], 'Attributes': ['a', 'b'], \
            'Summary': "Obiekt Gruszka opisuje nam wlasnosci gruszek."})


