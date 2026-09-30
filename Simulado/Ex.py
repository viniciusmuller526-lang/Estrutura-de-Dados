#Crux Sacra Sit Mihi Lux

class No:

    def __init__(self, id, nome):

        self.id = id
        self.nome = nome
        self.status = True
        self.anterior = None
        self.proximo = None

def inserir(lista, id, nome):

    no = No(id, nome)

    if lista is None:

        lista = no
        return lista

    no.proximo = lista
    lista.anterior  = no
    lista = no
    return lista

def remover(lista, id_a_remover):

    aux = lista

    if lista is None:

        print("Lista vazia")
        return

    while aux != None:

        if aux.id == id_a_remover:

            if aux == lista:

                lista = lista.proximo
                
                if lista is not None:
                
                    lista.anterior = None
                
                return lista

            aux.anterior.proximo = aux.proximo
            
            if aux.proximo != None:
                
                aux.proximo.anterior = aux.anterior

            return lista

        aux = aux.proximo

    return  lista

def ligar_desligar(lista, id):

    aux = lista

    if lista is None:

        print("Lista vazia")
        return

    while aux != None:

        if aux.id == id:

            if aux.status == True:

                aux.status = False
                return lista

            else:

                aux.status = True
                return lista

        aux = aux.proximo

    return lista

def percorrer(lista):

    aux = lista

    if lista is None:

        print("Lista vazia")
        return

    while aux != None:

        print(f"- {aux.id}, {aux.nome}, {aux.status}")
        aux = aux.proximo

def percorrer_contrario(lista):

    aux = lista

    if lista is None:

        print("Lista vazia")
        return

    while aux.proximo != None:

        aux = aux.proximo

    while aux != None:

        print(f"- {aux.id}, {aux.nome}, {aux.status}")
        aux = aux.anterior

def menu():

    print("1 - Inserir")
    print("2 - Remover")
    print("3 - Alterar status")
    print("4 - Listar")
    print("5 - Listar ao contrário")
    print("6 - Sair")

    opcao = int(input("Digite uma opção: "))
    return opcao

def main():

    lista = None
    opcao = 0

    while opcao != 6:

        opcao = menu()

        if opcao == 1:

            id = int(input("Insira uma ID: "))
            nome = input("Digite um nome: ")
            lista = inserir(lista, id, nome)

        elif opcao == 2:

            id_a_remover = int(input("Insira uma ID a remover: "))
            lista = remover(lista, id_a_remover)

        elif opcao == 3:

            id_a_alterar = int(input("Insira uma ID que deseja mudar o status: "))
            lista = ligar_desligar(lista, id_a_alterar)

        elif opcao == 4:

            percorrer(lista)

        elif opcao == 5:

            percorrer_contrario(lista)

main()
