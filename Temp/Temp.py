"""""Debido a los cambios bruscos de temperatura que se registran actualmente, se desea una aplicación que dada la temperatura actual presente en la consola un mensaje de acuerdo con la siguiente escala
entre -5 y 5 Congelados
entre 6 y 13 Frios
entre 16 y 24 Templados
entre 25 y 35 Acalorados
Mayor a 35 Evaporados""" 

def Cambio_temp(temp):
    if temp >= -5 and temp <= 5:
        print("congelados")
    elif temp >= 6 and temp <= 13:
        print("frios")
    elif temp >= 16 and temp <= 24:
        print("Templados")
    elif temp >= 25 and temp <= 35:
        print("Acalorados")
    elif temp >= 35:
        print("Evaporados")
    else:
        print("ingrese datos validos")