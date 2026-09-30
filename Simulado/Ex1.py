#Crux Sacra Sit Mihi Lux

class No:

    def __init__(self, nome, responsavel):

        self.nome = nome
        self.responsavel = responsavel
        self.proximo = None

def adicionar(lista, nome, responsavel):

    no = No(nome, responsavel)

    if lista is None:

        lista = no
        return lista

    no.proximo = lista
    lista = no
    return lista

def percorrer(lista):

    aux = lista

    if lista is None:

        print("Lista vazia")
        return

    while aux != None:

        print(f"- {aux.nome}, (responsável: {aux.responsavel})")
        aux = aux.proximo

def remover(lista, nome_a_remover):

    aux = lista
    anterior = None

    if lista is None:

        print("Lista vazia")
        return

    while aux != None:

        if aux.nome == nome_a_remover:

            if aux == lista:

                lista = lista.proximo
                return lista

            anterior.proximo = aux.proximo
            return lista

        anterior = aux
        aux = aux.proximo

def main():

    lista = None

    lista = adicionar(lista, "Planejamento do Produto", "Ana")
    lista = adicionar(lista, "Implementação do Backend", "João")
    lista = adicionar(lista, "Testes Automatizados", "Carla")
    percorrer(lista)
    lista = remover(lista, "Planejamento do Produto")
    percorrer(lista)

main()
