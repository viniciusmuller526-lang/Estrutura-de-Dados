#Crux Sacra Sit Mihi Lux

class No:

    def __init__(self, nome, id):

        self.nome = nome
        self.id = id
        self.anterior = None
        self.proximo = None

def menu():

    print("1 - Insirir nó")
    print("2 - Listar nós")
    print("3 - Remover nós")
    print("4 - Verificar se nó existe")
    print("5 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def submenu():

    print("1 - Pesquisar por nome")
    print("2 - Pesquisar por ID")
    escolha = int(input("Digite o método de procura: "))
    return escolha

def inserir(lista, nome, id):

    no = No(nome, id)

    if lista is None:

        lista = no
        return lista

    no.proximo = lista
    lista.anterior = no
    lista = no
    return lista

def listar(lista):

    aux = lista

    if lista is None:

        print("Lista vazia")
        return

    while aux != None:

        print(f"Nome: {aux.nome}, ID: {aux.id}")
        aux = aux.proximo

def remover(lista, id):

    aux = lista
    
    if lista is None:

        print("Lista vazia")
        return
    
    while aux != None:
    
        if aux.id == id:
    
            if aux.proximo == aux.anterior == None:
    
                lista = None
                return lista
    
            elif aux == lista:
    
                lista = lista.proximo
                lista.anterior = None
                return lista
    
            elif aux.proximo == None:
    
                aux.anterior.proximo = None
                return lista
    
            aux.proximo.anterior = aux.anterior
            aux.anterior.proximo = aux.proximo
            return lista
    
        aux = aux.proximo

    print("ID não encontrado")
    return lista

def verificar(lista, escolha):

    aux = lista

    if lista == None:

        print("Lista vazia")
        return

    if escolha == 2:

        id = int(input("Digite a ID do no que deseja verificar: "))

        while aux != None:

            if aux.id == id:

                print("Existe um nó com a ID informada")
                return

            aux = aux.proximo

        print("ID não encontrado")

    elif escolha == 1:

        nome = input("Digite o nome do no que deseja verificar: ")

        while aux != None:

            if aux.nome == nome:

                print("Existe um nó com o nome informado")
                return

            aux = aux.proximo

        print("Nome não encontrado")

def main():

    lista = None
    opc = 0

    while opc != 5:

        opc = menu()

        if opc == 1:

            nome = input("Insira um nome: ")
            id = int(input("Insira um ID: "))
            lista = inserir(lista, nome, id)

        elif opc == 2:

            listar(lista)

        elif opc == 3:

            id = int(input("Insira a ID do no que deseja remover: "))
            lista = remover(lista, id)

        elif opc == 4:

            escolha = submenu()
            verificar(lista, escolha)
            
main()
