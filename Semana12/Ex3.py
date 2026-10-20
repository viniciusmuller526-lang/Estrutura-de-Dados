#Crux Sacra Sit Mihi Lux

def soma_impares(n):
    
   if n == 0:
       return 0

   else:
        if n % 2 != 0:
            return n + soma_impares(n-1)

        else:
            return soma_impares(n-1)

print(soma_impares(9))
