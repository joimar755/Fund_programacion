# crear un programa con una funcion que calcule el 
# salario de un empleado pasando por parametros valor de la hora y horas trabajadas
def Salario(hora, vh):
    sal = hora*vh 

    return sal 

x = Salario(8,2000) 

print(type(x)) 

salario = Salario(8,2000)
print(salario)
hora,vh= x
print(hora,vh)