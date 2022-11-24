class Node:
    def __init__(self, data):
        self.back = None
        self.data = data
        self.next = None

class linkedList:
    
    def __init__(self):
        self.head = None

    def insert(self, element):
        new_node = Node(data = element)
        new_node.next = self.head
        new_node.back = None
        if self.head is not None:
            self.head.back = new_node
        self.head = new_node

    def insertGrades(self):
        aux = self.head
        while aux  != None:
            aux.data[1] = int(input("Digite a nota: "))
            aux = aux.next
        print("Notas inseridas!")

    def selfPrint(self):
        print()
        aux = self.head
        counter = 0
        while aux != None:
            counter += 1
            print(aux.data[0], ": ", aux.data[1],sep="")
            aux = aux.next

flag = True
option = 0
list = linkedList()
while (flag):
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    #SCNADU = Sistema de Cadastramento de Notas de Alunos em Disciplinas de uma Universidade
    print("Seja bem vindo ao sistema SCNADU")
    print("\nO que deseja fazer?\n")
    print("1 - Adicionar Notas\n2 - Modificar Notas\n3 - Imprimir Dados\n4 - Adicionar Cadeiras/Matérias\n5 - Remover Cadeiras/Matérias\n0 - Fechar sistema")
    option = int(input("Digite sua opção: "))
    print()
    if option == 1:
        list.insertGrades()
    if option == 4:
        option = input("Qual cadeira/matéria vc deseja adicionar à grade?: ")
        list.insert([option, 0])
    flag = False    
