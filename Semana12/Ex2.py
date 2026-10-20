#Crux Sacra Sit Mihi Lux

def pares(n):
   
   if n == 0:
       return 0

   else:
       pares(n-1)

       if n % 2 == 0:
           print(n)

pares(10)
