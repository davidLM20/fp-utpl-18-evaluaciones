# se pide valores para las variables x, y ^ z
x=float(input("Ingrese un valor para la primera variable\n "))
y=float(input("Ingrese un valor para la segunda variable\n "))
z=float(input("Ingrese un valor para la tercera variable\n "))
#se realizan las operaciones
m=float((x+(y/z))/ (x -(y/z)))
#se presenta el resultado
print ("El valor de m, en base a las variables:\n x= {0}\n\ty= {1}\n\t\tz: {2}".format(x, y, z))
print ("da como resultado:\n\t\t",m)
