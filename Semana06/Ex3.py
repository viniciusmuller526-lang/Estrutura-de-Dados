#Crux Sacra Sit Mihi Lux

#Crux Sacra Sit Mihi Lux

import random

class Carro:

    def __init__(self, nome):

        self.nome = nome
        self.proximo = None

def menu():

    print("1 - Gerar fila de carros")
    print("2 - Listar carros da fila")
    print("3 - Remover um carro da fila")
    print("4 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def criar_fila(fila):

    carros_disponiveis = ["Onix", "Prius", "Fusca", "Cayenne", "Opala"]

    escolha = carros_disponiveis[random.randint(0, 4)]
    carro = Carro(escolha)

    if fila is None:

        fila = carro
        return fila

    carro.proximo = fila
    fila = carro
    return fila

def listar(fila):

    aux = fila
    contador = 1

    if fila is None:

        print("Pilha vazia")
        return

    while aux is not None:

        print(f"{contador} - {aux.nome}")
        contador += 1
        aux = aux.proximo

def remover_carro(fila, posicao_a_remover):

    aux = fila
    contador = 0

    while True:

        if contador == posicao_a_remover - 1:

            fila = aux.proximo
            return fila

        if aux.proximo is None:

            return fila
        
        contador += 1
        aux = aux.proximo

def main():

    fila = None
    opcao = 0

    while opcao != 4:

        opcao = menu()

        if opcao == 1:

            fila = None

            for _ in range(20):

                fila = criar_fila(fila)

        elif opcao == 2:

            listar(fila)

        elif opcao == 3:

            posicao_a_remover = int(input("Insira a posição que deseja remover: "))
            fila = remover_carro(fila, posicao_a_remover)
        
main()
