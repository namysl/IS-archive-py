"""class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self, start, visit):
        if start:
            visit += (str(start.data) + "->")
            visit = self.preorder(start.left, visit)
            visit = self.preorder(start.right, visit)
        return visit

    def inorder(self):
        pass

    def postorder(self):
        pass

# wyswietlanie elementow w roznych kolejnosciach, preoder rekurencyjnie

bt = BinaryTree()
bt.root = Node('X')
bt.root.left = Node('Y')
bt.root.right = Node('Z')
bt.preorder('X', 'Y')
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder_print(self, start, visit):
        if start:
            visit += (str(start.value) + "-")
            visit = self.preorder_print(start.left, visit)
            visit = self.preorder_print(start.right, visit)
        return visit

    def print_tree(self, visit_type):
        if visit_type == 'preorder':
            return self.preorder_print(tree.root, "")
        elif visit_type == 'inorder':
            return self.inorder(tree.root, "")
        else:
            print("visit type " + str(visit_type) + " brak metody")
            return False

    def inorder(self, start, visit):
        if start:
            visit += (str(start.left) + "->")
            visit = self.inorder(start.value, visit)
            visit = self.inorder(start.right, visit)
        return visit

    def height(self):
        if tree.left is None and tree.right is None:
            return 0
        if tree.left is None:
            return self.height(tree.right) + 1
        elif tree.right is None:
            return self.height(tree.left) + 1

        return max(self.height(tree.left), self.height(tree.right)) + 1

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
print(tree.print_tree("preorder"))
print(tree.height())
#print(tree.print_tree("inorder"))
