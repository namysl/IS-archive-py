# coding: utf-8
# Prosta implementacja drzewa binarnego w oparciu o dodatkowa klase Node
# Nie ma zaimplementowanego wstawwiania -  to jest zalezna od zastosowan
# Prosze to samemu uzupelnic o inne operacje na drzewie
# Michal Baczynski (AiSD wyklad)

#importujemy plik z naszą klasa kolejki FIFO (np. opartej na liscie dowiazanej)
import FIFO_queue_ver_04_linked_list_poprawne

# dla ułatienia odwolania się do naszeej kolejki tworzymy alias
Kolejka = FIFO_queue_ver_04_linked_list_poprawne.Queue

class Node:
    """Klasa Node - do pamietania pojedynczego wezla w drzewie"""
    def __init__(self, dane=None, left=None, right=None):
        # konstruktor
        # pole "dane" bedzie zawieralo nasze dane np. liczby, napisy lub inne rekordy badz klasy
        # left_node bedzie wskazywalo na lewy wezel
        # right_node bedzie wskazywalo na prawy wezel
        self.dane = dane
        self.left_node = left
        self.right_node = right

class binaryTree:
    """Klasa drzewo binarne - istotna dana jest tylko korzen"""
    def __init__(self):
        self.korzen = None

    def _inorder(self,drzewo):
        #Wypisywanie drzewa w sposob inorder - procedura wewnetrzna
        if drzewo is not None:
            self._inorder(drzewo.left_node)
            print(drzewo.dane)
            self._inorder(drzewo.right_node)

    def inorder(self):
        #Wypisywanie w porzadku inorder dla korzenia - procedura zeewnetrzna
        self._inorder(self.korzen)


    def _postorder(self,drzewo):
        # Wypisywanie w porzadku postorder dla korzenia - procedura wewnetrzna
        if drzewo is not None:
            self._postorder(drzewo.left_node)
            self._postorder(drzewo.right_node)
            print(drzewo.dane)

    def postorder(self):
        #Wypisywanie w porzadku postorder dla korzenia - procedura zeewnetrzna
        self._postorder(self.korzen)


    def _breadthFirst(self,drzewo):
        # Wypisywanie metoda przeszukiwania wszerz - procedura wewnetrzna
        # korzystamy z kolejki FIFO (nieistotne jak zaimplementowanej!)
        q = Kolejka()
        # wkladamy do naszej kolejki FIFO korzen
        q.enqueue(drzewo)

        # odwiedzamy kazdy wezel w drzewie
        while not q.isEmpty():
            # wypisujemy i usuwamy to co jest na poczatku kolejki
            node = q.first()
            q.dequeue()
            print(node.dane)
            # i dodajemy dzieci tego wezla do kolejki o ile nie sa puste (czyli "Nonami")
            if node.left_node is not None:
                q.enqueue(node.left_node)
            if node.right_node is not None:
                q.enqueue(node.right_node)

    def breadthFirst(self):
        # Wypisywanie metoda przeszukiwania wszerz - procedura zewnetrzna
        self._breadthFirst(self.korzen)

# Przykladowe drzewo
"""r1 = binaryTree()
r1.korzen = Node("T")
r1.korzen.left_node =Node("X")
r1.korzen.left_node.left_node =Node("B")
r1.korzen.left_node.right_node=Node("G")
r1.korzen.left_node.right_node.left_node=Node("Z")
r1.korzen.right_node =Node("C")
r1.korzen.right_node.left_node =Node("J")
r1.korzen.right_node.right_node =Node("R")
r1.korzen.right_node.right_node.left_node =Node("K")
r1.korzen.right_node.right_node.left_node.left_node =Node("A")
r1.korzen.right_node.right_node.right_node=Node("M")"""


r1 = binaryTree()

r1.korzen = Node(1)
r1.korzen.left_node = Node(2)
r1.korzen.left_node.left_node = Node(4)
r1.korzen.left_node.right_node = Node(5)
r1.korzen.right_node = Node(3)


print("Porzadek Inorder")
r1.inorder()

print("Porzadek Postorder")
r1.postorder()

print("Przeszukiwanie wszerz")
r1.breadthFirst()
