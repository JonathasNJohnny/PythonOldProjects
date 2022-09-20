class Node:
   def __init__(self, data):
       self.data = data
       self.next = None
 
class linkedList:
 
   def __init__(self):
       self.head = None
 
   def insert(self, element):
       element.next = self.head
       self.head = element
  
   def evenElements(self):
       evenNumbers = 0
       current = self.head
       while current != None:
           if (current.data % 2 == 0):
               evenNumbers += 1
           current = current.next
       return evenNumbers
 
   def elementDepth(self, data):
       position = 0
       current = self.head
       while current != None:
           position += 1
           if (current.data == data):
               return position
           current = current.next
       return 0
 
   def ascendingChecker(self):
       current = self.head
       aux = current.data
       if current != None:
           current = current.next
       while current != None:
           if current.data > aux:
               aux = current.data
           else:
               return False
           current = current.next
       return True
 
list = linkedList()
 
list.insert(Node(4))
list.insert(Node(3))
list.insert(Node(2))
list.insert(Node(1))
 
#1
print("A lista possui", list.evenElements(), "números pares \n")
 
#2
x = 3
print("O elemento X não está na lista" if list.elementDepth(x) == 0 else "O elemento X está na profundidade/posição", list.elementDepth(x) if (list.elementDepth(x) != 0) else "", "\n")
 
#3
print("A lista está em ordem ascendente!" if list.ascendingChecker() == True else "A lista não está em ordem ascendente!", "\n")
