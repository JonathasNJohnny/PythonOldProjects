import gc
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

    def insertSubject(self, data):
        op = 0
        flag = False
        aux = self.head
        while aux != None:
            for i in range(len(aux.data[1])):
                if (aux.data[1][i] == data):
                    flag = True
            if (flag != True):
                while (op < 1 or op > 2):
                    print("1 - Para sim\n2 - Para não\nDeseja atribuir ",data[0]," ao aluno ", aux.data[0],"?: ", sep="", end="")
                    op = int(input())
                if (op == 1):
                    aux.data[1].append(data)
            aux = aux.next
            flag = False
            op = 0

    def insertGrades(self):
        op = 0
        aux = self.head
        while aux != None:
            if(len(aux.data[1]) != 0):
                for i in range(len(aux.data[1])):
                    for j in range(2):
                        if(aux.data[1][i][j+1] == None):
                            while (op < 1 or op > 2):
                                print("1 - Para sim\n2 - Para não\nDeseja adicionar a ", j+1 ,"º nota do aluno ", aux.data[0]," em ", aux.data[1][i][0],"?: ", sep="")
                                op = int(input())
                            if (op == 1):
                                print("Digite a ", j+1,"º nota: ")
                                aux.data[1][i][j+1] = int(input())
                            op = 0
                    if(aux.data[1][i][1] != None and aux.data[1][i][2] != None):
                        aux.data[1][i][3] = (aux.data[1][i][1] + aux.data[1][i][2]) / 2
            aux = aux.next

    def removeStudent(self, data):
        print("Hello World")

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
            print(counter, " - ",aux.data,sep="")
            aux = aux.next

    def remove(self, position):
        if self.head is None:
            return
        index = 0
        current = self.head
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1
        if index < position:
            print("\nNúmero digitado inválido.")
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next

flag = True
option = 0
list = linkedList()
while (flag):
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    #SCNADU = Sistema de Cadastramento de Notas de Alunos em Disciplinas de uma Universidade
    print("Seja bem vindo ao sistema SCNADU")
    print("\nO que deseja fazer?\n")
    print("1 - Adicionar Aluno\n2 - Adiconar Cadeira/Matéria ao Aluno\n3 - Adicionar Notas\n4 - Imprimir Dados\n")
    option = int(input("Digite sua opção: "))
    print()
    if option == 1:
        list.insert([input("Digie o nome do aluno: ").upper(), []])
    elif option == 2:
        list.insertSubject([input("Digite o nome da cadeira/matéria que deseja atribuir ao aluno: ").upper(), None, None, None])
    elif option == 3:
        list.insertGrades()
    elif option == 5:
        list.modifyGrades()
    elif option == 6:
        list.selfPrintNoGrades()
        list.remove(int(input("Digite a cadeira/matéria que quer remover: "))-1)
    elif option == 14:
        list.selfPrint()
    elif option == 0:
        print(len(list))
        flag = False
