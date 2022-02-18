# Punkt 1a: drzewo binarne jako klasa
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Punkt 3a: rekurencyjnie preorder, inorder, postorder
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

    def print_tree(self, method, tree_root):
        """Wybor metody wypisywania wezlow w drzewie binarnym"""
        if method == 'preorder':
            return self.preorder(tree_root)
        elif method == 'inorder':
            return self.inorder(tree_root)
        elif method == 'postorder':
            return self.postorder(tree_root)
        else:
            print('no such method')

    def height(self, tree_root):
        """Punkt 6: metoda wyznaczajaca wysokosc drzewa"""
        if tree_root is None:
            return -1
        elif tree_root.left is None and tree_root.right is None:
            return 0
        else:
            left_height = self.height(tree_root.left)
            right_height = self.height(tree_root.right)

            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    def count_leaves(self, tree_root):
        """Punkt 7: metoda wyznaczajaca ilosc lisci w drzewie"""
        count = 0
        if tree_root.left is None and tree_root.right is None:
            return 1  # korzen moze byc lisciem
        elif tree_root.left is None:
            count += self.count_leaves(tree_root.right)
        elif tree_root.right is None:
            count += self.count_leaves(tree_root.left)
        else:
            count += self.count_leaves(tree_root.left) + self.count_leaves(tree_root.right)

        return count

    def count_nodes(self, tree_root):
        """Punkt 8: metoda wyznaczajaca ilosc wszystkich wezlow w drzewie

        Bazuje na przechodzeniu postorder"""
        count = 0
        if tree_root is None:
            return 0
        if tree_root is not None:
            count += self.count_nodes(tree_root.left) + self.count_nodes(tree_root.right) + 1
        return count


drzewo = BinaryTree()
drzewo.root = Node(1)

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

print('\npreorder:')
print(drzewo.preorder(drzewo.root))
print('\ninorder:')
print(drzewo.inorder(drzewo.root))
print('\npostorder:')
print(drzewo.postorder(drzewo.root))

print('\nprint_tree:')
print(drzewo.print_tree('preorder', drzewo.root))
print(drzewo.print_tree('inorder', drzewo.root))
print(drzewo.print_tree('postorder', drzewo.root))

print('\nheight:')
print(drzewo.height(drzewo.root))
print('\ncount_leaves:')
print(drzewo.count_leaves(drzewo.root))
print('\ncount_nodes:')
print(drzewo.count_nodes(drzewo.root))
