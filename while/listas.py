i = 0
materias=[]
notas=[] 

while i <=2: 
    materias.append(input("digite materia: ")) 
    notas.append(float(input("digite nota: "))) 
    i = i+1 
    prom = sum(notas)/3 
    
print (materias,notas) 
print (prom)
