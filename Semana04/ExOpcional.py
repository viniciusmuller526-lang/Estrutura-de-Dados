#Crux Sacra Sit Mihi Lux

class No:

    def __init__(self, valor):

        self.valor = valor
        self.anterior = None
        self.proximo = None

def menu():

    print("1 - Inserir no início")
    print("2 - Inserir no final")
    print("3 - Exibir do primeiro até o último elemento")
    print("4 - Exibir do último até o primeiro elemento")
    print("5 - Remover um elemento")
    print("6 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def inserir_inicio(lista, valor):

    no = No(valor)

    if lista is None:

        lista = no
        return lista

    lista.anterior = no
    no.proximo = lista
    lista = no
    return lista

def inserir_final(lista, valor):

    no = No(valor)
    aux = lista

    if lista is None:

        lista = no
        return lista

    while aux.proximo != None:

        aux = aux.proximo

    aux.proximo = no
    no.anterior = aux
    return lista

def listar_primeiro_ultimo(lista):

    aux = lista

    if lista is None:

        print("Lista Vazia!")
        return

    while aux != None:

        print(f"Valor: {aux.valor}")

        aux = aux.proximo

def listar_ultimo_primeiro(lista):

    aux = lista

    if lista is None:
    
        print("Lista Vazia!")
        return
    
    while aux.proximo != None:

        aux = aux.proximo

    while aux != None:

        print(f"Valor: {aux.valor}")
        aux = aux.anterior

def remover(lista, valor_remover):

    aux = lista

    if lista is None:

        print("Lista Vazia!")
        return

    while aux != None:
    
        if aux.valor == valor_remover:
    
            if aux.proximo == aux.anterior == None:
    
                lista = None
                print("Valor removido")
                return lista
    
            elif aux == lista:
    
                lista = lista.proximo
                lista.anterior = None
                print("Valor removido")
                return lista
    
            elif aux.proximo == None:
    
                aux.anterior.proximo = None
                print("Valor removido")
                return lista
    
            aux.proximo.anterior = aux.anterior
            aux.anterior.proximo = aux.proximo
            print("Valor removido")
            return lista
    
        aux = aux.proximo

    print("Valor não encontrado")
    return lista

def main():

    lista = None
    opcao = 0

    while opcao != 6:

        opcao = menu()

        if opcao == 1:

            valor = int(input("Insira um valor: "))
            lista = inserir_inicio(lista, valor)

        elif opcao == 2:

            valor = int(input("Insira um valor: "))
            lista = inserir_final(lista, valor)

        elif opcao == 3:

            listar_primeiro_ultimo(lista)

        elif opcao == 4:

            listar_ultimo_primeiro(lista)

        elif opcao == 5:

            valor_remover = int(input("Insira o valor que deseja remover: "))
            lista = remover(lista, valor_remover)

main()
