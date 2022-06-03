#Escribir un programa que almacene las asignaturas 
# de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura 
# y elimine de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
i = 0

materias = []
notas = []
while i <= 2: 
    x = len
    materias.append(input("digite la asignatura: "))
    notas.append(float(input("digite la nota: ")))
    i += 1
 
#prom = sum(notas)/x

i = 0 
while i <= 2:
    if notas[i] > 3.0:
        materias.pop(i)
    i += 1

print("las materias que tiene que repetir: ",materias)
