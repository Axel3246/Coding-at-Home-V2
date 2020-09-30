#https://www.youtube.com/watch?v=JlMyYuY1aXU
#Node Class

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

#Linked list class

class linked_list:
    def __init__(self):
        self.head = node()
    
    def append(self, data):
        new_node = node(data)
        actual = self.head
        while actual.next != None:
            actual = actual.next
        actual.next = new_node

    def lenght(self):
        actual = self.head
        total = 0
        while actual.next != None:
            total += 1
            actual = actual.next
        return total
    
    def display(self):
        elements = []
        actual_node = self.head
        while actual_node.next != None:
            actual_node = actual_node.next
            elements.append(actual_node.data)
        print(elements)
    
    def get(self, index):
        if index >= self.lenght() or index<0:
            print('Index out of range')
            return None
        actual_index = 0
        actual_node = self.head
        while True:
            actual_node = actual_node.next
            if actual_index == index:
                return actual_node.data
            actual_index += 1
    
    def borrar(self, index):
        if index >= self.lenght() or index<0:
            print('Index out of range')
            return None
        actual_index = 0
        actual_node = self.head
        while True:
            last_node = actual_node
            actual_node = actual_node.next
            if actual_index == index:
                last_node.next = actual_node.next
                return
            actual_index += 1

mylinkedlist = linked_list()
mylinkedlist.append(1)
mylinkedlist.append(2)
mylinkedlist.append(3)
mylinkedlist.append(4)
mylinkedlist.get(3)
mylinkedlist.borrar(2)
mylinkedlist.display()

