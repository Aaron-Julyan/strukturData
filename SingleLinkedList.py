class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    #menambah data di paling belakang
    def add(self,data):
        if(self.head):
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.size+=1
        else:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            self.size+=1

    # mengambil data pada index tertentu
    def getData(self,index):
        if(index>=self.size):
            return False
        iterator = self.head
        for i in range (0,index):
            iterator = iterator.next
        return iterator.data

    # mengambil size dari linked list
    def getSize(self):
        return int(self.size)

    #Update data di node tertentu
    def update(self,data,index):
        if(index>=self.size):
            return False
        iterator = self.head
        if(index == 0):
            self.head.data = data
            return True
        for i in range(0,index):
            iterator = iterator.next
        iterator.data = data

    #print linked list
    def printList(self):
        iterator = self.head
        while(iterator):
            print(iterator.data, end = " ")
            iterator = iterator.next
        print()