

from BST import BinaryTree
from BST import Tree
from BinaryTreePrinter import BinaryTreePrinter

class SearchTree:
    def __init__(self):
        self.root = None

    def __insert_val(self, node, value):
        if node is None:
            return
        if node.val== value:
            return
        elif value < node.val:
            if node.left is None:
                node.left = Tree(value)
                return
            else:
                self.__insert_val(node.left, value)

        else:
            if node.right is None:
                node.right = Tree(value)
                return
            else:
                self.__insert_val(node.right, value)


        # else:
        #     self.__insert_val(node.right, value)
        #     if node.right is None:
        #         node.right = Tree(value)
        #         return


    def insert(self, val):
        if self.root is None:
            self.root=Tree(val)
        else:
            self.__insert_val(self.root, val)


    def __str__(self):
        tree_print = BinaryTreePrinter()
        return tree_print.get_tree_string(self.root)

    def in_order(self):
        self.__in_order(self.root)

    def __in_order(self, node):
        if node is None:
            return
        self.__in_order(node.left)
        print(node.val)
        self.__in_order(node.right)

my_bst = SearchTree()
for i in [1,2,3,5,4,6,21,11,10,22]:
    my_bst.insert(i)
    print(my_bst)
my_bst.in_order()