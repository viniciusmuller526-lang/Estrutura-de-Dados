#Crux Sacra Sit Mihi Lux

class No():

    def __init__(self, dado):

        self.dado = dado
        self.proximo = None

def menu():

    print("1 - Empilhar dado")
    print("2 - Desempilhar dado do topo")
    print("3 - Percorrer pilha")
    print("4 - Ver dado do topo")
    print("5 - Verificar se a pilha está vazia")
    print("6 - Ver tamanho da pilha")
    print("7 - Calcular média da pilha")
    print("8 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def empilhar(pilha, dado):
    
    no = No(dado)

    if pilha is None:
        pilha = no
        return pilha

    no.proximo = pilha
    pilha = no
    return pilha

def desempilhar(pilha):

    pilha = pilha.proximo
    return pilha

def percorrer_pilha(pilha):

    aux = pilha

    if pilha is None:

        print("Pilha vazia")
        return

    while aux != None:

        print(f"- {aux.dado}")
        aux = aux.proximo

def ver_dado_topo(pilha):

    print(f"- {pilha.dado}")

def verificar_pilha(pilha):

    if pilha is None:

        print("Pilha vazia")

    else:

        print("Pilha possui elementos")

def tamanho(pilha):

    aux = pilha
    contador = 0

    if pilha is None:

        print("Pilha vazia")
        return

    while aux != None:

        contador += 1
        aux = aux.proximo

    print(f"Há {contador} elementos na pilha")

def media(pilha):

    aux = pilha
    somador = 0
    divisor = 0

    if pilha is None:

        print("Pilha vazia")
        return

    while aux != None:

        somador += aux.dado
        divisor += 1
        aux = aux.proximo

    print(f"A média da pilha é de: {somador/divisor}")

def main():

    pilha = None
    opcao = 0

    while opcao != 8:

        opcao = menu()

        if opcao == 1:

            dado = int(input("Insira um dado: "))
            pilha = empilhar(pilha, dado)

        elif opcao == 2:

            pilha = desempilhar(pilha)

        elif opcao == 3:

            percorrer_pilha(pilha)

        elif opcao == 4:

            ver_dado_topo(pilha)

        elif opcao == 5:

            verificar_pilha(pilha)

        elif opcao == 6:

            tamanho(pilha)

        elif opcao == 7:

            media(pilha)

main()
