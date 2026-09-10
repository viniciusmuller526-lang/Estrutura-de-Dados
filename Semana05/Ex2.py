#Crux Sacra Sit Mihi Lux

class Cliente:

    def __init__(self, nome):

        self.nome = nome
        self.proximo = None
        self.anterior = None

def menu():

    print("1 - Inserir cliente")
    print("2 - Remover cliente")
    print("3 - Simular rodízio")
    print("4 - Sair")
    opcao = int(input("Insira uma opção: "))
    return opcao

def inserir(lista, nome):

    cliente = Cliente(nome)
    
    if lista is None:
    
        cliente.proximo = cliente
        cliente.anterior = cliente
        lista = cliente
        return lista
    
    cliente.proximo = lista
    cliente.anterior = lista.anterior
    lista.anterior.proximo = cliente
    lista.anterior = cliente
    lista = cliente
    return lista

def remover(lista, cliente_a_remover):

    aux = lista

    if lista is None:

        print("Lista vazia")
        return

    while True:

        if aux.dado == cliente_a_remover:

            if aux.proximo == aux:

                print("Único elemento da lista")
                return None

            elif aux == lista:

                lista.proximo.anterior = lista.anterior
                lista.anterior.proximo = lista.proximo
                lista = lista.proximo
                return lista

            aux.proximo.anterior = aux.anterior
            aux.anterior.proximo = aux.proximo
            return lista

        elif aux.proximo == lista:

            print("Cliente não encontrado")
            return lista

        aux = aux.proximo

def simular(lista):

    aux = lista

    if lista is None:

        print("Lista vazia")
        return

    while True:

        print(" - ", aux.nome, "está com a pizza")

        if aux.proximo == lista:

            return

        aux = aux.proximo   

def main():

    lista = None
    opcao = 0

    while opcao != 4:

        opcao = menu()

        if opcao == 1:

            nome = input("Insira o nome do cliente: ")
            lista = inserir(lista, nome)

        elif opcao == 2:

            cliente_a_remover = input("Insira o nome do cliente a remover: ")
            lista = remover(lista, cliente_a_remover)

        elif opcao == 3:

            simular(lista)

main()
