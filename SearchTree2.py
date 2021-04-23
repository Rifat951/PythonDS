from BinaryTreePrinter import BinaryTreePrinter


class Node:
    def __init__(self, val):
        self.left: Node = None
        self.right: Node = None
        self.val = val


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.__insert(self.root, val)

    def __insert(self, node: Node, val):
        if node.val == val:
            return
        elif val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self.__insert(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self.__insert(node.right, val)

    def __str__(self):
        tree_print = BinaryTreePrinter()
        return tree_print.get_tree_string(self.root)

bst = BinarySearchTree()
for i in [1,2,5,3,4,6]:
    bst.insert(i)
    print(bst)
