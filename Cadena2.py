#crear un programa que pida  el correo y verifique que la primera letra es difernte de la ultima
correo = input("digite correo: ")
def verficar_cadena():
    x=len(correo)
    print(x) 
    if correo[0] != correo[x-1]:
        print("es diferente")
    else:
        print("no es diferente")
verficar_cadena()
        