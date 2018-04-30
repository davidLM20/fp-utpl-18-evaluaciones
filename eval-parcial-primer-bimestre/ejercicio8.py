#se declara y se pide las variables
uno=(input("Ingrese la primera letra\n"))
dos=(input("Ingrese la segunda letra\n"))
tres=(input("Ingrese la tercera letra\n"))
#condiciones y presentacion de mensajes 
if (uno<dos and uno<tres):
	print("La primera letra es: {0}".format(uno))
elif(dos<uno and dos<tres):
	print("La primera letra es: {0}".format(dos))
elif(tres<uno and tres<dos):
	print("La primera letra es: {0}".format(tres))
