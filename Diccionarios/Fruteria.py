# Escribir un programa que guarde en un
#  diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y 
# muestre por pantalla el precio de ese número de kilos de fruta.
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
"""  fruta    precio
     banano   4500
     mango    5000
     limon    7000
     naranja  6000
"""
frutas = {"Banano":4500,"mango":5000,"limon":7000,"naranja":6000}
 
n = input("digite nombre de la fruta: ")
    
if n in frutas:
    print(n)
    c = int(input("digite cantidad kilo: "))
    f = frutas.get(n) 
    k = c*f
    print (k)
else:
    print("error")


