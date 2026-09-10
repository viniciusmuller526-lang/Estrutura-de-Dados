#Crux Sacra Sit Mihi Lux

import random

class Guerreiro:

    def __init__(self, num):

        self.nome = (f"Guerreiro {num}")
        self.proximo = None
        self.anterior = None

def menu():

    print("1 - Inserir quantidade inicial de guerreiros")
    print("2 - Simular partida")
    print("3 - Sair")
    opcao = int(input("Insira uma opção: "))
    return opcao

def inserir(lista, num):

    guerreiro = Guerreiro(num)

    if lista is None:

        guerreiro.proximo = guerreiro
        guerreiro.anterior = guerreiro
        lista = guerreiro
        return lista

    guerreiro.proximo = lista
    guerreiro.anterior = lista.anterior
    lista.anterior.proximo = guerreiro
    lista.anterior = guerreiro
    lista = guerreiro
    return lista

def simular(lista, quantidade):

    aux = lista

    for _ in range(quantidade - 1):

        passos = random.randint(1, 10)
        
        for _ in range(passos):

            aux = aux.proximo

        aux.anterior.proximo = aux.proximo
        aux.proximo.anterior = aux.anterior
        aux = aux.proximo

    print(f"Vencedor: {aux.nome}")
    return None

def main():

    lista = None
    opcao = 0
    quantidade = 0

    while opcao != 3:

        opcao = menu()

        if opcao == 1:

            quantidade = int(input("Insira a quantidade de guerreiros que vão participar: "))

            for _ in range(quantidade):

                lista = inserir(lista,_+1)

        elif opcao == 2:

            lista = simular(lista, quantidade)
            
main()
