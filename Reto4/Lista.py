#REto4
#Se debe implementar una función que utilice ciclos y que se detenga 
#cuando el usuario no quiera ingresar mas datos a las listas, el programa 
#recibe como entrada treslistas que corresponden a: 
#1) lista de nombres de jugadores
#2) lista de edades de jugadores,
#3) lista de mundos (mundos posibles del 1 al 5)
#4) Se debe encontrar el promedio de edades de los jugadores
import statistics


i='0'
nombres= []
edad= []
mundos= [] 
 
mundos.append(int(input('digite un  mundo:')))


for elemento in mundos:  
      print(mundos)
if elemento <= 5: 
     while i != '1':
         nombres.append(input("digite nombre: "))  
         edad.append(int(input("digite edad: ")))
         i=input("digite 1 si quiere terminar o 0 para continuar: ")
         promedio = statistics.mean(edad)
        
else:
        print('incorrecto') 

print ("lista jugadores:",nombres,"edad",edad) 
print ("promedio", promedio)
        



    


    