#Crux Sacra Sit Mihi Lux

class Operacao:

    def __init__(self, operacao):

        self.operacao = operacao
        self.proximo = None

def menu():

    print("1 - Inserir operação")
    print("2 - Listar operações")
    print("3 - Listar última operação adicionada")
    print("4 - Remover última operação")
    print("5 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def inserir(pilha, operacao):

    novo = Operacao(operacao) 

    if pilha is None:

        pilha = novo
        return pilha

    novo.proximo = pilha
    pilha = novo
    return pilha

def listar(pilha):

    aux = pilha
    contador = 1

    if pilha is None:

        print("Pilha vazia")
        return

    while aux is not None:

        print(f"{contador} - {aux.operacao}")
        contador += 1
        aux = aux.proximo

def listar_ultima(pilha):

    print(f"- {pilha.operacao}")

def remover(pilha):

    return pilha.proximo

def main():

    pilha = None
    opcao = 1

    while opcao != 5:

        opcao = menu()

        if opcao == 1:

            operacao = input("Insira uma operação matemática: ")
            pilha = inserir(pilha, operacao)

        elif opcao == 2:

            listar(pilha)

        elif opcao == 3:

            listar_ultima(pilha)

        elif opcao == 4:

            pilha = remover(pilha)

main()
