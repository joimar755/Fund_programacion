#sexo = input("digite sexo: ")
#if sexo =="hombre": 
#    print("su entrada cuesta 1000")
#elif sexo =="mujer":
#    print("su entrada cuesta 1500")

n1 = float(input("ingrese nota 1: "))
n2 = float(input("ingrese nota 2: "))
n3 = float(input("ingrese nota 3: ")) 

promedio = (n1+n2+n3) / 3 

print (promedio) 

if promedio >= 3.5:
  print("paso la materia")
else:
  print("no paso la materia")
