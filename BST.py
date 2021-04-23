from Queue import Queue
from BinaryTreePrinter import BinaryTreePrinter


class Tree:
    def __init__(self, val):
        self.left =None
        self.right =None
        self.val = val

class BinaryTree:
    #declare root
    def __init__(self):
        self.root =None

    #put the value of root node
    def insert(self, val):
        if self.root is None:
            self.root = Tree(val)
        else:
            node = Queue()
            node.enqueue(self.root)

            while True:
                #dequeue the first node
                check_node = node.dequeue()
                #if left child is empty then input value for left
                if check_node.left is None:
                    check_node.left = Tree(val)
                    return #it will return the value of left child node
                # if right child is empty then input value for right
                elif check_node.right is None:
                    check_node.right = Tree(val)
                    return
                else:
                    node.enqueue(check_node.left)
                    node.enqueue(check_node.right)
    def __str__(self):
        tree_disp = BinaryTreePrinter()
        return tree_disp.get_tree_string(self.root)

# my_bst = BinaryTree()
# for i in [1, 2, 3, 6, 7, 12, 45, 54, 12, 45, 76, 33]:
#     my_bst.insert(i)
#     print(my_bst)