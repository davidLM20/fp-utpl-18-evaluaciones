# se pide los valores para las variables de longitud y ancho 
ancho=float(input("Ingrese la longitud\n"))
longitud=float(input("Ingrese el ancho\n"))
if ancho > 0 and longitud >0 :
	superficie=(longitud * ancho)
	#se presenta el resultado
	print("La superficie de la habitacion es de: {0} metros cuadrados".format(superficie))
