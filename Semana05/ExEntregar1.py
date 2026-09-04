#Crux Sacra Sit Mihi Lux

class Atleta:

    def __init__(self, id):

        self.id = id
        self.bastao = False
        self.proximo = None
        self.anterior = None

def menu():

    print("1 - Inserir atleta")
    print("2 - Remover atleta")
    print("3 - Simular passar bastão")
    print("4 - Sair")
    opcao = int(input("Insira uma opção: "))
    return opcao

def inserir(lista, id):

    atleta = Atleta(id)

    if lista is None:

        atleta.proximo = atleta
        atleta.anterior = atleta
        lista = atleta
        return lista

    atleta.proximo = lista
    atleta.anterior = lista.anterior
    lista.anterior.proximo = atleta
    lista.anterior = atleta
    lista = atleta
    return lista

def remover(lista, dado_remover):

    aux = lista

    if lista is None:

        print("Nope")
        return

    while True:

        if aux.dado == dado_remover:

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

            print("ID não encontrado")
            return lista

        aux = aux.proximo

def simular(lista):

    aux = lista
    contador = 5

    if lista is None:

        print("Lista vazia")
        return

    while contador != 0:

        print(f"ID: {aux.id}, Tem o bastão?: {aux.bastao}")
        
        if aux.proximo == lista:
        
            contador -= 1

        if contador == 4:

            lista.bastao = True

        if aux.bastao == True:

            aux.proximo.bastao = True
            aux.bastao = False

        aux = aux.proximo

def main():

    lista = None

    opcao = 0

    while opcao != 4:

        opcao = menu()

        if opcao == 1:

            id = int(input("Insira uma id: "))
            lista = inserir(lista, id)

        elif opcao == 2:

            id_remover = int(input("Insira o id que deseja remover: "))
            lista = remover(lista, id_remover)

        elif opcao == 3:

            simular(lista)

main()
