#Crux Sacra Sit Mihi Lux

class Paciente:

    def __init__(self, nome, idade, prioridade):

        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
        self.proximo = None
        self.anterior = None

def menu():

    print("1 - Inserir paciente")
    print("2 - Remover paciente atendido")
    print("3 - Listar pacientes")
    print("4 - Atender paciente")
    print("5 - Sair")
    opcao = int(input("Insira uma opção: "))
    return opcao

def inserir(lista, nome, idade, prioridade):

    paciente = Paciente(nome, idade, prioridade)

    if lista is None:

        paciente.proximo = paciente
        paciente.anterior = paciente
        lista = paciente
        return lista

    paciente.proximo = lista
    paciente.anterior = lista.anterior
    lista.anterior.proximo = paciente
    lista.anterior = paciente
    lista = paciente
    return lista

def remover(lista, nome_a_remover):

    if lista is None:

        print("Lista vazia")
        return None

    aux = lista

    while True:
        if aux.nome.lower() == nome_a_remover.lower():
            
            if aux.proximo == aux:
                print(f"Paciente '{aux.nome}' removido.")
                return None

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == lista:
                lista = aux.proximo

            print(f"Paciente '{aux.nome}' removido.")
            return lista

        aux = aux.proximo
        if aux == lista:
            break

    print("Paciente não encontrado.")
    return lista

def listar(lista):

    aux = lista

    if lista is None:

        print("Lista vazia")
        return

    while True:

        print(f"Nome: {aux.nome}, Idade: {aux.idade}, Prioridade: {aux.prioridade}")

        if aux.proximo == lista:

            return

        aux = aux.proximo

def chamar_paciente_urgente(lista):

    if lista is None:
        print("Lista vazia")
        return None

    nivel_urgencia = {
        "emergência": 5, "emergencia": 5,
        "muito urgente": 4,
        "urgente": 3,
        "pouco urgente": 2,
        "não urgente": 1, "nao urgente": 1
    }

    aux = lista
    maior_urgencia = lista
    maior_prioridade = nivel_urgencia.get(lista.prioridade.lower(), 0)

    while True:
        prioridade_atual = nivel_urgencia.get(aux.prioridade.lower(), 0)
        if prioridade_atual > maior_prioridade:
            maior_urgencia = aux
            maior_prioridade = prioridade_atual

        aux = aux.proximo
        if aux == lista:
            break

    print(f"\nPaciente prioritário encontrado! Nome: {maior_urgencia.nome}, Idade: {maior_urgencia.idade}, Prioridade: {maior_urgencia.prioridade}")

    return remover(lista, maior_urgencia.nome)

def main():

    lista = None
    opcao = 0

    while opcao != 5:

        opcao = menu()

        if opcao == 1:

            nome = input("Insira o nome do paciente: ")
            idade = int(input("Insira a idade do paciente: "))
            prioridade = input("Insira o nível de prioridade do paciente: ")
            lista = inserir(lista, nome, idade, prioridade)

        elif opcao == 2:

            nome_a_remover = input("Insira o nome do paciente que deseja remover: ")
            lista = remover(lista, nome_a_remover)

        elif opcao == 3:

            listar(lista)

        elif opcao == 4:

            lista = chamar_paciente_urgente(lista)

main()
