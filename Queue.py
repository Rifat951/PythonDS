from Linked_List import doublelinkedlist

#first in first out

class Queue:
    def __init__(self):
        self.__list_queue = doublelinkedlist()

    def enqueue(self,val):
        self.__list_queue.add_node(val)

    def dequeue(self):
        val = self.__list_queue.tracefirstval()
        self.__list_queue.remove_first_node()
        return val

    def front(self):
        return self.__list_queue.tracefirstval()

    def isempty(self):
        return self.__list_queue.size == 0

    def __len__(self):
        return self.__list_queue.size

# myfifo = Queue()
# myfifo.enqueue(2)
# myfifo.enqueue(3)
# myfifo.enqueue(1)
#
# print(myfifo.front())
# print(len(myfifo))
#
# myfifo.dequeue()
# print(myfifo.front())
# print(len(myfifo))

