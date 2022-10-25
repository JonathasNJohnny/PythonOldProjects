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
        if aux == None:
            print("Não há pessoas hospedadas!")
        else:
            while aux != None:
                counter += 1
                print(counter, "º Pessoa\nNome:",aux.data[0], "\nNúmero do quarto:", aux.data[1], "\n",sep="")
                aux = aux.next

    def remove(self):
        aux = self.head
        if aux != None:
            self.head = self.head.next
            del aux

proceed = 1
option = 0
room = 23.00
food = 57.00
hotWater = 10.00
totalCoust = room

list = linkedList()
while (proceed != 0):
    option = int(input("Digite\n1 para adicionar um hospede\n2 para imprimir a lista de pessoas hospedadas\n3 para fazer o checkout de um hospede na ordem da fila\n0 para encerrar\n\nDigite sua ação: "))
    if (option == 1):
        list.insert([input("Digite o nome do hospede: "), input("Digite o número do quarto do hospede: ")])
        print()
    elif (option == 2):
        list.selfPrint()
    elif (option == 3):
        if (list.head != None):
            print("\nO hospede do quarto", list.head.data[1], "comeu alimentos da geladeira?", end=" ")
            option = int(input("Digite\n1 para Sim\n2 para Não\nDigite a opção: "))
            if (option == 1):
                totalCoust += food
            print("\nO hospede do quarto", list.head.data[1], "usou água quente?", end=" ")
            option = int(input("Digite\n1 para Sim\n2 para Não\nDigite a opção: "))
            if (option == 1):
                totalCoust += hotWater
            print("\nA pessoa de nome", list.head.data[0], "e de quarto número", list.head.data[1], "se despede do nosso hotel\nO valor total de sua hospedagem ficou por:", totalCoust, "R$\n")
            list.remove()
            totalCoust = room
            option = 3
        else:
            print("\nNão há pessoas hospedadas no hotel!\n")
    elif (option == 0):
        proceed = 0
