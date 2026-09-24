#Crux Sacra Sit Mihi Lux

class No:

    def __init__(self, nome, gols):

        self.nome = nome
        self.gols = gols
        self.proximo = None

class ListaEncadeada:

    def __init__(self):

        self.lista = None

    def adicionar_inicio(self, nome, gols):

        no = No(nome, gols)
        no.proximo = self.lista
        self.lista = no

    def adicionar_final(self, nome, gols):

        no = No(nome, gols)

        aux = self.lista

        if self.lista is None:

            self.lista = no
            return

        while aux.proximo is not None:

             aux = aux.proximo

        aux.proximo = no

    def percorrer(self):

        aux = self.lista

        if self.lista is None:

            print("Lista vazia")
            return

        while aux is not None:

            print(f"Nome do jogador: {aux.nome}, gols marcados no campeonato: {aux.gols}")
            aux = aux.proximo

    def media(self):

        aux = self.lista
        soma = 0
        contador = 0
        
        while aux is not None:

            soma += aux.gols
            contador += 1
            aux = aux.proximo

        print(f"A média de gols dos jogadores da lista foi de {soma/contador} gols")

def main():

    lista = ListaEncadeada()
    lista.adicionar_inicio("Eduardo", 4)
    lista.adicionar_inicio("Robinho", 6)
    lista.adicionar_inicio("Cafú", 10)
    lista.adicionar_final("Ronaldinho", 12)
    lista.percorrer()
    lista.media()

main()
