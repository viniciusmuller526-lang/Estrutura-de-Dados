#Crux Sacra Sit Mihi Lux

class Parada:

    def __init__(self, num_parada):

        self.num_parada = num_parada
        self.bastao = False
        self.proximo = None
        self.anterior = None

def menu():

    print("1 - Inserir parada")
    print("2 - Remover parada")
    print("3 - Simular percurso")
    print("4 - Sair")
    opcao = int(input("Insira uma opção: "))
    return opcao

def inserir(lista, num_parada):

    parada = Parada(num_parada)

    if lista is None:

        parada.proximo = parada
        parada.anterior = parada
        lista = parada
        return lista

    parada.proximo = lista
    parada.anterior = lista.anterior
    lista.anterior.proximo = parada
    lista.anterior = parada
    lista = parada
    return lista

def remover(lista, dado_remover):

    aux = lista

    if lista is None:

        print("Nope")
        return

    while True:

        if aux.dado == dado_remover:

            if aux.proximo == aux:

                print("Única parada da lista")
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

            print("Parada não encontrada")
            return lista

        aux = aux.proximo

def simular(lista):

    aux = lista

    if lista is None:

        print("Lista Vazia")
        return

    while True:

        print(f"O ônibus está na parada {aux.num_parada}")

        if aux.proximo == lista:

            return

        aux = aux.proximo

def main():

    lista = None

    opcao = 0

    while opcao != 4:

        opcao = menu()

        if opcao == 1:

            num_parada = int(input("Insira o número da parada: "))
            lista = inserir(lista, num_parada)

        elif opcao == 2:

            parada_remover = int(input("Insira o número da parada que deseja remover: "))
            lista = remover(lista, parada_remover)

        elif opcao == 3:

            simular(lista)

main()
