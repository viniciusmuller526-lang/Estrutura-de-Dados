#Crux Sacra Sit Mihi Lux

class Cliente:

    def __init__(self, nome):

        self.nome = nome
        self.proximo = None
        self.anterior = None

def menu():

    print("1 - Inserir cliente")
    print("2 - Atender")
    print("3 - Contar clientes")
    print("4 - Mostrar próximo cliente na fila")
    print("5 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def inserir(fila_inicio, fila_fim, nome):

    cliente = Cliente(nome)

    if fila_inicio is None:

        fila_inicio = cliente
        fila_fim = cliente
        return fila_inicio, fila_fim

    fila_fim.proximo = cliente
    cliente.anterior = fila_fim
    fila_fim = cliente
    return fila_inicio, fila_fim

def atender(fila_inicio, fila_fim):

    if fila_inicio is None:

        print("Fila vazia")
        return None, None

    if fila_inicio == fila_fim:
        print("Único cliente na fila")
        print(f"- {fila_inicio.nome} foi atendido")
        return None, None

    print(f"- {fila_inicio.nome} foi atendido")
    fila_inicio = fila_inicio.proximo
    fila_inicio.anterior = None
    return fila_inicio, fila_fim

def quantidade(fila_inicio):

    aux = fila_inicio
    contador = 0

    if fila_inicio is None:

        print("Não há ninguém na fila")
        return

    while aux != None:

        contador += 1
        aux = aux.proximo

    print(f"Há {contador} clientes esperando atendimento")

def proximo_cliente(fila_inicio):

    if fila_inicio is None:

        print("Não há clientes esperando na fila")
        return

    print(f"- {fila_inicio.nome} é o proximo cliente")

def main():

    fila_inicio = None
    fila_fim = None
    opcao = 0

    while opcao != 5:

        opcao = menu()

        if opcao == 1:

            nome = input("Insira o nome do cliente: ")
            fila_inicio, fila_fim = inserir(fila_inicio, fila_fim, nome)

        elif opcao == 2:

            fila_inicio, fila_fim = atender(fila_inicio, fila_fim)

        elif opcao == 3:

            quantidade(fila_inicio)

        elif opcao == 4:
        
            proximo_cliente(fila_inicio)

main()
