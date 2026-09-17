#Crux Sacra Sit Mihi Lux

class Jogador:

    def __init__(self, nome):

        self.nome = nome
        self.proximo = None
        self.anterior = None

def menu():

    print("1 - Inserir jogador")
    print("2 - Simular 1 rodada")
    print("3 - Simular N rodadas")
    print("4 - Mostrar fila")
    print("5 - Mostrar pŕoximo a jogar")
    print("6 - Limpar fila")
    print("7 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def inserir(fila_inicio, fila_fim, nome):

    jogador = Jogador(nome)

    if fila_inicio is None:

        fila_inicio = jogador
        fila_fim = jogador
        return fila_inicio, fila_fim

    fila_fim.proximo = jogador
    jogador.anterior = fila_fim
    fila_fim = jogador
    return fila_inicio, fila_fim

def simular_uma_vez(fila_inicio, fila_fim):

    aux = fila_inicio

    print(f"Jogador {fila_inicio.nome} jogou")

    fila_inicio = fila_inicio.proximo
    fila_inicio.anterior = None
    fila_fim.proximo = aux
    aux.anterior = fila_fim
    aux.proximo = None
    fila_fim = aux
    return fila_inicio, fila_fim

def mostrar_fila(fila_inicio):

    aux = fila_inicio
    contador = 1

    if fila_inicio is None:

        print("Fila vazia")
        return

    while aux != None:

        print(f"{contador} = {aux.nome}")
        contador += 1
        aux = aux.proximo

def mostrar_proximo(fila_inicio):

    if fila_inicio is None:

        print("Não há jogadores esperando na fila")
        return

    print(f"- {fila_inicio.nome} é o proximo jogador")

def limpar(fila_inicio, fila_fim):

    fila_inicio = None
    fila_fim = None

    return fila_inicio, fila_fim

def main():

    fila_inicio = None
    fila_fim = None
    opcao = 0

    while opcao != 7:

        opcao = menu()

        if opcao == 1:

            nome = input("Insira o nome do jogador: ")
            fila_inicio, fila_fim = inserir(fila_inicio, fila_fim, nome)

        elif opcao == 2:

            fila_inicio, fila_fim = simular_uma_vez(fila_inicio, fila_fim)

        elif opcao == 3:

            quantidade = int(input("Insira a quantidade de vezes que deseja simular: "))

            for _ in range(quantidade):

                fila_inicio, fila_fim = simular_uma_vez(fila_inicio, fila_fim)

        elif opcao == 4:

            mostrar_fila(fila_inicio)

        elif opcao == 5:

            mostrar_proximo(fila_inicio)

        elif opcao == 6:

            fila_inicio, fila_fim = limpar(fila_inicio, fila_fim)

main()
