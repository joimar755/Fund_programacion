# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).



des = float()
imp = float()
c = float()
des = 0.2
imp = 0.15
print("ingrese valor compra")
c = float(input())
des = c*0.2
descp = c-des
imp = descp*0.15
precio_f = descp+imp
print("des :",des)
print("total_Compra :",descp)
print("impuesto: ",imp)
print("Precio final: ",precio_f)

