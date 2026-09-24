#Crux Sacra Sit Mihi Lux

class NoDuplo:

    def __init__(self, nome):

        self.nome = nome
        self.proximo = None
        self.anterior = None

def menu():

    print("1 - Adicionar jogador")
    print("2 - Listar jogadores")
    print("3 - Listar jogadores em ordem reversa")
    print("4 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def adicionar_jogador(lista, nome):

    noduplo = NoDuplo(nome)

    if lista is None:

        lista = noduplo
        return lista

    lista.anterior = noduplo
    noduplo.proximo = lista
    lista = noduplo
    return lista

def percorrer_lista(lista):

    aux = lista

    if lista is None:

        print("Lista vazia!")
        return

    while aux is not None:

        print(f"- {aux.nome}")
        aux = aux.proximo

def percorrer_lista_contrario(lista):

    aux = lista

    if lista is None:

        print("Lista vazia!")
        return

    while aux.proximo is not None:

        aux = aux.proximo

    while aux is not None:

        print(f"- {aux.nome}")
        aux = aux.anterior

def main():

    lista = None
    opcao = 0

    while opcao != 4:

        opcao = menu()

        if opcao == 1:

            nome = input("Insira o nome do jogador: ")
            lista = adicionar_jogador(lista, nome)

        elif opcao == 2:

            percorrer_lista(lista)

        elif opcao == 3:

            percorrer_lista_contrario(lista)

main()
