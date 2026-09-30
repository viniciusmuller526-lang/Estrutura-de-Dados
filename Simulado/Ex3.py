#Crux Sacra Sit Mihi Lux

class No:

    def __init__(self, nome, duracao, ambiente):

        self.nome = nome
        self.duracao = duracao
        self.ambiente = ambiente
        self.ativo = True
        self.anterior = None
        self.proximo = None

def inserir(lista, nome, duracao, ambiente):

    no = No(nome, duracao, ambiente)

    if lista is None:

        no.anterior = no
        no.proximo = no
        lista = no
        return lista

    no.proximo = lista
    no.anterior = lista.anterior
    lista.anterior.proximo = no
    lista.anterior = no
    lista = no
    return lista

def listar_ordem(lista):

    ambientes = ["Teste", "Homologação", "Produção"]

    if lista is None:

        print("Lista vazia")
        return

    for _ in range(len(ambientes)):

        aux = lista

        while True:

            if aux.ambiente == ambientes[_]:

                print(f"- {aux.nome}, {aux.duracao}, {aux.ambiente}, {aux.ativo}")
            
            aux = aux.proximo

            if aux == lista:

                break

def listar_ativos(lista):

    aux = lista

    if lista is None:

        print("Lista vazia")
        return

    while True:

        if aux.ativo == True:

            print(f"- {aux.nome}, {aux.duracao}, {aux.ambiente}, {aux.ativo}")

        aux = aux.proximo

        if aux == lista:

            break

def exibir_tempo(lista):

    aux = lista

    if lista is None:

        print("Lista vazia")
        return

    contador = 0

    while True:

        contador += aux.duracao
        aux = aux.proximo

        if aux == lista:

            break

    print(f"Tempo total da lista: {contador} segundos")

def ativar(lista, nome_ativar):

    aux = lista

    if lista is None:

        print("Lista vazia")
        return

    while True:

        if aux.nome == nome_ativar:

            aux.ativo = True
            return lista

        aux = aux.proximo

        if aux == lista:

            return lista

def desativar(lista, nome_desativar):

    aux = lista

    if lista is None:

        print("Lista vazia")
        return

    while True:

        if aux.nome == nome_desativar:

            aux.ativo = False
            return lista

        aux = aux.proximo

        if aux == lista:

            return lista

def remover(lista, nome_a_remover):

    aux = lista

    if lista is None:

        print("Lista vazia")
        return

    while True:

        if aux.nome == nome_a_remover:

            if aux.proximo == aux:

                print("Único item na lista")
                return None

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == lista:

                lista = lista.proximo
            
            return lista

        aux = aux.proximo

        if aux == lista:

            return lista

def menu():

    print("1 - Inserir")
    print("2 - Listar ordem")
    print("3 - Listar ativos")
    print("4 - Exibir tempo")
    print("5 - Ativar")
    print("6 - Desativar")
    print("7 - Remover")
    print("8 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def main():

    lista = None
    opcao = 0

    while opcao != 8:

        opcao = menu()

        if opcao == 1:
            
            nome = input("Insira um nome: ")
            duracao = int(input("Insira a duração do processo(em segundos): "))
            ambiente = input("Insira o ambiente: ")
            lista = inserir(lista, nome, duracao, ambiente)

        elif opcao == 2:

            listar_ordem(lista)

        elif opcao == 3:

            listar_ativos(lista)

        elif opcao == 4:

            exibir_tempo(lista)

        elif opcao == 5:

            nome_ativar = input("Insira o nome do processo que deseja ativar: ")
            lista = ativar(lista, nome_ativar)

        elif opcao == 6:

            nome_desativar = input("Insira o nome do processo que deseja desativar: ")
            lista = desativar(lista, nome_desativar)

        elif opcao == 7:

            nome_a_remover = input("Insira o nome do processo que deseja remover: ")
            lista = remover(lista, nome_a_remover)

main()
