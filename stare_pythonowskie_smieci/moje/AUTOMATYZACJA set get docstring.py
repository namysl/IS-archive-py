def create_setget(atributes):
    print("SET/GET")
    for i in atributes:
        print("def get_{}(self):\n\treturn self.{}".format(i, i))
        print()
        print("def set_{}(self, new):\n\tself.{} = new".format(i, i))
        print()

#create_setget(['bok_a', 'bok_b', 'promien'])


def create_docstring(atributes):
    print("DOCSTRING")
    print()
    print("Obiekt *** opisuje nam podstawowe wlasnosci ***.")

    print()
    print("Parameters")
    print("----------")
    print()

    for i in atributes:
        print("{}: ***int/float/str/list/tuple***".format(i))
        print("\ttrzyma {}".format(i))

    print()
    print("Attributes")
    print("----------")
    print()

    for i in atributes:
        print("{}: tu przechowujemy informacje o parametrze {}".format(i, i))

    print()
    print("Examples")
    print("--------")
    print()


create_docstring(['a, w, h'])
