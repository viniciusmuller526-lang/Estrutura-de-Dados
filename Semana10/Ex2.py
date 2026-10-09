#Crux Sacra Sit Mihi Lux

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def inserir_head(self, dado):
        novo = No(dado)

        if self.head == None:
            self.head = self.tail = novo
            return

        novo.proximo = self.head
        self.head.anterior = novo
        self.head = novo

    def inserir_tail(self, dado):
        novo = No(dado)

        if self.tail is None:
            self.tail = self.head = novo
            return

        novo.anterior = self.tail
        self.tail.proximo = novo
        self.tail = novo

    def atender(self):

        if self.head is None:
            print("Deque vazio")
            return

        if self.head == self.tail:
            self.head = self.tail =  None
            return

        self.head = self.head.proximo
        self.head.anterior = None

    def mostrar_fila(self):

        if self.head is None:
            print(" vazio")
            return
        
        aux = self.head

        while aux != None:
            print("- ", aux.dado)
            aux = aux.proximo

def menu():
    print("1 - Inserir")
    print("2 - Atender")
    print("3 - Mostrar fila")
    print("4 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def main():
    opcao = 0
    deque = Deque()

    while opcao != 6:
        opcao = menu()
        if opcao == 1:
            dado = input("Insira o tipo de cliente: ")

            if dado == "preferencial":
                deque.inserir_head(dado)
            else:
                deque.inserir_tail(dado)
        elif opcao == 2:
            deque.atender()
        elif opcao == 3:
            deque.mostrar_fila()

main()
