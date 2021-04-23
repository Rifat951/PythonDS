class Node:

    # create node
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

    # declare head, tail and size for linked list
class doublelinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_node(self, val):
        #declare node
        node = Node(val) #refers to the first node and its value
        if self.tail  is  None:
            self.head = node
            self.tail = node
            self.size +=1
        else:
            #if it has values
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def remove_node(self,node):
        # if the node is at the beginning or not
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        self.size -= 1

    def remove_last_node(self):
        if self.tail is not None:
            self.remove_node(self.tail)

    def remove_first_node(self):
        if self.head is not None:
            self.remove_node(self.head)

    def remove(self,value):
        node = self.head
        while node is not None:
            #if the value of node and given value is equal then remove it
            if node.val == value: #the value which will be passed for removing
                self.remove_node(node)
            node = node.next #it will iterate to next node

    def tracelastval(self):
        return self.tail.val

    def tracefirstval(self):
        return self.head.val


    def __str__(self):
        vals=[]
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"

# mylist = doublelinkedlist()
# mylist.add_node(1)
# mylist.add_node(5)
# mylist.add_node(4)
# print(mylist)
# print(mylist.size)


# mylist.remove(4)
# print(mylist)
# print(mylist.size)
#
# mylist.remove_last_node()
# print(mylist)
# print(mylist.size)
#
# mylist.remove_first_node()
# print(mylist)
# print(mylist.size)