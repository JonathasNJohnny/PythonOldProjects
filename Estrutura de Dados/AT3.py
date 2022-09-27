class Node:
    def __init__(self, data):
        self.back = None
        self.data = data
        self.next = None
    
class simpleLinkedList:

    def __init__(self):
        self.head = None
 
    def insert(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
    
    def compareList(self, anotherLinkedList):
        list1 = self.head
        list2 = anotherLinkedList.head
        while list1 != None or list2 != None:
            if(list1.data != list2.data):
                return False
            list1 = list1.next
            list2 = list2.next
        return True

class doubleLinkedList:
 
    def __init__(self):
        self.head = None
 
    def insert(self, element):
        new_node = Node(data = element)
        new_node.next = self.head
        new_node.back = None
        if self.head is not None:
            self.head.back = new_node
        self.head = new_node
  
    def lowerElement(self):
        current = self.head
        aux = current.data
        while current != None:
            if (current.data <= aux):
                aux = current.data
            current = current.next
        return aux

    def elementToEndAmount(self, c):
        aux = False
        counter = 0
        current = self.head
        while current != None:
            if current.data == c:
                aux = True
            if aux == True:
                counter += 1
            current = current.next
        return counter

doubleLinkedList1 = doubleLinkedList()
doubleLinkedList1.insert(5)
doubleLinkedList1.insert(2)
doubleLinkedList1.insert(4)
doubleLinkedList1.insert(3)
doubleLinkedList1.insert(8)

simpleLinkedList1 = simpleLinkedList()
simpleLinkedList1.insert(5)
simpleLinkedList1.insert(5)
simpleLinkedList1.insert(3)

simpleLinkedList2 = simpleLinkedList()
simpleLinkedList2.insert(5)
simpleLinkedList2.insert(5)
simpleLinkedList2.insert(3)

#1
print("O menor elemento da lista é o {}!".format(doubleLinkedList1.lowerElement()))

#2
print("As duas listas são iguais!" if simpleLinkedList1.compareList(simpleLinkedList2) == True else "As duas listas são diferentes!")

#3
c = 4
print("A altura do 'elemento' C na lista é {}".format(doubleLinkedList1.elementToEndAmount(c)) if (doubleLinkedList1.elementToEndAmount(c) != 0) else "O valor C não está na lista")
