#el total pagar por todos los productos que lleve un cliente 
from itertools import product


i='0'
producto=[]
while i!= '1':
  producto.append(float(input("digite el valor del producto: ")))
  i=input("digite 1 si quiere terminar o 0 para continuar: ")


  total=sum(producto) 

print("el total es: ",total)

 