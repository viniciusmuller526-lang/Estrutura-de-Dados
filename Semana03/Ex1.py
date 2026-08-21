#Crux Sacra Sit Mihi Lux

class No:

    def __init__(self, id, nome, nota):

        self.id = id
        self.nome = nome
        self.nota = nota
        self.proximo = None
        self.anterior = None

def menu():

    print("1 - Inserir Aluno")
    print("2 - Listar Alunos")
    print("3 - Remover Aluno")
    print("4 - Buscar Aluno")
    print("5 - Listar todos os alunos classificados como: a) Aprovado (nota ≥ 7,0), b) Exame (nota entre 4,0 e 6,9), c) Reprovado (nota < 4,0)")
    print("6 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def inserir(lista, id, nome, nota):

    novo = No(id, nome, nota)

    if lista is None:

        lista = novo
        return lista

    novo.proximo = lista
    lista.anterior = novo
    lista = novo
    return lista

def listar(lista):

    aux = lista

    if lista is None:
    
        print("Lista vazia")
        return

    while aux != None:
        
        print(f"Nome: {aux.nome}, ID: {aux.id}, Nota final: {aux.nota}")
        aux = aux.proximo

def remover(lista, id):

    aux = lista

    if lista is None:

        print("Lista vazia")
        return

    while aux != None:

        if aux.id == id:

            if aux.proximo == aux.anterior == None:

                lista = None
                return lista

            elif aux == lista:

                lista = lista.proximo
                lista.anterior = None
                return lista

            elif aux.proximo == None:

                aux.anterior.proximo = None

            aux.proximo.anterior = aux.anterior
            aux.anterior.proximo = aux.proximo
            return lista

        aux = aux.proximo

def encontrar(lista, id):

    aux = lista

    while aux != None:

        if aux.id == id:

            print(f"Nome do aluno: {aux.nome}, ID: {aux.id}, Nota final: {aux.nota}")
            return

        aux = aux.proximo

def listar_estado(lista):

    aux = lista

    while aux != None:

        if aux.nota >= 7:

            print(f"Aluno: {aux.nome}, ID: {aux.id}, Estado: Aprovado")

        elif aux.nota >= 4 and aux.nota < 7:
        
            print(f"Aluno: {aux.nome}, ID: {aux.id}, Estado: Exame")

        elif aux.nota < 4:

            print(f"Aluno: {aux.nome}, ID: {aux.id}, Estado: Reprovado")

        aux = aux.proximo

def main():

    lista = None
    opcao = 0

    while opcao != 6:

        opcao = menu()

        if opcao == 1:

            id = int(input("Insira a ID do novo aluno: "))
            nome = input("Insira o nome do aluno: ")
            nota = float(input("Insira a nota final do aluno: "))
            lista = inserir(lista, id, nome, nota)

        elif opcao == 2:

            listar(lista)

        elif opcao == 3:

            id = int(input("Insira a id do aluno que deseja remover: "))
            lista = remover(lista, id)

        elif opcao == 4:

            id = int(input("Insira a id do aluno que deseja encontrar: "))
            encontrar(lista, id)

        elif opcao == 5:

            listar_estado(lista)
            
main()
