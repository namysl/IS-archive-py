# Podpunkt 3 b)
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Zwraca informacje czy stos jest pusty"""
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        """Umieszcza element na szczycie stosu"""
        self.items.append(item)

    def pop(self):
        """Usuwa element ze szczytu stosu"""
        if self.is_empty() is False:
            self.items.pop()
        else:
            print('Pusty stos')

    def peak(self):
        """Zwraca element, ktory jest na szczycie stosu"""
        if self.is_empty() is False:
            return self.items[-1]
        else:
            print('Pusty stos')

    def size(self):
        """Zwraca rozmiar stosu"""
        return len(self.items)

    def __str__(self):
        return str(self.items)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """Podpunkt 3 b), wypisywanie kluczy za pomoca stosu w kolejnosci
    inorder, preorder, postorder"""
    def __init__(self):
        self.root = None

    def preorder_stack(self, tree_root):
        """root -> left -> right (za pomoca stosu)"""
        lista_output = []
        stos = Stack()
        stos.push(tree_root)

        while not stos.is_empty():
            temp = stos.peak()
            stos.pop()
            lista_output.append(temp.value)

            if temp.right is not None:
                stos.push(temp.right)
            if temp.left is not None:
                stos.push(temp.left)

        return lista_output

    def inorder_stack(self, tree_root):
        """left -> root -> right (za pomoca stosu)"""
        lista_output = []
        stos = Stack()
        temp = tree_root

        while temp is not None:
            stos.push(temp)
            temp = temp.left

        while not stos.is_empty():
            temp = stos.peak()
            lista_output.append(temp.value)
            stos.pop()

            if temp.right is not None:
                temp = temp.right
                stos.push(temp)

        return lista_output

"""    def postorder_stack(self, tree_root):
        lista_output = []
        stos = Stack()
        temp = tree_root

        while True:
            while temp is not None:
                if temp.right is not None:
                    stos.push(temp.right)

                stos.push(temp)
                temp = temp.left

            temp = stos.peak()
            stos.pop()

            if temp.right is not None and stos.peak() == temp.right:
                stos.pop()
                stos.push(temp)
                temp = temp.right

            else:
                lista_output.append(temp.value)
                temp = None

            if stos.is_empty():
                break
        return lista_output"""


drzewo = BinaryTree()
drzewo.root = Node(1)
drzewo.root.left = Node(2)
drzewo.root.left.left = Node(4)
drzewo.root.left.right = Node(5)
drzewo.root.right = Node(3)
drzewo.root.right.right = Node(6)


"""
       1
     /   \
    2     3
   / \     \
  4   5     6

"""


print('preorder_stack: ', drzewo.preorder_stack(drzewo.root))
print('inorder_stack:  ', drzewo.inorder_stack(drzewo.root))
#print('postorder_stack:', drzewo.postorder_stack(drzewo.root))

print('~~~~~')

"""Punkt 4:

Kompletne, niezdegenerowane drzewo binarne jako lista:


Moze miec postac taka jak kopiec w formie listy, gdzie w indeksie 0
wstawiamy None, korzeń ma indeks i=1, lewe dziecko 2i, prawe dziecko 2i+1:

tree = [None, 1, 2, 3, 4, 5, 6]

"""



class Node:
    """Punkt 2 - drzewo o dowolnej strukturze"""
    def __init__(self, value):
        self.value = value
        self.children = []
        # nie ma lewego ani prawego potomka, tylko lista przechowujaca dowolna ich ilosc

    def print_children(self):
        temp = []
        for child in self.children:
            temp.append(child.value)

        output = 'potomkowie {}: {}'.format(self.value, temp)
        return output

    def add_new_child(self, child):
        self.children.append(child)


print('drzewo o dowolnej strukturze:\n')
root1 = Node(10)
dziecko1 = Node(7)
dziecko2 = Node(8)
dziecko3 = Node(9)

root1.add_new_child(dziecko1)
root1.add_new_child(dziecko2)
root1.add_new_child(dziecko3)

print(root1.print_children())

dziecko4 = Node(5)
dziecko5 = Node(6)

dziecko1.add_new_child(dziecko4)
dziecko1.add_new_child(dziecko5)

print(dziecko1.print_children())

dziecko6 = Node(4)
dziecko3.add_new_child(dziecko6)
print(dziecko3.print_children())


""" 
wyglad powyzszego drzewa:

        10
       / | \
      7  8  9
    / |      \
   5  6       4

"""