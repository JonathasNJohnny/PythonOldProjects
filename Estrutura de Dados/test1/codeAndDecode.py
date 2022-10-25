from string import ascii_uppercase
alphabet = list(ascii_uppercase)

def code(message, key, option):
    codedMessage = ""
    for eachLetter in message:
        charUnicode = ord(eachLetter)-65
        codedMessage += alphabet[(charUnicode+key) %len(alphabet)] if eachLetter in alphabet else eachLetter
    if (option == 1):
        print("Sua mensagem codificada: ", end="")
    else:
        print("Sua mensagem decodificada: ", end="")        
    print(codedMessage, "\n")

def decode(message, key):
    code(message, len(alphabet)-key, option)


proceed = 1
option = 0
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("CODIFICAÇÃO COM CIFRA DE CESAR!")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
while (proceed != 0):
    option = int(input("\nDeseja codificar ou decodificar uma palavra?\nDigite\n1 para codificação\n2 para decodificação\nDigite sua opção: "))
    if (option == 1):
        code(input("\nDigite a palavra que deseja codificar: ").upper(), int(input("Digite a chave da codificação: ")), option)
    elif (option == 2):
        decode(input("\nDigite a palavra que deseja decodificar: ").upper(), int(input("Digite a chave da decodificação: ")))
    proceed = int(input("Deseja codificar ou decodificar outra palavra? Digite\n1 para sim\n0 para não\nEscolha sua opção: "))
