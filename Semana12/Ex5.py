#Crux Sacra Sit Mihi Lux

def mostrar_num_caixas(n):

    if n == 0:
        return
    
    else:
        print(n) 
        mostrar_num_caixas(n-1)

mostrar_num_caixas(10)
