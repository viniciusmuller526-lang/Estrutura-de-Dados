#Crux Sacra Sit Mihi Lux

class Musica:

    def __init__(self, id, nome, artista, duracao):

        self.id = id
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        self.anterior = None
        self.proximo = None

def menu():

    print("1 - Adicionar música a playlist")
    print("2 - Listar todas as músicas")
    print("3 - Remover música")
    print("4 - Buscar música")
    print("5 - Mostrar a duração total da playlist")
    print("6 - Avançar música")
    print("7 - Voltar música")
    print("8 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def submenu_buscar():

    print("1 - Pesquisar por nome")
    print("2 - Pesquisar por artista")
    escolha = int(input("Digite o método de procura: "))
    return escolha

def adicionar(playlist, nome, artista, duracao, id):

    musica = Musica(id, nome, artista, duracao)

    if playlist is None:

        playlist = musica
        return playlist

    musica.proximo = playlist
    playlist.anterior = musica
    playlist = musica
    return playlist

def listar(playlist):

    aux = playlist

    if playlist is None:

        print("Playlist vazia")
        return

    while aux != None:

        print(f"Nome: {aux.nome}, Artista: {aux.artista}, Duração(em minutos): {aux.duracao} ID: {aux.id}")
        aux = aux.proximo

def remover(playlist, id_remocao):

    aux = playlist
    
    if playlist is None:

        print("Playlist vazia")
        return
    
    while aux != None:
    
        if aux.id == id_remocao:
    
            if aux.proximo == aux.anterior == None:
    
                playlist = None
                return playlist
    
            elif aux == playlist:
    
                playlist = playlist.proximo
                playlist.anterior = None
                return playlist
    
            elif aux.proximo == None:
    
                aux.anterior.proximo = None
                return playlist
    
            aux.proximo.anterior = aux.anterior
            aux.anterior.proximo = aux.proximo
            return playlist
    
        aux = aux.proximo

    print("ID n encontrado")
    return playlist

def buscar(playlist, escolha):

    aux = playlist

    if playlist == None:

        print("Playlist vazia")
        return

    if escolha == 2:

        artista = input("Digite o artista da música que deseja encontrar: ")
        musicas_artista = []

        while aux != None:

            if aux.artista == artista:

                musicas_artista.append(aux)

            aux = aux.proximo

        if not musicas_artista:

            print("Artista não encontrado")

        else:

            print("Foram encontradas as seguintes músicas para o artista buscado: ")

            for musica in musicas_artista:

                print(f"Nome: {musica.nome}, Artista: {musica.artista}, Duração(em minutos): {musica.duracao} ID: {musica.id}")

    elif escolha == 1:

        nome = input("Digite o nome da música que deseja encontrar: ")

        while aux != None:

            if aux.nome == nome:

                print(f"Música encontrada! Nome: {aux.nome}, Artista: {aux.artista}, Duração: {aux.duracao}, ID: {aux.id}")
                return

            aux = aux.proximo

        print("Música não encontrada")

def mostrar_duracao(playlist):

    aux = playlist
    duracao = 0

    while aux != None:

        duracao += aux.duracao
        aux = aux.proximo

    print(f"A duração total da playlist em minutos é de: {duracao} minutos")

def avancar(playlist, msc_atual):

    if playlist == None:
    
        print("Playlist vazia")
        return None

    if msc_atual == None:

        msc_atual = playlist
        print(f"Música tocando: Nome: {msc_atual.nome}, Artista: {msc_atual.artista}, Duração: {msc_atual.duracao}, ID: {msc_atual.id}")
        return msc_atual

    elif msc_atual != None:

        if msc_atual.proximo == None:

            print("Fim da playlist")
            return msc_atual

        msc_atual = msc_atual.proximo
        print(f"Música tocando: Nome: {msc_atual.nome}, Artista: {msc_atual.artista}, Duração: {msc_atual.duracao}, ID: {msc_atual.id}")
        return msc_atual

def anterior(playlist, msc_atual):

    if playlist == None:
        
        print("Playlist vazia")
        return None
    
    if msc_atual == None:
    
        msc_atual = playlist
        print(f"Música tocando: Nome: {msc_atual.nome}, Artista: {msc_atual.artista}, Duração: {msc_atual.duracao}, ID: {msc_atual.id}")
        return msc_atual

    elif msc_atual != None:

        if msc_atual.anterior == None:

            print("Impossível retroceder")
            return msc_atual

        msc_atual = msc_atual.anterior
        print(f"Música tocando: Nome: {msc_atual.nome}, Artista: {msc_atual.artista}, Duração: {msc_atual.duracao}, ID: {msc_atual.id}")
        return msc_atual       

def main():

    playlist = None
    msc_atual = None
    opc = 0

    while opc != 8:

        opc = menu()

        if opc == 1:

            nome = input("Insira o nome da música: ")
            artista = input("Insira o nome do artista: ")
            duracao = int(input("Inisira a duração (em minutos) da música: "))
            id = int(input("Insira uma ID: "))
            playlist = adicionar(playlist, nome, artista, duracao, id)

        elif opc == 2:

            listar(playlist)

        elif opc == 3:

            id_remocao = int(input("Insira o ID da música que deseja remover: "))

            if msc_atual and msc_atual.id == id_remocao:

                msc_atual = None

            playlist = remover(playlist, id_remocao)

        elif opc == 4:

            escolha = submenu_buscar()
            buscar(playlist,escolha)

        elif opc == 5:

            mostrar_duracao(playlist)

        elif opc == 6:

            msc_atual = avancar(playlist, msc_atual)

        elif opc == 7:

            msc_atual = anterior(playlist, msc_atual)
            
main()
