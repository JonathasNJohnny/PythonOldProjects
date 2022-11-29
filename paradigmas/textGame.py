import time
import random

class game():
    def __init__(self):
        self.counter = 0
        self.playerLife = 100
        self.playerItems = []

    def start(self):
        newGame.story1()
        op = 0
        while(op < 1 or op > 3):
            print("Em qual porta deseja ir", " primeiro?: " if (self.counter == 0) else "?: ", sep="", end="")
            op = int(input())
            if (op == 4):
                time.sleep(1.5)
                print("Você vai até a 4º porta", end="", sep="")
                if (self.counter != 3):
                    print(" porém ela não abre..."); time.sleep(2); print("Ainda faltam", (3-self.counter), "cadeados"); time.sleep(1)
                else:
                    print("A porta finalmente está aberta, o que será que me espera lá dessa vez?")
        time.sleep(1.5)
        print("Você abre a ",op ,"º porta e entra", sep="")
        time.sleep(1.5)
        if (self.counter == 0):
            print("sem saber o que te espera lá dentro...")
        else:
            print("O que será que te espera dessa vez?")
        time.sleep(2)
        if (op == 1):
            newGame.map1()
        elif (op == 2):
            newGame.map2()
        elif (op == 3):
            newGame.map3()

    def map1(self):
        op = 0
        print("Ao entrar na porta você você se depara com uma sala totalmente escura, não da pra ver nada")
        time.sleep(3.5)
        print("você olha para trás e... a porta sumiu???")    
        time.sleep(2)
        print("numa sala completamente escura, você começa a sentir um cansaço, seus olhos involutariamente vão se fechando")
        time.sleep(4)
        print("Até você desmaiar...\n")
        print(".", end="", sep=""); time.sleep(1); print(".", end="", sep=""); time.sleep(1); print(".", end="", sep=""); time.sleep(2)
        print("\nVocê acorda num lugar totalmente diferente, a céu aberto")
        time.sleep(3)
        print("Suas roupas também mudaram de novo, são roupas verdes, dessa vez descalço")
        time.sleep(3.8)
        print("Uma bolsinha amarrada em seus... shorts??? enfim")
        time.sleep(2.4)
        print("Você coloca suas mãos dentro da bolsinha e encontra...")
        time.sleep(3)
        print("Um dado de 20 lados")
        time.sleep(2)
        print("Uma carta com o desenho de um machado de gelo")
        self.playerItems.append(["Machado Leviathan", "Um machado com poderes de gelo, se utilizado em batalha, ele congela a própria vida do usuário, e ele não sofrerá danos do próximo ataque"])
        time.sleep(3)
        print("e uma outra carta com o desenho de um colar")
        self.playerItems.append(["Colar de Lunda, um colar que ao equipado tem influência sobre o dado de 20 lados, que influência seria essa? aparentemente, esse item dura uma batalha inteira"])
        time.sleep(3)
        print("Ao olhar pra frente seus olhos embaçam sem acreditar no que vêem")
        time.sleep(4)
        print("Uma figura gigante, seu corpo parece se estender do chão e de algumas arvores, possui um grande manto verde cobrindo seu corpo")
        time.sleep(5)
        print("A figura não abre a boca, mas você pode ouvir ela falando dentro de sua mente... ")
        time.sleep(3)
        print('"Você parece assustado, não tenha medo, venha, já conhece como as coisas funcionam ou preciso te explicar?"')
        time.sleep(2)

        while (op < 0 or op > 2):
            print("1 - Não, por favor, me explique\n2 - Sim, não vou gastar seu tempo")
            op = int(input("1 ou 2. Digite sua resposta: "))
        time.sleep(1)
        print('"Pois bem, me chamo Frøya, entre meus irmãos, sou a mais benelovente, eu dou a vida, enquanto eles tiram..."')
        time.sleep(4)
        if (op == 1):
            print('"Aqui no nosso mundo, você enfrentará algumas batalhas, que o ajudarão a enfrentar dificuldades futuras"')
            time.sleep(3)
            print('"o dano é baseado nos nossos dados de 20 lados, e se o nosso inimigo sofrerá o dano ou não"')
            time.sleep(3)
            print('"é decidido pelo dado do mundo, um dado de 10 lados"')
            time.sleep(3)
            print('"Caso o número do dado do mundo seja par, o ataque é suscedido"')
            time.sleep(2.5)
            print('"Caso seja impar, o ataque é anulado"')
            time.sleep(3)
            print('"As cartas que você possui podem ser usadas durante as batalhas"')
            time.sleep(2.4)
            print('"Tome, pegue isso, te ajudará a sobreviver"')
            time.sleep(3)
            print("Ela te entrega uma carta com o desenho da própria Frøya")
            self.playerItems.append(["Espirito de Frøya", "Frøya, quem ela é? não sabemos, mas aparentemente essa carta possui um de seus espiritos, ao ser usada cura uma boa quantidade de vida"])
        print('"Então, vamos começar?"')

        
        self.counter += 1

    def map2(self):
        print("Hello World")
    
    def map3(self):
        print("Hello World")
    
    def story1(self):
        print(".", end="", sep=""); time.sleep(1); print(".", end="", sep=""); time.sleep(1); print(".", end="", sep=""); time.sleep(2)
        print("\nVocê acorda numa sala estranha, você está usando uma roupa que nunca viu na vida\nvocê vê apenas quatro portas, três delas a sua frente, e uma atrás")
        time.sleep(4)
        print("todas as portas tem um número e um simbolo acima delas")
        time.sleep(3)
        if (self.counter == 0):
            print("A porta de número um tem uma mão aberta")
            time.sleep(2)
            print("A porta de número dois tem uma mão com 2 dedos levantados")
            time.sleep(2)
            print("A porta de número três tem uma mão totalmente fechada")
            time.sleep(2)
            print("Aparentemente Pedra Papel e Tesoura??? é oq você presume")
            time.sleep(2)
            print("Já a quarta porta...")
            time.sleep(1.3)
            print("não tem simbolo, não tem número, apenas 3 cadeados grandes e correntes")
            time.sleep(3.5)
            print(".", end="", sep=""); time.sleep(1); print(".", end="", sep=""); time.sleep(1); print(".", end="", sep=""); time.sleep(2)
            print()
        elif (self.counter == 1):
            print("Ah, você lembrou, é aquilo do Pedra, Papel e Tesoura!")
            time.sleep(2)
            print("Será que tudo foi real, ou apenas um sonho?")
            time.sleep(2)
            print("Você escuta um barulho metálico, um dos cadeados que prediam a 4º porta quebra e desaparece")
            time.sleep(3.8)
            print("e a porta 1... desapareceu?? você vê apenas o símbolo, não há mais porta")
            time.sleep(2.4)
            print(".", end="", sep=""); time.sleep(1); print(".", end="", sep=""); time.sleep(1); print(".", end="", sep=""); time.sleep(2)
            print()

print("          ###\n         #####\n         #####\n         #####\n         #####\n         #####\n         #####\n         #####\n   #################\n   #################\n         #####\n         #####\n         #####\n         #####\n         #####\n         #####\n         #####\n         #####\n         #####\n         #####\n         #####\n          ###\n           #")
print("\n=-=-=Janken-Dice-Warrior=-=-=\n")

op = 0
newGame = game()
while(True):
    print("Menu\n")
    print("1 - iniciar", "\n2 - Instruções\n0 - Fechar Jogo", sep="")
    op = int(input("Digite sua opção: "))
    if (op == 1):
        newGame.start()
    elif (op == 2):
        print("")
    elif (op == 0):
        break
