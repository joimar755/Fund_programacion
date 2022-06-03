# calcular peso ideal IBW
Altura_h = float(input("ingrese altura hombre: "))
Altura_m = float(input("ingrese altura mujer: "))  

peso_h = int(input("ingrese peso hombre: "))  
peso_M = int(input("ingrese peso mujer: "))   

Edad_h = int(input("ingrese edad hombre: "))  
Edad_m = int(input("ingrese edad mujer: "))  

minutos = int(input("ingrese minutos: ")) 
peso = int(input("ingrese el peso: "))


Caminar = 2
Tenis = 5
Montar_en_bicicleta = 14
Correr = 6
Nadar = 9.8



IMC_h = round(peso_h / (Altura_h**2),2) 
IMC_M = round(peso_M / (Altura_m**2),2)  




print("imc_h",IMC_h)
print("imc_M",IMC_M)

def calcular_IBW():
    Hombre = 56.2 + 1.41*(Altura_h / 2.54 - 60)
    Mujer = 53.1 + 1.36 * (Altura_m / 2.54 - 60)

    return print("IBW hombre es: ", Hombre , ": IBW mujer es: ", Mujer)
calcular_IBW()

#porcentaje del peso grasa 
def Calcular_Peso_Grasa():
    Hombre_a = 1.20 * IMC_h + 0.23 * Edad_h - 16.2
    Mujer_a = 1.20 * IMC_M + 0.23 * Edad_m - 5.4  

    return print("peso grasa hombre es: ", Hombre_a , ": peso grasa mujer: ", Mujer_a)
Calcular_Peso_Grasa() 

def MEtabolismo_basal():
    Hombres = 13.397*(peso_h) + 4.799*(Edad_h) - 5.677*(Altura_h) + 88.362 
    Mujeres = 9.247*(peso_M) + 3.098*(Edad_m) - 4.330*(Altura_m) + 447.593


    return print("metabolismo_basal_H: ",Hombres, " metabolismo_basal_M: ",Mujeres) 
    
MEtabolismo_basal()

def Quemando_cal():
    caminar= (minutos * Caminar * peso) / 200 
    tenis= (minutos * Tenis * peso) / 200 
    montar_en_bicicleta= (minutos * Montar_en_bicicleta * peso) / 200 
    correr= (minutos * Correr * peso) / 200 
    nadar= (minutos * Nadar * peso) / 200 
    return print("Caminar: ", caminar,
    " Tenis: ", tenis,
    " Montar_bicicletas: ",montar_en_bicicleta,
    " Correr: ",correr, 
    " Nadar: ", nadar )

Quemando_cal()