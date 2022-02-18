import math

class Rocket:
    '''
    Obiekt Rakieta opisuje rakiete w przestworzach.
 
    Args:
    fuel (num): trzyma ilosc paliwa  
    pos: LIST lub TUPLE z dwoma liczbami (x, y)
    trace (list): trzyma liste zapisujaca zmiany polozenia rakiety
 
    Attributes:
    fuel: tu przechowujemy informacje o parametrze fuel
    pos: tu przechowujemy informacje o parametrze pos
    x: tu przechowujemy informacje o parametrze x
    y: tu przechowujemy informacje o parametrze y
    trace: tu przechowujemy informacje o parametrze trace
 
    '''

    def __init__(self, fuel, pos=(0, 0), trace = []):
        Rocket.no_fuel(fuel)
        self.fuel = fuel
        Rocket.check_pos(pos)
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.trace = trace # lista zapisujaca zmiane polozenia rakiety

    def no_fuel(fuel):
        assert fuel > 0, "rakieta nie ma paliwa, parametr fuel" \
        "mniejszy lub równy 0"
        
    def check_pos(pos):  # nie ma self!
        assert isinstance(pos, (list, tuple)), "pos to lista lub krotka"
        assert len(pos) == 2, "pos powinna miec 2 elementy"
        assert all([isinstance(el, (int, float)) for el in pos]), "wszystkie elementy powinny byc liczbami"
        assert pos[1] >= 0, "wysokosc na jakiej jest Rakieta nie powinna byc ujemna"


# sprawdzanie pozycji:

    def get_pos(self):
        return self.pos
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

# ustawianie pozycji:
    
    def set_x(self, x):   
        test_pos = x, self.pos[1]
        return self.set_pos(test_pos)
    
    def set_y(self, y):           
        test_pos = self.pos[0], y
        return self.set_pos(test_pos)
 
    def set_pos(self, pos):
        Rocket.check_pos(pos)
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.trace.append((self.x, self.y))
        return self.pos

# poruszanie sie po linii prostej:

    def move_left(self, x):
        if abs(x) > self.fuel:
            raise FuelTooLow(x)
        else:
            self.fuel -= abs(x)
        final = self.set_x(self.x - x)
        return final
        
    def move_right(self, x):
        if abs(x) > self.fuel:
            raise FuelTooLow(x)
        else:
            self.fuel -= abs(x)
        final = self.set_x(self.x + x)
        return final
        
    def move_up(self, x):
        if abs(x) > self.fuel:
            raise FuelTooLow(x)
        else:
            self.fuel -= abs(x)
        final = self.set_y(self.y + x)
        return final
    
    def move_down(self, x):
        if abs(x) > self.fuel:
            raise FuelTooLow(x)
        else:
            self.fuel -= abs(x)
        final = self.set_y(self.y - x)
        return final

# obliczanie odleglosci:

    def dist_point(self, pos):
        """
        Oblicza odleglosc w linii prostej od rakiety
        (w jej aktualnym położeniu) do punktu wybranego
        przez uzytkownika (podana krotka lub lista złozona
        z dwoch elementow)
        """
        a = pos[0] # x wybranego punktu
        b = pos[1] # y wybranego punktu
        dist = math.sqrt((a - self.x)**2 + (b - self.y)**2)
        # alfa = (math.asin(self.y/dist) * 180)/math.pi
        print("Odleglosc od", pos, "wynosi", dist, "jednostek")
        # print(alfa, "stopni")
    
    def dist_base(self):
        """
        Oblicza odległość w linii prostej od rakiety
        (w jej aktualnym położeniu) do bazy (punkt 0,0)
        """
        dist = math.sqrt((self.x)**2 + (self.y)**2)
        # alfa = (math.asin(self.y/dist) * 180)/math.pi
        print("Odleglosc od bazy wynosi", dist, "jednostek")
        # print(alfa, "stopni względem bazy")


    def fuel_left(self):
        """Zwraca liczbe dostepnego paliwa"""
        info = "Dostepna ilosc paliwa: " + str(self.fuel)
        return info

    def see_list(self):
        """Zwraca liste trace zawierającą koordynaty zmian polozenia rakiety"""
        return self.trace
    
class FuelTooLow(Exception):
    def __init__(self, wpro):
        self.wpro = wpro
    def __str__(self):
        info = "Zbyt malo paliwa, aby rakieta zmienila polozenie. \n" +\
               "Odleglosc jaka miala przebyc rakieta: " \
               + str(self.wpro) +"\n" + "Sprawdz ilosc dostepnego paliwa."
        return info


raki = Rocket(10)
print(raki.set_pos((0,0)), raki.fuel_left())
print(raki.move_up(2), raki.fuel_left())
print(raki.see_list())
