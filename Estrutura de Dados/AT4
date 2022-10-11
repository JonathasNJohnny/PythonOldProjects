class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    
    def __init__(self):
        self.head = None

    def insert(self, element):
        new_node = Node(element)
        if self.head == None:
            self.head = new_node
            return
        aux = self.head
        while aux.next != None:
            aux = aux.next
        aux.next = new_node

    def selfPrint(self):
        print()
        aux = self.head
        counter = 0
        while aux != None:
            counter += 1
            print(counter, "º Pessoa: ",aux.data, sep="")
            aux = aux.next

    def remove(self):
        aux = self.head
        if aux != None:
            self.head = self.head.next
            del aux

proceed = 1
option = 0
list = linkedList()
while (proceed != 0):
    option = int(input("\nDigite\n1 para adicionar uma pessoa\n2 para imprimir a lista de pessoas\n3 para atender uma pessoa da lista\n0 para encerrar\n\nDigite sua ação: "))
    if (option == 1):
        list.insert([input("Digite seu nome: "), input("Digite seu CPF: "), input("Digite o número da sua conta bancária: ")])
    elif (option == 2):
        list.selfPrint()
    elif (option == 3):
        print("A pessoa de nome", list.head.data[0], "foi atendida!")
        list.remove()
    elif (option == 0):
        proceed = 0


#Inverter Strings
string = input("\nDigite uma palavra para invertermos: ")
aux = ""
for i in range(len(string)):
    aux += string[len(string) - 1 - i]
string = aux
print("A palavra invertida é:", string)
