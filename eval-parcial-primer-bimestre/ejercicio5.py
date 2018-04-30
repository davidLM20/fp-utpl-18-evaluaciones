#se declara y se pide el valor para los segundos 
nota1=float(input("Ingrese la primera nota \n "))
nota2=float(input("Ingrese la segunda nota \n "))
nota3=float(input("Ingrese la tercera nota \n "))
nota4=float(input("Ingrese la cuarta nota \n "))
#se realiza los procesos para calcular el promedio
prom = (nota1+nota2+nota3+nota4)/4
if (prom >= 90 and prom <=100):
    print("El estudiante con el promedio de calificaiones {0} , tiene una puntuacion de A\n".format(prom))
else:
    if (prom >=80 and prom <=89):
        print("El estudiante con el promedio de calificaiones {0} , tiene una puntuacion de B\n".format(prom))
    else:
        if (prom >=70 and prom <=79):
            print("El estudiante con el promedio de calificaiones {0} , tiene una puntuacion de C\n".format(prom))
        else:
            if (prom >=0 and prom <=69):
                print("El estudiante con el promedio de calificaiones {0} , tiene una puntuacion de D\n".format(prom))
