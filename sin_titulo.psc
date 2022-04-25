Algoritmo sin_titulo
	definir Des,imp,c Como Real 
	Des <- 0.2
	imp <- 0.15
	Escribir "ingrese valor compra"
	leer c
	Des <- c*0.2
	Descp <- c - Des
	imp <- Descp*0.15
	precio_f <- Descp + imp
	escribir "des :", Des
	Escribir "total_Compra :", Descp 
	Escribir "impuesto: ", imp
	Escribir "Precio final: ", precio_f
	
	
FinAlgoritmo
