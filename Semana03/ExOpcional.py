#Crux Sacra Sit Mihi Lux

class Tarefa:

    def __init__(self, descricao, prazo):

        self.descricao = descricao
        self.prazo = prazo
        self.anterior = None
        self.proximo = None
        
def menu():

    print("1 - Inserir nova tarefa")
    print("2 - Remover tarefa existente")
    print("3 - Listar todas as tarefas")
    print("4 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def inserir(lista, descricao, prazo):

    tarefa = Tarefa(descricao, prazo)

    if lista is None:

        lista = tarefa
        return lista

    tarefa.proximo = lista
    lista.anterior = tarefa
    lista = tarefa
    return lista

def remover(lista, tarefa_a_remover):

    aux = lista
    
    if lista is None:

        print("Lista vazia")
        return
    
    while aux != None:
    
        if aux.descricao == tarefa_a_remover:
    
            if aux.proximo == aux.anterior == None:
    
                lista = None
                print("Tarefa removida")
                return lista
    
            elif aux == lista:
    
                lista = lista.proximo
                lista.anterior = None
                print("Tarefa removida")
                return lista
    
            elif aux.proximo == None:
    
                aux.anterior.proximo = None
                print("Tarefa removida")
                return lista
    
            aux.proximo.anterior = aux.anterior
            aux.anterior.proximo = aux.proximo
            print("Tarefa removida")
            return lista
    
        aux = aux.proximo

    print("Descrição não encontrada")
    return lista

def listar(lista):

    aux = lista

    if lista is None:

        print("Lista vazia")
        return

    while aux != None:

        print(f"Descricao: {aux.descricao}, Prazo: {aux.prazo}")
        aux = aux.proximo

def main():

    lista = None
    opc = 0

    while opc != 4:

        opc = menu()

        if opc == 1:

            descricao = input("Insira a descrição da tarefa: ")
            prazo = input("Insira o prazo da tarefa: ")
            lista = inserir(lista, descricao, prazo)

        elif opc == 2:

            tarefa_a_remover = input("Insira a exata descrição da tarefa que deseja remover: ")
            lista = remover(lista, tarefa_a_remover)

        elif opc == 3:

            listar(lista)

main()
