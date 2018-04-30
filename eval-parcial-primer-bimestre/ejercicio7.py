#declaracion de variables 
ventas=float(input("Ingresar el valor de las ventas\n"))
sueldo= 360.40
comision=0
#condiciones y presentacion de resultados
if (ventas <=500):
    comision = ventas*0.5
    sueldo = comision+sueldo
    print("El valor del sueldo total es: {0}".format(sueldo))
else:
    if(ventas>500 & ventas <=1000 ):
        comision = ventas*0.8
        sueldo = comision+sueldo
        print("El valor del sueldo total es: {0}".format(sueldo))
    else:
        if (ventas>1000 & ventas<=5000):
            comision = ventas*0.10
            sueldo = comision+sueldo
            print("El valor del sueldo total es: {0}".format(sueldo))
        else:
            if (ventas>5000):
                comision = ventas*0.15
                sueldo = comision+sueldo
                print("El valor del sueldo total es: {0}".format(sueldo))
            

