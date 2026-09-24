#Crux Sacra Sit Mihi Lux

class NoDuploCircular:

    def __init__(self, dado):

        self.dado = dado
        self.proximo = None
        self.anterior = None

def menu():

    print("1 - Adicionar dado")
    print("2 - Adicionar dado no final")
    print("3 - Listar dados")
    print("4 - Listar dados de trás para frente")
    print("5 - Remover dado")
    print("6 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def adicionar(lista, dado):

    noduplocircular = NoDuploCircular(dado)

    if lista is None:

        noduplocircular.anterior = noduplocircular
        noduplocircular.proximo = noduplocircular
        lista = noduplocircular
        return lista

    noduplocircular.proximo = lista
    noduplocircular.anterior = lista.anterior
    lista.anterior.proximo = noduplocircular
    lista.anterior = noduplocircular
    lista = noduplocircular
    return lista

def adicionar_final(lista, dado):

    noduplocircular = NoDuploCircular(dado)

    if lista is None:
    
        noduplocircular.anterior = noduplocircular
        noduplocircular.proximo = noduplocircular
        lista = noduplocircular
        return lista

    noduplocircular.proximo = lista
    noduplocircular.anterior = lista.anterior
    lista.anterior.proximo = noduplocircular
    lista.anterior = noduplocircular
    return lista

def listar(lista):

    aux = lista

    if lista is None:

        print("Lista vazia!")
        return

    while True:
      
        print(f"- {aux.dado}")

        if aux.proximo == lista:

            return

        aux = aux.proximo

def listar_contrario(lista):

    aux = lista

    if lista is None:

        print("Lista vazia!")
        return

    while True:

        aux = aux.anterior

        print(f"- {aux.dado}")

        if aux.anterior == lista:

            aux = aux.anterior
            print(f"- {aux.dado}")        
            return

def remover(lista, dado_a_remover):

    if lista is None:

        print("Lista vazia")
        return None

    aux = lista

    while True:

        if aux.dado == dado_a_remover:
            
            if aux.proximo == aux:
                print(f"Dado {aux.dado}, removido")
                return None

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == lista:
                lista = aux.proximo

                print(f"Dado {aux.dado}, removido")

            return lista

        aux = aux.proximo

        if aux == lista:
            break

    print("Dado não encontrado.")
    return lista
                

def main():

    lista = None
    opcao = 0

    while opcao != 6:

        opcao = menu()

        if opcao == 1:

            dado = int(input("Insira um dado: "))
            lista = adicionar(lista, dado)

        elif opcao == 2:

            dado = int(input("Insira um dado: "))
            lista = adicionar_final(lista, dado)

        elif opcao == 3:

            listar(lista)

        elif opcao == 4:

            listar_contrario(lista)

        elif opcao == 5:

            dado_a_remover = int(input("Insira o dado que deseja remover: "))
            lista = remover(lista, dado_a_remover)
            
main()
