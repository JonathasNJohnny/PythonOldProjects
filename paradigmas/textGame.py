def printAll(list):
    print()
    for i in range(len(list)):
            print(list[i], end=" ")

def amongusPrint():
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠄⣀⣠⣤⣤⣤⣤⣤⣀⡀⠄⠈⠙⠿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⠇⠄⢀⣿⣿⣿⡟⠁⠄⣀⣀⣠⣤⣤⣤⣤⣄⣀⡀⠈⠙⢿⣿⣿")
    print("⣿⡿⠿⠟⠛⠛⠄⠄⣼⣿⣿⣿⠄⠄⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡀⠈⢻⣿")
    print("⣿⠁⠄⣠⣤⣤⠄⠄⣿⣿⣿⣿⡄⠄⠄⠄⠈⠙⠛⠛⠛⠛⠛⠛⠋⠉⠄⠄⢸⣿")
    print("⡟⠄⠄⣿⣿⡏⠄⠄⣿⣿⣿⣿⣷⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣿⣿")
    print("⡏⠄⠄⣿⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣤⣤⣤⣶⣶⣶⣿⠄⠄⢿⣿⣿")
    print("⠇⠄⢰⣿⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⢸⣿⣿")
    print("⡀⠄⠸⣿⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⢸⣿⣿")
    print("⣇⠄⠄⣿⣿⣧⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠄⠄⣿⣿⣿")
    print("⣿⣄⡀⠈⠉⠉⠄⠄⣿⣿⣿⣿⣿⣿⠛⠛⠛⠛⠛⠛⠛⢛⣿⣿⠃⠄⢸⣿⣿⣿")
    print("⣿⣿⣿⣶⣶⣶⠄⠄⢸⣿⣿⣿⣿⡏⠄⠄⢠⠄⠄⢰⣾⣿⣿⡏⠄⠄⣼⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⠄⠄⢸⣿⣿⣿⣿⡇⠄⠄⣿⣆⠄⠘⠿⠿⠿⠇⠄⣠⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣆⠄⠄⠈⠉⠉⠁⠄⢀⣸⣿⣿⣶⣤⣤⣤⣠⣤⣶⣿⣿⣿⣿⣿")

import random
import time
amongusPrint()
print("=-=-=-=-Bem Vindo a nave-=-=-=")
initialCrew = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impostor = random.choice(initialCrew)
print("\nEntre os", len(initialCrew), "membros da tripulação temos um assassino, seu trabalho é tentar encontra-lo, e joga-lo no espaço, porém, você só tem 6 vidas, caso mate alguém inocente, perde 1 vida, quando alguém morre, você também perde 1 vida\n")
print("Não é permitido voltar para ver como estavam os números anteriores, teste sua memória")
while(True):
    crew = initialCrew.copy()
    life = 6
    input(f"Pressione Enter Para Começar");
    print(".", end="", sep=""); time.sleep(1); print(".", end="", sep=""); time.sleep(1); print(".", end="", sep=""); time.sleep(2)
    print()
    while(life > 0):
        random.shuffle(crew)    
        printAll(crew)
        print()
        while (True):
            choice = input("(S ou N) Suspeita de alguém da nave?: ").upper()
            if (choice == "S" or choice == "N"):
                break
        if (choice == "S"):
            choice = 0
            while(crew.count(choice) == 0):
                if (initialCrew.count(choice) != 0):
                    print("\nO tripulante digitado já está morto!\n")
                choice = int(input("Digite o número de quem você acha que é o assassino: "))
            print(".", end="", sep=""); time.sleep(1); print(".", end="", sep=""); time.sleep(1); print(".", end="", sep=""); time.sleep(2)
            if (choice == impostor):
                crew[crew.index(impostor)] = ("Assassino: ", impostor)
                printAll(crew)
                print("\nParabéns, você encontrou o assassino ", impostor,", ele foi expulso da nave!\n", sep="")
                break
            else:
                life -= 1
                crew[crew.index(choice)] = "X"
                print("\nVocê acaba de matar um inocente! Perdeu 1 vida extra")
        if (crew.index(impostor) == 0):
            crew[crew.index(impostor)+1] = "X"
        elif (crew.index(impostor) == len(crew) - 1):
            crew[crew.index(impostor)-1] = "X"
        else:
            crew[crew.index(impostor) - random.choice([-1, 1])] = "X"
        life -= 1
        if (life < 1):
            print("Você demorou demais, o assassino te matou!")
            break
        amongusPrint()
