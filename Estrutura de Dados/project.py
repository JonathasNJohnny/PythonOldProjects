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
        flag = False
        aux = self.head
        while aux != None:
            print("\n", aux.data[0])
            if (aux.data[1] == None or aux.data[1] == 0):
                aux.data[1] = int(input("Digite a 1º nota: "))
                flag = True
            if (aux.data[2] == None or aux.data[2] == 0):
                aux.data[2] = int(input("Digite a 2º nota: "))
                flag = True
            aux = aux.next
        if (flag):
            print("Notas inseridas!")
        else:
            print("Não há cadeiras que precisam adicionar notas!")

    def modifyGrades(self):
        flag = False
        aux = self.head
        while aux  != None:
            print("\n", aux.data[0])
            if (aux.data[1] != None):
                aux.data[1] = int(input("Digite a 1º nota: "))
                flag = True
            if (aux.data[2] != None):
                aux.data[2] = int(input("Digite a 2º nota: "))
                flag = True
            aux = aux.next
        if (flag):
            print("Notas modificadas!")
        else:
            print("Não há cadeiras que precisam modificar notas!")

    def selfPrint(self):
        print()
        aux = self.head
        counter = 0
        while aux != None:
            counter += 1
            print(aux.data[0], ": ", aux.data[1], ", ", aux.data[2],sep="")
            aux = aux.next

    def remove(self, data):
        aux = self.head
        if(aux.next != None):
            if(aux.data[0] == data):
                aux.next.back = None
                self.head = aux.next
                aux.next = None
                return
            else:
                while(aux.next != None):
                    if(aux.data[0] == data):
                        break
                    aux = aux.next
                if(aux.next):
                    aux.back.next = aux.next
                    aux.next.back = aux.back
                    aux.next = None
                    aux.back = None
                else:
                    aux.back.next = None
                    aux.back = None
                return

        if (aux == None):
            return

        if (aux == None):
            return
                
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
    elif option == 2:
        list.modifyGrades()
    elif option == 3:
        list.selfPrint()
    elif option == 4:
        list.insert([input("Qual cadeira/matéria quer adicionar a grade?: ").upper(), None, None])
    elif option == 5:
        list.remove(input("Digite a cadeira/matéria que quer remover: ").upper)
    elif option == 0:
        flag = False
