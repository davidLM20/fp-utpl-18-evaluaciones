#se declara y se pide las variables 
a=float(input("Ingrese un valor para la variable a\n "))
b=float(input("Ingrese un valor para la variable b\n "))
c=float(input("Ingrese un valor para la variable c\n "))
d=float(input("Ingrese un valor para la variable d\n "))
e=float(input("Ingrese un valor para la variable e\n "))
f=float(input("Ingrese un valor para la variable f\n "))
# se realiza los calculos 
x = ((c*e)-(b*f))/((a*e)-(b*d))
y = x ;
#se presenta el mensaje de resultados
print ("La variable X tiene un valor de:  {0} y la variable Y tiene un valor de: {1}".format(x,y))
