#Crux Sacra Sit Mihi Lux

class Solicitacao:

    def __init__(self, usuario, tempo_espera):

        self.usuario = usuario
        self.tempo_espera = tempo_espera
        self.anterior = None
        self.proximo = None

def menu():

    print("1 - Enfileirar")
    print("2 - Desenfileirar")
    print("3 - Percorrer")
    print("4 - Ver próximo na fila")
    print("5 - Verificar se há pessoas na fila")
    print("6 - Verificar tamanho da fila")
    print("7 - Calcular tempo de espera médio da fila")
    print("8 - Sair")
    opcao = int(input("Digite uma opcão: "))
    return opcao

def enfileirar(fila_inicio, fila_fim, usuario, tempo_espera):

    solicitacao = Solicitacao(usuario, tempo_espera)

    if fila_inicio == fila_fim == None:

        fila_inicio = solicitacao
        fila_fim = solicitacao
        return fila_inicio, fila_fim

    solicitacao.anterior = fila_fim
    fila_fim.proximo = solicitacao
    fila_fim = solicitacao
    return fila_inicio, fila_fim

def desenfileirar(fila_inicio, fila_fim):

    if fila_inicio == fila_fim == None:

        print("Fila vazia")
        return None, None

    if fila_inicio == fila_fim:

        print("Último usuário na fila")
        return None, None

    fila_inicio = fila_inicio.proximo
    fila_inicio.anterior = None
    print("Usuário atendido")
    return fila_inicio, fila_fim

def percorrer(fila_inicio):

    aux = fila_inicio

    if fila_inicio is None:

        print("Fila vazia")
        return

    while aux != None:

        print(f"- {aux.usuario}")
        aux = aux.proximo

def ver_usuario_topo(fila_inicio):

    if fila_inicio is None:

        print("Fila vazia")
        return

    print(f"- {fila_inicio.usuario}")

def verificar_fila(fila_inicio):

    if fila_inicio is None:

        print("Fila vazia")

    else:

        print("Fila possui elementos")

def tamanho(fila_inicio):

    aux = fila_inicio
    contador = 0

    if fila_inicio is None:

        print("Fila vazia")
        return

    while aux != None:

        contador += 1
        aux = aux.proximo

    print(f"Há {contador} usuarios na fila")

def media(fila_inicio):

    aux = fila_inicio
    somador = 0
    divisor = 0

    if fila_inicio is None:

        print("Fila vazia")
        return

    while aux != None:

        somador += aux.tempo_espera
        divisor += 1
        aux = aux.proximo

    print(f"O tempo de espera médio da fila é de: {somador / divisor} minutos")

def main():

    fila_inicio = None
    fila_fim = None

    opcao = 0

    while opcao != 8:

        opcao = menu()

        if opcao == 1:

            usuario = input("Insira o nome do usuartio: ")
            tempo_espera = int(input("Insira o tempo de espera em minutos: "))
            fila_inicio, fila_fim = enfileirar(fila_inicio, fila_fim, usuario, tempo_espera)

        elif opcao == 2:

            fila_inicio, fila_fim = desenfileirar(fila_inicio, fila_fim)

        elif opcao == 3:

            percorrer(fila_inicio)

        elif opcao == 4:

            ver_usuario_topo(fila_inicio)

        elif opcao == 5:

            verificar_fila(fila_inicio)

        elif opcao == 6:

            tamanho(fila_inicio)

        elif opcao == 7:

            media(fila_inicio)
    
main()
