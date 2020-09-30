#https://www.youtube.com/watch?v=JlMyYuY1aXU
#Node Class, Linked List

class node: #Se crea la clase de nodo
    def __init__(self, data=None): #usando el __init__, se usa el parametro de data
        self.data = data #Especifica que es variable.data
        self.next = None #Especifica el siguiente valor, nulo por ahora

#Linked list class

class linked_list: #Se crea la clase de linkes list
    def __init__(self): #Se define funcion, init siempre inicializa la clase
        self.head = node() #Se crea una relacion entre .head = class node
    
    def append(self, data): #Funcion para agregar a la linked list
        new_node = node(data) #Relacion de varaibles con la clase dado el parametro data
        actual = self.head #Da valor a actual de ser un nodo
        while actual.next != None: #Iteracion mientras el actual.next no sea nulo
            actual = actual.next #Da el valor al siguiente nodo, mientras no sea cero
        actual.next = new_node #Crea el(los) siguiente(s) nodo(s) dando el valor

    def lenght(self): #funcion para obtener el largo de la linked list
        actual = self.head #Valor a actual de nodo
        total = 0 #Contador
        while actual.next != None: #Iteracion mientras el actual.next no sea nulo
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

