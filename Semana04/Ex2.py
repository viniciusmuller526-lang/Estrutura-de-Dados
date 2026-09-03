#Crux Sacra Sit Mihi Lux

class Paciente:

    def __init__(self, codigo, nome, idade, prioridade):

        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
        self.proximo = None
        self.anterior = None

def menu():

    print("1 - Cadastrar um paciente")
    print("2 - Remover um paciente após o atendimento")
    print("3 - Localizar um paciente pelo código")
    print("4 - Atender um paciente mais urgente")
    print("5 - Listar os pacientes do primeiro para o último")
    print("6 - Listar todos os pacientes pela prioridade do atendimento")
    print("7 - Listar os pacientes do último para o primeiro")
    print("8 - Informar quantos pacientes aguardam atendimento")
    print("9 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def cadastrar(lista, codigo, nome, idade, prioridade):

    paciente = Paciente(codigo, nome, idade, prioridade)

    if lista is None:

        lista = paciente
        return lista

    paciente.proximo = lista
    lista.anterior = paciente
    lista = paciente
    return lista

def remover(lista, codigo_a_remover):

    aux = lista
    
    if lista is None:

        print("Lista vazia")
        return
    
    while aux != None:
    
        if aux.codigo == codigo_a_remover:
    
            if aux.proximo == aux.anterior == None:
    
                lista = None
                print("Paciente removido")
                return lista
    
            elif aux == lista:
    
                lista = lista.proximo
                lista.anterior = None
                print("Paciente removido")
                return lista
    
            elif aux.proximo == None:
    
                aux.anterior.proximo = None
                print("Paciente removido")
                return lista
    
            aux.proximo.anterior = aux.anterior
            aux.anterior.proximo = aux.proximo
            print("Paciente removido")
            return lista
    
        aux = aux.proximo

    print("Código não encontrado")
    return lista

def encontrar(lista, codigo_a_encontrar):

    aux = lista

    if lista is None:
    
        print("Lista vazia")
        return

    while aux != None:

        if aux.codigo == codigo_a_encontrar:

            print(f"Paciente encontrado! Código: {aux.codigo}, Nome: {aux.nome}, Idade: {aux.idade}, Prioridade: {aux.prioridade}")
            return

        aux = aux.proximo

    print("Código não encontrado")
    return

def chamar_paciente_urgente(lista):

    aux = lista

    if lista is None:
        
        print("Lista vazia")
        return

    nivel_urgencia = {

        "Emergência": 5,
        "Muito urgente": 4,
        "Urgente": 3,
        "Pouco urgente": 2,
        "Não urgente": 1

    }

    maior_urgencia = None
    maior_prioridade = 0

    while aux != None:

        if nivel_urgencia[aux.prioridade] > maior_prioridade:

            maior_urgencia = aux
            maior_prioridade = nivel_urgencia[aux.prioridade]

        aux = aux.proximo

    print(f"Paciente prioritário encontrado!, Código: {maior_urgencia.codigo}, Nome: {maior_urgencia.nome}, Idade: {maior_urgencia.idade}, Prioridade: {maior_urgencia.prioridade}")
        
def listar_primeiro_ultimo(lista):

    aux = lista

    while aux != None:

        print(f"Código: {aux.codigo}, Nome: {aux.nome}, Idade: {aux.idade}, Prioridade: {aux.prioridade}")

        aux = aux.proximo

def listar_por_prioridade(lista):

    if lista is None:
            
        print("Lista vazia")
        return

    nivel_urgencia = {
    
        "Emergência": 5,
        "Muito urgente": 4,
        "Urgente": 3,
        "Pouco urgente": 2,
        "Não urgente": 1
    
    }

    for nivel_prioritário in range(5,0,-1):

        aux = lista

        while aux != None:

            if nivel_urgencia[aux.prioridade] == nivel_prioritário:

                print(f"Código: {aux.codigo}, Nome: {aux.nome}, Idade: {aux.idade}, Prioridade: {aux.prioridade}")

            aux = aux.proximo

def listar_ultimo_primeiro(lista):

    aux = lista

    while aux.proximo != None:

        aux = aux.proximo

    while aux != None:

        print(f"Código: {aux.codigo}, Nome: {aux.nome}, Idade: {aux.idade}, Prioridade: {aux.prioridade}")
        aux = aux.anterior

def contabilizar_pacientes(lista):

    aux = lista
    contador = 0

    while aux != None:

        contador += 1
        aux = aux.proximo

    print(f"Há {contador} pacientes esperando atendimento")

def main():

    lista = None
    opcao = 0

    while opcao != 9:

        opcao = menu()

        if opcao == 1:

            codigo = int(input("Insira o código do paciente: "))
            nome = input("Insira o nome do paciente: ")
            idade = int(input("Insira a idade do paciente: "))
            prioridade = input("Insira o nível de prioridade do paciente: ")
            lista = cadastrar(lista, codigo, nome, idade, prioridade)

        elif opcao == 2:

            codigo_a_remover = int(input("Insira o código do paciente que deseja remover: "))
            lista = remover(lista, codigo_a_remover)

        elif opcao == 3:

            codigo_a_encontrar = int(input("Insira o código do paciente que deseja encontrar: "))
            encontrar(lista, codigo_a_encontrar)

        elif opcao == 4:

            chamar_paciente_urgente(lista)

        elif opcao == 5:

            listar_primeiro_ultimo(lista)

        elif opcao == 6:

            listar_por_prioridade(lista)

        elif opcao == 7:

            listar_ultimo_primeiro(lista)

        elif opcao == 8:

            contabilizar_pacientes(lista)

main()
