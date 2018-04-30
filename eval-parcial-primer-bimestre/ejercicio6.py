#se declara y se pide el valor de la variable 
mes=int(input("Ingrese el numero de mes\n"))

#se realiza la verificacion de la variable para la presentacion del mensaje 
if (mes == 1 or  mes ==3 or mes ==5 or  mes ==7 or  mes ==8 or mes ==10 or mes ==12):
    dias = 31
    print("El mes tiene {0} dias\n".format(dias))
else: 
    if (mes == 4 or mes ==6 or mes ==9 or mes ==11):
        dias = 30
        print("El mes tiene {0} dias\n".format(dias))
    else:
        if (mes ==2):
            dias =28
            print("El mes tiene {0} dias\n".format(dias))
        else:
            print("El numero ingresado es incorrecto")
            
    
