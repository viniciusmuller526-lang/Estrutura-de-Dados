#Crux Sacra Sit Mihi Lux

class Aluno:

    def __init__(self, matricula, nome, situacao, nota_final):

        self.matricula = matricula
        self.nome = nome
        self.situacao = situacao
        self.nota_final = nota_final
        self.proximo = None

def menu():

    print("1 - Cadastrar um aluno no final da lista")
    print("2 - Listar todos os alunos cadastrados")
    print("3 - Listar apenas alunos ativos no sistema")
    print("4 - Listar apenas alunos desativados no sistema")
    print("5 - Buscar um aluno pela matrícula")
    print("6 - Alterar nota final de um aluno")
    print("7 - Alterar a situação do aluno")
    print("8 - Remover um aluno da lista")
    print("9 - Informar a quantidade de alunos cadastrados")
    print("10 - Calcular a média das notas da turma")
    print("11 - Calcular a média das notas dos alunos ativos no sistema")
    print("12 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def cadastrar(turma, matricula, nome, situacao, nota_final):

    aluno = Aluno(matricula, nome, situacao, nota_final)

    aux = turma

    if turma == None:

        turma = aluno
        return turma

    while aux.proximo != None:

        aux = aux.proximo

    aux.proximo = aluno
    return turma

def listar(turma):

    aux = turma

    if turma == None:

        print("Turma vazia!")
        return

    while aux != None:

        print(f"Matrícula: {aux.matricula}, Nome: {aux.nome}, Situação: {aux.situacao}, Nota Final: {aux.nota_final}")
        aux = aux.proximo
    
def listar_ativos(turma):

    aux = turma

    if turma == None:

        print("Turma vazia!")
        return

    while aux != None:

        if aux.situacao == True:

            print(f"Matrícula: {aux.matricula}, Nome: {aux.nome}, Situação: {aux.situacao}, Nota Final: {aux.nota_final}")

        aux = aux.proximo

def listar_desativados(turma):

    aux = turma

    if turma == None:

        print("Turma vazia!")
        return

    while aux != None:

        if aux.situacao == False:

            print(f"Matrícula: {aux.matricula}, Nome: {aux.nome}, Situação: {aux.situacao}, Nota Final: {aux.nota_final}")

        aux = aux.proximo

def buscar_matricula(turma, matricula_pesquisada):

    aux = turma

    if turma == None:

        print("Turma vazia!")
        return

    while aux != None:

        if aux. matricula == matricula_pesquisada:

            print(f"Aluno Encontrado. Matrícula: {aux.matricula}, Nome: {aux.nome}, Situação: {aux.situacao}, Nota Final: {aux.nota_final}")
            return
    
        aux = aux.proximo

    print("Matrícula não encontrada")
    return turma

def alterar_nota(turma, matricula_nova_nota, nova_nota):

    aux = turma

    if turma == None:

        print("Turma vazia!")
        return

    while aux != None:

        if aux. matricula == matricula_nova_nota:

            aux.nota_final = nova_nota
            print("Nota alterada com sucesso")
            return turma

        aux = aux.proximo

    print("Matrícula não encontrada")
    return turma

def alterar_situacao(turma, matricula_situacao_nova):

    aux = turma

    if turma == None:

        print("Turma vazia!")
        return

    while aux != None:

        if aux. matricula == matricula_situacao_nova:

            if aux.situacao == True:

                aux.situacao = False
                print("Situação alterada com sucesso")
                return turma

            elif aux.situacao == False:

                aux.situacao = True
                print("Situação alterada com sucesso")
                return turma

        aux = aux.proximo

    print("Matrícula não encontrada")
    return turma

def remover(turma, aluno_a_remover):

    aux = turma
    anterior = None

    if turma == None:

        print("Turma vazia!")
        return

    while aux != None:

        if aux.matricula == aluno_a_remover:

            if aux == turma:

                turma = turma.proximo
                return turma

            anterior.proximo = aux.proximo
            return turma

        anterior = aux
        aux = aux.proximo

    print("Matrícula não encontrada")
    return turma

def contar_cadastrados(turma):

    aux = turma
    contador = 0

    if turma == None:

        print("Turma vazia!")
        return

    while aux != None:

        contador += 1
        aux = aux.proximo

    print(f"Há {contador} alunos cadastrados")

def media_cadastrados(turma):

    aux = turma
    soma = 0
    divisor = 0

    if turma == None:

        print("Turma vazia!")
        return

    while aux != None:

        soma += aux.nota_final
        divisor += 1
        aux = aux.proximo

    if divisor != 0:

        media = soma / divisor
        print(f"A média da turma foi de {media} pontos")
        return

    print("Impossível dividir por zero")
    
def media_ativos(turma):

    aux = turma
    soma = 0
    divisor = 0

    if turma == None:

        print("Turma vazia!")
        return

    while aux != None:

        if aux.situacao == True:

            soma += aux.nota_final
            divisor += 1

        aux = aux.proximo

    if divisor != 0:

        media = soma / divisor
        print(f"A média dos alunos ativos da turma foi de {media} pontos")
        return

    print("Impossível dividir por zero")

def main():

    turma = None
    opcao = 0

    while opcao != 12:

        opcao = menu()

        if opcao == 1:

            matricula = int(input("Insira o número de matrícula do aluno: "))
            nome = input("Insira o nome do aluno: ")
            situacao = True
            nota_final = int(input("Insira a nota final do aluno: "))
            turma = cadastrar(turma, matricula, nome, situacao, nota_final)

        elif opcao == 2:

            listar(turma)

        elif opcao == 3:

            listar_ativos(turma)

        elif opcao == 4:

            listar_desativados(turma)

        elif opcao == 5:

            matricula_pesquisada = int(input("Insira a matrícula do aluno que deseja buscar: "))
            buscar_matricula(turma, matricula_pesquisada)

        elif opcao == 6:

            matricula_nova_nota = int(input("Insira a matrícula do aluno que deseja trocar a nota final: "))
            nova_nota = int(input("Insira a nova nota:"))
            turma = alterar_nota(turma, matricula_nova_nota, nova_nota)

        elif opcao == 7:

            matricula_situacao_nova = int(input("Insira a matrícula do aluno que deseja trocar a situação: "))
            turma = alterar_situacao(turma, matricula_situacao_nova)

        elif opcao == 8:

            aluno_a_remover = int(input("Insira a matrícula do aluno que deseja remover: "))
            turma = remover(turma, aluno_a_remover)

        elif opcao == 9:

            contar_cadastrados(turma)

        elif opcao == 10:

            media_cadastrados(turma)

        elif opcao == 11:

            media_ativos(turma)

main()
