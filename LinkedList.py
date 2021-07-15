class Node:
    def __init__(self , info , link = None):
        self.info = info
        self.link = link

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_begining(self,info):
               #create a new node
        newNode = Node(info)
        if self.head != None:
            newNode.link = self.head
            self.head = newNode
        else:
            self.head = newNode

    def insert_at_end(self , info):
        newNode = Node(info)
        if self.head != None:
            current = self.head
            while current.link != None:
                current = current.link
            current.link = newNode
        else:
            self.head = newNode

    def display(self):
        current = self.head
        while current != None:
            print(current.info)
            current = current.link




LL = LinkedList()
LL.insert_at_begining(10)
LL.insert_at_begining(1)
LL.display()
print("-------------------")
LL.insert_at_end(777)
LL.insert_at_end(222)
LL.display()
