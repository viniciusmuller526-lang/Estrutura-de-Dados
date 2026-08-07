#Crux Sacra Sit Mihi Lux

class Aluno:

    def __init__(self, nome, lista):

        self.nome = nome
        self.lista = lista
        self.media = 0

    def calcular_media(self):

        self.media = sum(self.lista) / len(self.lista)
        print(f"Aluno {self.nome} possui {self.media} de média")
    


notas_clara = []
notas_rafael = []
notas_renato = []

notas_clara.extend ([8, 9, 8])
notas_rafael.extend ([0, 4, 2])
notas_renato.extend ([5, 8, 8])

clara = Aluno("Clara", notas_clara)
rafael = Aluno("Rafael", notas_rafael)
renato = Aluno("Renato", notas_renato)

turma = []
turma.extend([clara, rafael, renato])

for aluno in turma:

    aluno.calcular_media()
