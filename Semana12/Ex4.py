#Crux Sacra Sit Mihi Lux

def media_vetor(vetor):

    def soma_vetor(vetor):

        if len(vetor) == 0:
            return 0
    
        else:
            return vetor[0] + soma_vetor(vetor[1:])
    
    soma = soma_vetor(vetor)

    if len(vetor) == 0:
        print('Vetor vazio')

    else:
        media = soma/len(vetor)
        print(media)

vetor = [1,2,3,4,5,6]
media_vetor(vetor)
