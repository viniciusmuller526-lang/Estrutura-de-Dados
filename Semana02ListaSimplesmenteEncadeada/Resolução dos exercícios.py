#Crux Sacra Sit Mihi Lux

class No:

    def __init__(self, dado):

        self.dado = dado
        self.proximo = None

def menu():

    print("1 - Inserir")
    print("2 - Listar")
    print("3 - Retirar")
    print("4 - Achar valores maiores que n")
    print("5 - Achar último item")
    print("6 - Inserir no final da lista")
    print("7 - Calcular média")
    print("8 - Alterar sinal dos valores")
    print("9 - Sair")

    opcao = int(input("Digite a opcao:"))

    return opcao

def inserir(lista, dado):

    no = No(dado)

    if lista is None:

        lista = no
        return lista

    no.proximo = lista
    lista = no
    return lista

def listar(lista):

    aux = lista

    while aux != None:

        print(" - ", aux.dado)
        aux = aux.proximo

def remover(lista, dado):

    aux = lista
    anterior = None

    if lista == None:

        print("Lista vazia")
        return

    while aux != None:

        if aux.dado == dado:

            if aux == lista:

                lista = lista.proximo
                return lista

            else:

                anterior.proximo = aux.proximo
                return lista

        anterior = aux
        aux = aux.proximo

    print("Dado n encontrado")
    return lista

def maiores(lista, n):

    aux = lista
    dados_maiores_que_n = 0

    if lista == None:

        print("Lista Vazia")
        return

    while aux != None:

        if aux.dado > n:

            dados_maiores_que_n += 1

        aux = aux.proximo

    print(f"Há {dados_maiores_que_n} dados maiores que {n}")

def ultimo(lista):

    aux = lista

    if lista == None:
    
        print("Lista Vazia")
        return

    while aux != None:

        if aux.proximo == None:

            print(f"O último dado da lista é {aux.dado}")
            return

        aux = aux.proximo

def lista_insere_final(lista, valor):

    no = No(valor)
    aux = lista

    if lista is None:
    
        lista = no
        return lista

    else:

        while aux != None:    
    
            if aux.proximo is None:


                aux.proximo = no
                return lista

            aux = aux.proximo

def calcular_media(lista):

    aux = lista
    somatorio = 0
    dividendo = 0

    if lista == None:
    
        print("Lista Vazia")
        return

    while aux != None:

        somatorio += aux.dado
        dividendo += 1
        aux = aux.proximo

    media = somatorio / dividendo

    print(f"A média dos dados é {media}")

def alterar_sinal(lista):

    aux = lista

    while aux != None:

        aux.dado = -aux.dado
        aux = aux.proximo

    return lista
            
def main():

    lista = None
    opcao = 0

    while opcao != 9:

        opcao = menu()

        if opcao == 1:

            dado = float(input("Digite um dado:"))
            lista = inserir(lista, dado)

        elif opcao == 2:

            listar(lista)

        elif opcao == 3:

            dado = float(input("Dado para retirar: "))
            lista = remover(lista, dado)

        elif opcao == 4:

            n = float(input("Número de comparação: "))
            maiores(lista, n)

        elif opcao == 5:

            ultimo(lista)

        elif opcao == 6:

            valor = float(input("Insira um valor: "))
            lista = lista_insere_final(lista, valor)

        elif opcao == 7:

            calcular_media(lista)

        elif opcao == 8:

            lista = alterar_sinal(lista)

main()
