#llenar una lista con los numeros ganadores de la loteria (6 numeros) y mostralos de forma ordenadad 
i = 0
loteria = []
while i <= 6:
  loteria.append(float(input("digite numeros ganadores: ")))
  i += 1 
  
loteria.sort() 
print(loteria)  
