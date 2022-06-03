longitud = 10
def comparar(codigo_cdia):
    cdia = len(codigo_cdia)
    if cdia > longitud:
        print("El codigo es muy largo")
    else:
        print("El codigo es correcto")     
    if codigo_cdia[6]=="@" and codigo_cdia[0]!=codigo_cdia[-1]:
     print("es un correo")
    else:
     print("CDIA no es un correo")
    
def buscar_cdia(codigo_cdia):
    usuario_1="erikaa@gmail.com"
    usuario_2="pepito@gmail.com"
    usuario_3="chepes@hotmail.com"
    if codigo_cdia==usuario_1 or codigo_cdia==usuario_2 or codigo_cdia==usuario_3:
     print("ya existe")
    else:
     print("puede crear")
    

 

def jugador():
    edad = int(input("Digite su edad: "))
    respuesta = input("Digite su respuesta: ")
    if respuesta == "si":
        
    