from Linked_List import doublelinkedlist

class Stack_Test:
    def __init__(self):
        self.__list = doublelinkedlist()

    def push(self, val):
        self.__list.add_node(val)

    def pop(self):
        val = self.__list.tracelastval()
        self.__list.remove_last_node()
        return val

    def list_isempty(self):
        return  self.__list.size ==0

    def pivot(self):
        return self.__list.tracelastval()

    def __len__(self):
        return self.__list.size


mystack = Stack_Test()
mystack.push(1)
mystack.push(2)
mystack.push(3)
print(mystack.pivot())

print(len(mystack))
mystack.pop()
print(mystack.pivot())
print(mystack.pivot())
