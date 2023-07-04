class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def preorder(self, tree_root):
        """root -> left -> right"""
        preordered = []
        if tree_root is not None:
            preordered.append(tree_root.value)
            preordered = preordered + self.preorder(tree_root.left)
            preordered = preordered + self.preorder(tree_root.right)
        return preordered

    def inorder(self, tree_root):
        """left -> root -> right"""
        inordered = []
        if tree_root is not None:
            inordered = self.inorder(tree_root.left)
            inordered.append(tree_root.value)
            inordered = inordered + self.inorder(tree_root.right)
        return inordered

    def postorder(self, tree_root):
        """left -> right -> root"""
        postordered = []
        if tree_root is not None:
            postordered = self.postorder(tree_root.left)
            postordered = postordered + self.postorder(tree_root.right)
            postordered.append(tree_root.value)
        return postordered

    def wszerz_wypisz(self, tree_root):
        lista = []

        if tree_root:
            lista.append(tree_root)
            print(tree_root.value)
        aktualny_node = tree_root

        while aktualny_node is not None:
            if aktualny_node.left is not None:
                print(aktualny_node.left.value)
                lista.append(aktualny_node.left)

            if aktualny_node.right is not None:
                print(aktualny_node.right.value)
                lista.append(aktualny_node.right)
            lista.pop(0)

            if len(lista) == 0:
                break

            aktualny_node = lista[0]


drzewo = BinaryTree(1)

drzewo.root.left = Node(2)
drzewo.root.left.left = Node(4)
drzewo.root.left.right = Node(5)

drzewo.root.right = Node(3)
drzewo.root.right.right = Node(6)
drzewo.root.right.right.right = Node(7)

"""
       1
     /   \
    2     3
   / \     \
  4   5     6
             \     
             7

"""

# print('\npreorder:')
# print(drzewo.preorder(drzewo.root))
# print('\ninorder:')
# print(drzewo.inorder(drzewo.root))
# print('\npostorder:')
# print(drzewo.postorder(drzewo.root))

drzewo.wszerz_wypisz(drzewo.root)